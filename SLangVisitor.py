# Generated from SLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SLangParser import SLangParser
else:
    from SLangParser import SLangParser

# This class defines a complete generic visitor for a parse tree produced by SLangParser.

class SLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SLangParser#program.
    def visitProgram(self, ctx:SLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#statement.
    def visitStatement(self, ctx:SLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#block.
    def visitBlock(self, ctx:SLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SLangParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:SLangParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#printStatement.
    def visitPrintStatement(self, ctx:SLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#ifStatement.
    def visitIfStatement(self, ctx:SLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#whileStatement.
    def visitWhileStatement(self, ctx:SLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#forLoop.
    def visitForLoop(self, ctx:SLangParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#breakStatement.
    def visitBreakStatement(self, ctx:SLangParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#expressionStatement.
    def visitExpressionStatement(self, ctx:SLangParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#expression.
    def visitExpression(self, ctx:SLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:SLangParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:SLangParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:SLangParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#equalityExpression.
    def visitEqualityExpression(self, ctx:SLangParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#relationalExpression.
    def visitRelationalExpression(self, ctx:SLangParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:SLangParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SLangParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#unaryExpression.
    def visitUnaryExpression(self, ctx:SLangParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:SLangParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:SLangParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#functionCall.
    def visitFunctionCall(self, ctx:SLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#literal.
    def visitLiteral(self, ctx:SLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SLangParser#typeType.
    def visitTypeType(self, ctx:SLangParser.TypeTypeContext):
        return self.visitChildren(ctx)



del SLangParser