from antlr4 import *
from SLangLexer import SLangLexer
from SLangParser import SLangParser
from SLangVisitor import SLangVisitor
from collections import defaultdict
import sys


class SLangInterpreter(SLangVisitor):
    def __init__(self):
        self.variables = defaultdict(lambda: None)
        self.types = {}

    # Helper to convert literal to Python value
    # def literal_to_value(self, literal):
    #     if literal.INTEGER():
    #         return int(literal.getText())
    #     elif literal.FLOATING_POINT():
    #         return float(literal.getText())
    #     elif literal.STRING_LITERAL():
    #         return literal.getText()[1:-1]  # Remove quotes
    #     elif literal.TRUE():
    #         return True
    #     elif literal.FALSE():
    #         return False
    #     return None

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

    # Helper to get type as string
    def get_type_string(self, type_node):
        if type_node.INT(): return "int"
        if type_node.FLOAT(): return "float"
        if type_node.BOOLEAN(): return "boolean"
        if type_node.STRING(): return "string"
        if type_node.ARRAY(): return "array"
        return None

    # Program: Execute a
    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return None

    # Statement types
    def visitVariableDeclaration(self, ctx):
        var_type = self.get_type_string(ctx.typeType())
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        # Type checking
        if var_type == "int" and not isinstance(value, int):
            raise ValueError(f"Type mismatch: Expected int for {var_name}, got {type(value)}")
        elif var_type == "float" and not isinstance(value, (int, float)):
            raise ValueError(f"Type mismatch: Expected float for {var_name}, got {type(value)}")
        elif var_type == "boolean" and not isinstance(value, bool):
            raise ValueError(f"Type mismatch: Expected boolean for {var_name}, got {type(value)}")
        elif var_type == "string" and not isinstance(value, str):
            raise ValueError(f"Type mismatch: Expected string for {var_name}, got {type(value)}")
        elif var_type == "array" and not isinstance(value, list):
            raise ValueError(f"Type mismatch: Expected array for {var_name}, got {type(value)}")

        self.variables[var_name] = value
        self.types[var_name] = var_type
        return None

    def visitAssignmentStatement(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        index = None

        # Check for array index
        if ctx.expression(0) and ctx.expression(1):
            index = self.visit(ctx.expression(0))
            if not isinstance(index, int):
                raise ValueError("Array index must be an integer")
            value = self.visit(ctx.expression(1))
        else:
            value = self.visit(ctx.expression(0))

        # Assign to array element
        if index is not None:
            if var_name not in self.variables or not isinstance(self.variables[var_name], list):
                raise ValueError(f"{var_name} is not an array")
            if index < 0 or index >= len(self.variables[var_name]):
                raise ValueError("Array index out of bounds")
            self.variables[var_name][index] = value
        else:
            # Assign to regular variable
            if var_name not in self.variables:
                raise ValueError(f"Variable {var_name} not declared")
            self.variables[var_name] = value

        return None

    # def visitAssignmentStatement(self, ctx):
    #     var_name = ctx.IDENTIFIER().getText()
    #     index = None
    #     if ctx.expression(0):  # Array index
    #         index = self.visit(ctx.expression(0))
    #         if not isinstance(index, int):
    #             raise ValueError("Array index must be an integer")
    #
    #     value = self.visit(ctx.expression(1) if index is None else ctx.expression(1))
    #
    #     if index is not None:
    #         if var_name not in self.variables or not isinstance(self.variables[var_name], list):
    #             raise ValueError(f"{var_name} is not an array")
    #         if index < 0 or index >= len(self.variables[var_name]):
    #             raise ValueError("Array index out of bounds")
    #         self.variables[var_name][index] = value
    #     else:
    #         if var_name not in self.variables:
    #             raise ValueError(f"Variable {var_name} not declared")
    #         self.variables[var_name] = value
    #     return None

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expression())
        print(value)
        return None

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if not isinstance(condition, bool):
            raise ValueError("If condition must be boolean")

        if condition:
            self.visit(ctx.block(0))
        elif ctx.block(1):  # Else block
            self.visit(ctx.block(1))
        return None

    def visitForLoop(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        array = self.visit(ctx.expression())
        if not isinstance(array, list):
            raise ValueError("For loop must iterate over an array")

        for value in array:
            self.variables[var_name] = value
            self.visit(ctx.block())
        return None

    def visitExpressionStatement(self, ctx):
        self.visit(ctx.expression())
        return None

    def visitBlock(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return None

    # Expressions
    def visitExpression(self, ctx):
        return self.visit(ctx.conditionalExpression())

    def visitConditionalExpression(self, ctx):
        if ctx.expression():  # Ternary operator
            condition = self.visit(ctx.logicalOrExpression())
            if not isinstance(condition, bool):
                raise ValueError("Ternary condition must be boolean")
            return self.visit(ctx.expression(0)) if condition else self.visit(ctx.expression(1))
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            right = self.visit(ctx.logicalAndExpression(i))
            if not (isinstance(result, bool) and isinstance(right, bool)):
                raise ValueError("Logical OR requires boolean operands")
            result = result or right
        return result

    def visitLogicalAndExpression(self, ctx):
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, len(ctx.equalityExpression())):
            right = self.visit(ctx.equalityExpression(i))
            if not (isinstance(result, bool) and isinstance(right, bool)):
                raise ValueError("Logical AND requires boolean operands")
            result = result and right
        return result

    def visitEqualityExpression(self, ctx):
        result = self.visit(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            right = self.visit(ctx.relationalExpression(i))
            op = ctx.getChild(2 * i - 1).getText()
            if op == "==":
                result = result == right
            elif op == "!=":
                result = result != right
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
        return result

    def visitMultiplicativeExpression(self, ctx):
        result = self.visit(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            right = self.visit(ctx.unaryExpression(i))
            op = ctx.getChild(2 * i - 1).getText()
            if op == "*":
                result = result * right
            elif op == "/":
                result = result / right
            elif op == "%":
                result = result % right
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
                raise ValueError("Logical NOT requires boolean operand")
            return not value

    def visitPrimaryExpression(self, ctx):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                raise ValueError(f"Variable {var_name} not declared")
            if ctx.expression():  # Array access
                index = self.visit(ctx.expression())
                if not isinstance(index, int):
                    raise ValueError("Array index must be integer")
                if not isinstance(self.variables[var_name], list):
                    raise ValueError(f"{var_name} is not an array")
                if index >= len(self.variables[var_name]):
                    raise ValueError("Array index out of bounds")
                return self.variables[var_name][index]
            return self.variables[var_name]
        elif ctx.literal():
            return self.literal_to_value(ctx.literal())
        elif ctx.LPAREN():
            return self.visit(ctx.expression())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())
        return None

    def visitArrayLiteral(self, ctx):
        elements = [self.visit(expr) for expr in ctx.expression()]
        return elements

    def visitFunctionCall(self, ctx):
        # For now, we'll assume no user-defined functions
        raise ValueError("Function calls not supported in this interpreter")


def interpret(code):
    input_stream = InputStream(code)
    lexer = SLangLexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = SLangParser(stream)
    tree = parser.program()
    interpreter = SLangInterpreter()
    interpreter.visit(tree)


if __name__ == "__main__":
    # Example usage
    sample_code = """
    print("Slang says Hello!")
    var int x = 5
    var float y = 3.14
    var boolean isActive = true
    
    print x
    print y
    print "Hello, World!"
    
    if (x > 0) {
        print "x is positive"
        } 
    else {
    print "x is non-positive"
        }
    
    var array arr = [1, 2, 3]
    for i in arr {
    print (i)
    print (i*10)
    }
    
    var int y = 10
    var array numbers = [4,5,6,7]
    for num in numbers{
    y = num + 10
    print(y)
    }
    

    """
    interpret(sample_code)