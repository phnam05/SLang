from antlr4 import *
from SLangLexer import SLangLexer
from SLangParser import SLangParser
from SLangVisitor import SLangVisitor
from antlr4.error.ErrorListener import ErrorListener
from collections import defaultdict
import sys
import traceback
from Errors import (
    SLangSyntaxError,
    SLangNameError,
    SLangValueError,
    SLangTypeError,
    SLangIndexError,
    SLangBaseError,
    SLangBreakException
)

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        offending_text = offendingSymbol.text if offendingSymbol else "unknown"

        if "missing {'int', 'float', 'boolean', 'string'" in msg:
            custom_msg = (
                f"Unrecognized variable declaration at line {line}, column {column}: "
                f"'{offending_text}' is not a valid type."
            )
        else:
            custom_msg = f"Syntax error at line {line}, column {column}: {msg}"

        raise SLangSyntaxError(custom_msg, None)



class SLangInterpreter(SLangVisitor):

    def __init__(self):
        self.variables = defaultdict(lambda: None)
        self.types = {}

    # def debug_ctx(self, ctx, label=None):
    #     try:
    #         label = label or ctx.__class__.__name__
    #         line = getattr(ctx.start, 'line', '?')
    #         col = getattr(ctx.start, 'column', '?')
    #         print(f"[DEBUG] Visiting {label}: line {line}, col {col}, text: {ctx.getText()}")
    #     except Exception as e:
    #         print(f"[DEBUG] Visiting {label or 'Unknown'}: ctx info unavailable ({e})")
    #
    # def visit(self, tree):
    #     # Overridden visit() to include automatic ctx printing
    #     if hasattr(tree, "getText") and hasattr(tree, "start"):
    #         self.debug_ctx(tree)
    #     return super().visit(tree)

    def literal_to_value(self, literal):
        if literal.INTEGER():
            return int(literal.INTEGER().getText())
        elif literal.FLOATING_POINT():
            return float(literal.FLOATING_POINT().getText())
        elif literal.STRING_LITERAL():
            return literal.STRING_LITERAL().getText()[1:-1]
        elif literal.TRUE():
            return True
        elif literal.FALSE():
            return False
        return None

    def get_type_string(self, type_node):
        if type_node.INT(): return "int"
        if type_node.FLOAT(): return "float"
        if type_node.BOOLEAN(): return "boolean"
        if type_node.STRING(): return "string"
        if type_node.ARRAY(): return "array"
        return None

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    def visitVariableDeclaration(self, ctx):
        var_type = self.get_type_string(ctx.typeType())
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        # ✋ Check for redeclaration
        if var_name in self.types:
            raise SLangNameError(f"Variable '{var_name}' already declared", ctx)

        if var_type == "int" and (not isinstance(value, int) or isinstance(value, bool)):
            raise SLangTypeError(f"Expected int for '{var_name}', got {type(value).__name__}", ctx)
        elif var_type == "float" and not isinstance(value, (int, float)):
            raise SLangTypeError(f"Expected float for '{var_name}', got {type(value).__name__}", ctx)
        elif var_type == "boolean" and not isinstance(value, bool):
            raise SLangTypeError(f"Expected boolean for '{var_name}', got {type(value).__name__}", ctx)
        elif var_type == "string" and not isinstance(value, str):
            raise SLangTypeError(f"Expected string for '{var_name}', got {type(value).__name__}", ctx)
        elif var_type == "array" and not isinstance(value, list):
            raise SLangTypeError(f"Expected array for '{var_name}', got {type(value).__name__}", ctx)

        self.variables[var_name] = value
        self.types[var_name] = var_type

    def visitAssignmentStatement(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        index = None

        if ctx.expression(0) and ctx.expression(1):
            # This is an array assignment: arr[2] = value
            index = self.visit(ctx.expression(0))
            if not isinstance(index, int):
                raise SLangTypeError("Array index must be an integer", ctx)
            value = self.visit(ctx.expression(1))
        else:
            # This is a normal assignment: x = value
            value = self.visit(ctx.expression(0))

        if var_name not in self.variables:
            raise SLangNameError(f"Variable '{var_name}' not declared", ctx)

        if index is not None:
            # Array element assignment
            if not isinstance(self.variables[var_name], list):
                raise SLangTypeError(f"{var_name} is not an array", ctx)
            if index < 0 or index >= len(self.variables[var_name]):
                raise SLangIndexError("Array index out of bounds", ctx)
            # 🛡️ No type checking for array elements!
            self.variables[var_name][index] = value
        else:
            # Whole variable assignment
            expected_type = self.types.get(var_name)

            if expected_type == "int" and not isinstance(value, int):
                raise SLangTypeError(f"Expected int for '{var_name}', got {type(value).__name__}", ctx)
            elif expected_type == "float" and not isinstance(value, (int, float)):
                raise SLangTypeError(f"Expected float for '{var_name}', got {type(value).__name__}", ctx)
            elif expected_type == "boolean" and not isinstance(value, bool):
                raise SLangTypeError(f"Expected boolean for '{var_name}', got {type(value).__name__}", ctx)
            elif expected_type == "string" and not isinstance(value, str):
                raise SLangTypeError(f"Expected string for '{var_name}', got {type(value).__name__}", ctx)
            elif expected_type == "array" and not isinstance(value, list):
                raise SLangTypeError(f"Expected array for '{var_name}', got {type(value).__name__}", ctx)

            self.variables[var_name] = value

    # def visitPrintStatement(self, ctx):
    #     value = self.visit(ctx.expression())
    #     sys.stdout.flush()  # Flush before printing (important in case previous outputs pending)
    #     print(value)
    # #     sys.stdout.flush()  # Flush immediately after printing (to push it out before any error happens)
    def visitPrintStatement(self, ctx):
        values = [self.visit(expr) for expr in ctx.expression()]
        sys.stdout.flush()
        print(*values)
        sys.stdout.flush()


    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if not isinstance(condition, bool):
            raise SLangTypeError("If condition must be boolean", ctx)
        if condition:
            self.visit(ctx.block(0))
        elif ctx.block(1):
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        try:
            while True:
                condition = self.visit(ctx.expression())
                if not isinstance(condition, bool):
                    raise SLangTypeError("While condition must be boolean", ctx)
                if not condition:
                    break
                try:
                    self.visit(ctx.block())
                except SLangBreakException:
                    break
        except SLangBreakException:
            # Break from the outer loop (useful for nested loops)
            raise

    def visitForLoop(self, ctx):
        try:
            var_name = ctx.IDENTIFIER().getText()
            array = self.visit(ctx.expression())
            if not isinstance(array, list):
                raise SLangTypeError("For loop must iterate over an array", ctx)
            for value in array:
                self.variables[var_name] = value
                try:
                    self.visit(ctx.block())
                except SLangBreakException:
                    break
        except SLangBreakException:
            # Re-raise if this is a nested loop break
            raise

    def visitBreakStatement(self, ctx):
        # Raise the break exception - it will be caught by the loop
        raise SLangBreakException("'break' outside loop", ctx)

    def visitExpressionStatement(self, ctx):
        self.visit(ctx.expression())

    def visitBlock(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    def visitExpression(self, ctx):
        return self.visit(ctx.conditionalExpression())

    def visitConditionalExpression(self, ctx):
        if ctx.expression():
            condition = self.visit(ctx.logicalOrExpression())
            if not isinstance(condition, bool):
                raise SLangTypeError("Ternary condition must be boolean", ctx)
            return self.visit(ctx.expression(0)) if condition else self.visit(ctx.expression(1))
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            right = self.visit(ctx.logicalAndExpression(i))
            if not (isinstance(result, bool) and isinstance(right, bool)):
                raise SLangTypeError("Logical OR requires boolean operands", ctx)
            result = result or right
        return result

    def visitLogicalAndExpression(self, ctx):
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, len(ctx.equalityExpression())):
            right = self.visit(ctx.equalityExpression(i))
            if not (isinstance(result, bool) and isinstance(right, bool)):
                raise SLangTypeError("Logical AND requires boolean operands", ctx)
            result = result and right
        return result

    def visitEqualityExpression(self, ctx):
        result = self.visit(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            right = self.visit(ctx.relationalExpression(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "==" or op == "is":
                result = result == right
            elif op == "!=" or op == "aint":
                result = result != right
            else:
                raise SLangSyntaxError(f"Unsupported operator '{op}'", ctx)
        return result

    def visitRelationalExpression(self, ctx):
        result = self.visit(ctx.additiveExpression(0))
        for i in range(1, len(ctx.additiveExpression())):
            right = self.visit(ctx.additiveExpression(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "<":
                result = result < right
            elif op == "<=":
                result = result <= right
            elif op == ">":
                result = result > right
            elif op == ">=":
                result = result >= right
            else:
                raise SLangSyntaxError(f"Unsupported operator '{op}'", ctx)
        return result

    def visitAdditiveExpression(self, ctx):
        result = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            right = self.visit(ctx.multiplicativeExpression(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "+":
                result = result + right
            elif op == "-":
                result = result - right
            else:
                raise SLangSyntaxError(f"Unsupported operator '{op}'", ctx)
        return result

    def visitMultiplicativeExpression(self, ctx):
        result = self.visit(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            right = self.visit(ctx.unaryExpression(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "/":
                if right == 0:
                    raise SLangValueError("Division by zero", ctx)
                result = result / right
            elif op == "*":
                result = result * right
            elif op == "%":
                if right == 0:
                    raise SLangValueError("Modulo by zero", ctx)
                result = result % right
            else:
                raise SLangSyntaxError(f"Unsupported operator '{op}'", ctx)
        return result

    def visitUnaryExpression(self, ctx):
        if ctx.primaryExpression():
            return self.visit(ctx.primaryExpression())
        op = ctx.getChild(0).getText()

        value = self.visit(ctx.unaryExpression())
        if op == "+":
            return value
        elif op == "-":
            return -value
        elif op == "!":
            if not isinstance(value, bool):
                raise SLangTypeError("Logical NOT requires boolean operand", ctx)
            return not value
        else:
            raise SLangSyntaxError(f"Unsupported operator '{op}'", ctx)

    def visitPrimaryExpression(self, ctx):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                raise SLangNameError(f"Variable '{var_name}' not declared", ctx)
            if ctx.expression():
                index = self.visit(ctx.expression())
                if not isinstance(index, int):
                    raise SLangTypeError("Array index must be integer", ctx)
                if not isinstance(self.variables[var_name], list):
                    raise SLangTypeError(f"{var_name} is not an array", ctx)
                if index < 0 or  index >= len(self.variables[var_name]):
                    raise SLangIndexError("Array index out of bounds", ctx)
                return self.variables[var_name][index]
            return self.variables[var_name]
        elif ctx.literal():
            return self.literal_to_value(ctx.literal())
        elif ctx.LPAREN():
            return self.visit(ctx.expression())
        elif ctx.functionCall():
            raise SLangValueError("Function calls not supported", ctx)
        elif ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())
        else:
            raise SLangSyntaxError(f"Unsupported operator'", ctx)
        return None

    def visitArrayLiteral(self, ctx):
        return [self.visit(expr) for expr in ctx.expression()]

def interpret(code):
    input_stream = InputStream(code)
    lexer = SLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    #print("LEXER PART")

    stream = CommonTokenStream(lexer)
    parser = SLangParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    #print("PARSER PART")
    tree = parser.program()
    interpreter = SLangInterpreter()
   # print("REACHED INTERPRETER")
    interpreter.visit(tree)
    #print("TREE VISIT COMPLETE")


if __name__ == "__main__":
    try:
        # Check if a file name was provided
        if len(sys.argv) > 1:
            # Use the provided file name
            filename = sys.argv[1]
        else:
            # Default to "tests.txt" for backward compatibility
            filename = "test.slang"
            
        # Open and read the file
        with open(filename, "r") as file:
            code = file.read()
            
        interpret(code)
    except SLangBaseError as e:
        sys.stderr.write(str(e) + "\n")
    except FileNotFoundError as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.stderr.write(f"Usage: python {sys.argv[0]} [filename]\n")
    except Exception as e:
        import traceback
        traceback.print_exception(type(e), e, e.__traceback__)

