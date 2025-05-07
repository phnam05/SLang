# Generated from SLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SLangParser import SLangParser
else:
    from SLangParser import SLangParser

# This class defines a complete listener for a parse tree produced by SLangParser.
class SLangListener(ParseTreeListener):

    # Enter a parse tree produced by SLangParser#program.
    def enterProgram(self, ctx:SLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SLangParser#program.
    def exitProgram(self, ctx:SLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SLangParser#statement.
    def enterStatement(self, ctx:SLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SLangParser#statement.
    def exitStatement(self, ctx:SLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SLangParser#block.
    def enterBlock(self, ctx:SLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SLangParser#block.
    def exitBlock(self, ctx:SLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SLangParser#breakStatement.
    def enterBreakStatement(self, ctx:SLangParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SLangParser#breakStatement.
    def exitBreakStatement(self, ctx:SLangParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SLangParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SLangParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by SLangParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SLangParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by SLangParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:SLangParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by SLangParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:SLangParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by SLangParser#printStatement.
    def enterPrintStatement(self, ctx:SLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SLangParser#printStatement.
    def exitPrintStatement(self, ctx:SLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by SLangParser#ifStatement.
    def enterIfStatement(self, ctx:SLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SLangParser#ifStatement.
    def exitIfStatement(self, ctx:SLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SLangParser#whileStatement.
    def enterWhileStatement(self, ctx:SLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SLangParser#whileStatement.
    def exitWhileStatement(self, ctx:SLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SLangParser#forLoop.
    def enterForLoop(self, ctx:SLangParser.ForLoopContext):
        pass

    # Exit a parse tree produced by SLangParser#forLoop.
    def exitForLoop(self, ctx:SLangParser.ForLoopContext):
        pass


    # Enter a parse tree produced by SLangParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SLangParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SLangParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SLangParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SLangParser#expression.
    def enterExpression(self, ctx:SLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#expression.
    def exitExpression(self, ctx:SLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:SLangParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:SLangParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:SLangParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:SLangParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:SLangParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:SLangParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#equalityExpression.
    def enterEqualityExpression(self, ctx:SLangParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#equalityExpression.
    def exitEqualityExpression(self, ctx:SLangParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SLangParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SLangParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SLangParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SLangParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SLangParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SLangParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#unaryExpression.
    def enterUnaryExpression(self, ctx:SLangParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#unaryExpression.
    def exitUnaryExpression(self, ctx:SLangParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SLangParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SLangParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SLangParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SLangParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:SLangParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by SLangParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:SLangParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by SLangParser#functionCall.
    def enterFunctionCall(self, ctx:SLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SLangParser#functionCall.
    def exitFunctionCall(self, ctx:SLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SLangParser#literal.
    def enterLiteral(self, ctx:SLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by SLangParser#literal.
    def exitLiteral(self, ctx:SLangParser.LiteralContext):
        pass


    # Enter a parse tree produced by SLangParser#typeType.
    def enterTypeType(self, ctx:SLangParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by SLangParser#typeType.
    def exitTypeType(self, ctx:SLangParser.TypeTypeContext):
        pass



del SLangParser