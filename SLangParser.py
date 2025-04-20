# Generated from SLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,225,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,4,0,50,8,0,11,0,12,0,51,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,5,2,66,8,2,10,2,
        12,2,69,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        3,4,84,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,99,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,123,8,11,1,12,1,12,
        1,12,5,12,128,8,12,10,12,12,12,131,9,12,1,13,1,13,1,13,5,13,136,
        8,13,10,13,12,13,139,9,13,1,14,1,14,1,14,5,14,144,8,14,10,14,12,
        14,147,9,14,1,15,1,15,1,15,5,15,152,8,15,10,15,12,15,155,9,15,1,
        16,1,16,1,16,5,16,160,8,16,10,16,12,16,163,9,16,1,17,1,17,1,17,5,
        17,168,8,17,10,17,12,17,171,9,17,1,18,1,18,1,18,3,18,176,8,18,1,
        19,1,19,1,19,1,19,1,19,3,19,183,8,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,3,19,192,8,19,1,20,1,20,1,20,1,20,5,20,198,8,20,10,20,12,
        20,201,9,20,3,20,203,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,5,21,
        212,8,21,10,21,12,21,215,9,21,3,21,217,8,21,1,21,1,21,1,22,1,22,
        1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,0,7,1,0,29,30,1,0,31,34,1,0,24,25,1,0,26,
        28,2,0,24,25,37,37,2,0,12,13,19,21,1,0,14,18,226,0,49,1,0,0,0,2,
        61,1,0,0,0,4,63,1,0,0,0,6,72,1,0,0,0,8,78,1,0,0,0,10,88,1,0,0,0,
        12,91,1,0,0,0,14,100,1,0,0,0,16,106,1,0,0,0,18,112,1,0,0,0,20,114,
        1,0,0,0,22,116,1,0,0,0,24,124,1,0,0,0,26,132,1,0,0,0,28,140,1,0,
        0,0,30,148,1,0,0,0,32,156,1,0,0,0,34,164,1,0,0,0,36,175,1,0,0,0,
        38,191,1,0,0,0,40,193,1,0,0,0,42,206,1,0,0,0,44,220,1,0,0,0,46,222,
        1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,
        51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,62,3,6,
        3,0,56,62,3,8,4,0,57,62,3,10,5,0,58,62,3,12,6,0,59,62,3,16,8,0,60,
        62,3,18,9,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,
        0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,67,5,44,0,0,64,66,
        3,2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,
        68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,45,0,0,71,5,1,0,0,0,72,73,5,
        5,0,0,73,74,3,46,23,0,74,75,5,22,0,0,75,76,5,23,0,0,76,77,3,20,10,
        0,77,7,1,0,0,0,78,83,5,22,0,0,79,80,5,40,0,0,80,81,3,20,10,0,81,
        82,5,41,0,0,82,84,1,0,0,0,83,79,1,0,0,0,83,84,1,0,0,0,84,85,1,0,
        0,0,85,86,5,23,0,0,86,87,3,20,10,0,87,9,1,0,0,0,88,89,5,6,0,0,89,
        90,3,20,10,0,90,11,1,0,0,0,91,92,5,7,0,0,92,93,5,38,0,0,93,94,3,
        20,10,0,94,95,5,39,0,0,95,98,3,4,2,0,96,97,5,8,0,0,97,99,3,4,2,0,
        98,96,1,0,0,0,98,99,1,0,0,0,99,13,1,0,0,0,100,101,5,9,0,0,101,102,
        5,38,0,0,102,103,3,20,10,0,103,104,5,39,0,0,104,105,3,4,2,0,105,
        15,1,0,0,0,106,107,5,10,0,0,107,108,5,22,0,0,108,109,5,11,0,0,109,
        110,3,20,10,0,110,111,3,4,2,0,111,17,1,0,0,0,112,113,3,20,10,0,113,
        19,1,0,0,0,114,115,3,22,11,0,115,21,1,0,0,0,116,122,3,24,12,0,117,
        118,5,1,0,0,118,119,3,20,10,0,119,120,5,2,0,0,120,121,3,20,10,0,
        121,123,1,0,0,0,122,117,1,0,0,0,122,123,1,0,0,0,123,23,1,0,0,0,124,
        129,3,26,13,0,125,126,5,36,0,0,126,128,3,26,13,0,127,125,1,0,0,0,
        128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,25,1,0,0,0,131,
        129,1,0,0,0,132,137,3,28,14,0,133,134,5,35,0,0,134,136,3,28,14,0,
        135,133,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,
        138,27,1,0,0,0,139,137,1,0,0,0,140,145,3,30,15,0,141,142,7,0,0,0,
        142,144,3,30,15,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,
        0,145,146,1,0,0,0,146,29,1,0,0,0,147,145,1,0,0,0,148,153,3,32,16,
        0,149,150,7,1,0,0,150,152,3,32,16,0,151,149,1,0,0,0,152,155,1,0,
        0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,31,1,0,0,0,155,153,1,0,0,
        0,156,161,3,34,17,0,157,158,7,2,0,0,158,160,3,34,17,0,159,157,1,
        0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,33,1,0,
        0,0,163,161,1,0,0,0,164,169,3,36,18,0,165,166,7,3,0,0,166,168,3,
        36,18,0,167,165,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,
        1,0,0,0,170,35,1,0,0,0,171,169,1,0,0,0,172,173,7,4,0,0,173,176,3,
        36,18,0,174,176,3,38,19,0,175,172,1,0,0,0,175,174,1,0,0,0,176,37,
        1,0,0,0,177,182,5,22,0,0,178,179,5,40,0,0,179,180,3,20,10,0,180,
        181,5,41,0,0,181,183,1,0,0,0,182,178,1,0,0,0,182,183,1,0,0,0,183,
        192,1,0,0,0,184,192,3,44,22,0,185,186,5,38,0,0,186,187,3,20,10,0,
        187,188,5,39,0,0,188,192,1,0,0,0,189,192,3,42,21,0,190,192,3,40,
        20,0,191,177,1,0,0,0,191,184,1,0,0,0,191,185,1,0,0,0,191,189,1,0,
        0,0,191,190,1,0,0,0,192,39,1,0,0,0,193,202,5,40,0,0,194,199,3,20,
        10,0,195,196,5,42,0,0,196,198,3,20,10,0,197,195,1,0,0,0,198,201,
        1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,199,
        1,0,0,0,202,194,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,
        5,41,0,0,205,41,1,0,0,0,206,207,5,22,0,0,207,216,5,38,0,0,208,213,
        3,20,10,0,209,210,5,42,0,0,210,212,3,20,10,0,211,209,1,0,0,0,212,
        215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,217,1,0,0,0,215,
        213,1,0,0,0,216,208,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,
        219,5,39,0,0,219,43,1,0,0,0,220,221,7,5,0,0,221,45,1,0,0,0,222,223,
        7,6,0,0,223,47,1,0,0,0,19,51,61,67,83,98,122,129,137,145,153,161,
        169,175,182,191,199,202,213,216
    ]

class SLangParser ( Parser ):

    grammarFileName = "SLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "':'", "<INVALID>", "<INVALID>", 
                     "'var'", "'print'", "'if'", "'else'", "'while'", "'for'", 
                     "'in'", "'true'", "'false'", "'int'", "'float'", "'boolean'", 
                     "'string'", "'array'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
                     "'||'", "'!'", "'('", "')'", "'['", "']'", "','", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "COMMENT", 
                      "VAR", "PRINT", "IF", "ELSE", "WHILE", "FOR", "IN", 
                      "TRUE", "FALSE", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "ARRAY", "INTEGER", "FLOATING_POINT", "STRING_LITERAL", 
                      "IDENTIFIER", "ASSIGN", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "AND", "OR", 
                      "NOT", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "COMMA", "SEMI", "LBRACE", "RBRACE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_variableDeclaration = 3
    RULE_assignmentStatement = 4
    RULE_printStatement = 5
    RULE_ifStatement = 6
    RULE_whileStatement = 7
    RULE_forLoop = 8
    RULE_expressionStatement = 9
    RULE_expression = 10
    RULE_conditionalExpression = 11
    RULE_logicalOrExpression = 12
    RULE_logicalAndExpression = 13
    RULE_equalityExpression = 14
    RULE_relationalExpression = 15
    RULE_additiveExpression = 16
    RULE_multiplicativeExpression = 17
    RULE_unaryExpression = 18
    RULE_primaryExpression = 19
    RULE_arrayLiteral = 20
    RULE_functionCall = 21
    RULE_literal = 22
    RULE_typeType = 23

    ruleNames =  [ "program", "statement", "block", "variableDeclaration", 
                   "assignmentStatement", "printStatement", "ifStatement", 
                   "whileStatement", "forLoop", "expressionStatement", "expression", 
                   "conditionalExpression", "logicalOrExpression", "logicalAndExpression", 
                   "equalityExpression", "relationalExpression", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "primaryExpression", 
                   "arrayLiteral", "functionCall", "literal", "typeType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    COMMENT=4
    VAR=5
    PRINT=6
    IF=7
    ELSE=8
    WHILE=9
    FOR=10
    IN=11
    TRUE=12
    FALSE=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    STRING=17
    ARRAY=18
    INTEGER=19
    FLOATING_POINT=20
    STRING_LITERAL=21
    IDENTIFIER=22
    ASSIGN=23
    PLUS=24
    MINUS=25
    MULT=26
    DIV=27
    MOD=28
    EQUAL=29
    NOT_EQUAL=30
    LESS_THAN=31
    LESS_THAN_OR_EQUAL=32
    GREATER_THAN=33
    GREATER_THAN_OR_EQUAL=34
    AND=35
    OR=36
    NOT=37
    LPAREN=38
    RPAREN=39
    LBRACKET=40
    RBRACKET=41
    COMMA=42
    SEMI=43
    LBRACE=44
    RBRACE=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.statement()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1511886697696) != 0)):
                    break

            self.state = 53
            self.match(SLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(SLangParser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(SLangParser.AssignmentStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(SLangParser.PrintStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SLangParser.IfStatementContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(SLangParser.ForLoopContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(SLangParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.printStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.forLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.expressionStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SLangParser.LBRACE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1511886697696) != 0):
                self.state = 64
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(SLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SLangParser.VAR, 0)

        def typeType(self):
            return self.getTypedRuleContext(SLangParser.TypeTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(SLangParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(SLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = SLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SLangParser.VAR)
            self.state = 73
            self.typeType()
            self.state = 74
            self.match(SLangParser.IDENTIFIER)
            self.state = 75
            self.match(SLangParser.ASSIGN)
            self.state = 76
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SLangParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(SLangParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.ExpressionContext,i)


        def LBRACKET(self):
            return self.getToken(SLangParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(SLangParser.RBRACKET, 0)

        def getRuleIndex(self):
            return SLangParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = SLangParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignmentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SLangParser.IDENTIFIER)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 79
                self.match(SLangParser.LBRACKET)
                self.state = 80
                self.expression()
                self.state = 81
                self.match(SLangParser.RBRACKET)


            self.state = 85
            self.match(SLangParser.ASSIGN)
            self.state = 86
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(SLangParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = SLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(SLangParser.PRINT)
            self.state = 89
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SLangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(SLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(SLangParser.ELSE, 0)

        def getRuleIndex(self):
            return SLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SLangParser.IF)
            self.state = 92
            self.match(SLangParser.LPAREN)
            self.state = 93
            self.expression()
            self.state = 94
            self.match(SLangParser.RPAREN)
            self.state = 95
            self.block()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 96
                self.match(SLangParser.ELSE)
                self.state = 97
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(SLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SLangParser.WHILE)
            self.state = 101
            self.match(SLangParser.LPAREN)
            self.state = 102
            self.expression()
            self.state = 103
            self.match(SLangParser.RPAREN)
            self.state = 104
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SLangParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(SLangParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(SLangParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(SLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = SLangParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SLangParser.FOR)
            self.state = 107
            self.match(SLangParser.IDENTIFIER)
            self.state = 108
            self.match(SLangParser.IN)
            self.state = 109
            self.expression()
            self.state = 110
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = SLangParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(SLangParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.conditionalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(SLangParser.LogicalOrExpressionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SLangParser.RULE_conditionalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpression" ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpression" ):
                listener.exitConditionalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalExpression" ):
                return visitor.visitConditionalExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpression(self):

        localctx = SLangParser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_conditionalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.logicalOrExpression()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 117
                self.match(SLangParser.T__0)
                self.state = 118
                self.expression()
                self.state = 119
                self.match(SLangParser.T__1)
                self.state = 120
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.OR)
            else:
                return self.getToken(SLangParser.OR, i)

        def getRuleIndex(self):
            return SLangParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = SLangParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.logicalAndExpression()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 125
                self.match(SLangParser.OR)
                self.state = 126
                self.logicalAndExpression()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.AND)
            else:
                return self.getToken(SLangParser.AND, i)

        def getRuleIndex(self):
            return SLangParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = SLangParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.equalityExpression()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 133
                self.match(SLangParser.AND)
                self.state = 134
                self.equalityExpression()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.RelationalExpressionContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.EQUAL)
            else:
                return self.getToken(SLangParser.EQUAL, i)

        def NOT_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.NOT_EQUAL)
            else:
                return self.getToken(SLangParser.NOT_EQUAL, i)

        def getRuleIndex(self):
            return SLangParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = SLangParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.relationalExpression()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self.relationalExpression()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.AdditiveExpressionContext,i)


        def LESS_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.LESS_THAN)
            else:
                return self.getToken(SLangParser.LESS_THAN, i)

        def LESS_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.LESS_THAN_OR_EQUAL)
            else:
                return self.getToken(SLangParser.LESS_THAN_OR_EQUAL, i)

        def GREATER_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.GREATER_THAN)
            else:
                return self.getToken(SLangParser.GREATER_THAN, i)

        def GREATER_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.GREATER_THAN_OR_EQUAL)
            else:
                return self.getToken(SLangParser.GREATER_THAN_OR_EQUAL, i)

        def getRuleIndex(self):
            return SLangParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = SLangParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.additiveExpression()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0):
                self.state = 149
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.additiveExpression()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.PLUS)
            else:
                return self.getToken(SLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.MINUS)
            else:
                return self.getToken(SLangParser.MINUS, i)

        def getRuleIndex(self):
            return SLangParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = SLangParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.multiplicativeExpression()
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 158
                    self.multiplicativeExpression() 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.UnaryExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.MULT)
            else:
                return self.getToken(SLangParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.DIV)
            else:
                return self.getToken(SLangParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.MOD)
            else:
                return self.getToken(SLangParser.MOD, i)

        def getRuleIndex(self):
            return SLangParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = SLangParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.unaryExpression()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 165
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.unaryExpression()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(SLangParser.UnaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(SLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SLangParser.MINUS, 0)

        def NOT(self):
            return self.getToken(SLangParser.NOT, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(SLangParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = SLangParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137489285120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.unaryExpression()
                pass
            elif token in [12, 13, 19, 20, 21, 22, 38, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SLangParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(SLangParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(SLangParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(SLangParser.RBRACKET, 0)

        def literal(self):
            return self.getTypedRuleContext(SLangParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(SLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SLangParser.RPAREN, 0)

        def functionCall(self):
            return self.getTypedRuleContext(SLangParser.FunctionCallContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(SLangParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return SLangParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = SLangParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primaryExpression)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(SLangParser.IDENTIFIER)
                self.state = 182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 178
                    self.match(SLangParser.LBRACKET)
                    self.state = 179
                    self.expression()
                    self.state = 180
                    self.match(SLangParser.RBRACKET)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(SLangParser.LPAREN)
                self.state = 186
                self.expression()
                self.state = 187
                self.match(SLangParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.arrayLiteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(SLangParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(SLangParser.RBRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.COMMA)
            else:
                return self.getToken(SLangParser.COMMA, i)

        def getRuleIndex(self):
            return SLangParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = SLangParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(SLangParser.LBRACKET)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1511886696448) != 0):
                self.state = 194
                self.expression()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 195
                    self.match(SLangParser.COMMA)
                    self.state = 196
                    self.expression()
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 204
            self.match(SLangParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SLangParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(SLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SLangParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SLangParser.COMMA)
            else:
                return self.getToken(SLangParser.COMMA, i)

        def getRuleIndex(self):
            return SLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = SLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(SLangParser.IDENTIFIER)
            self.state = 207
            self.match(SLangParser.LPAREN)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1511886696448) != 0):
                self.state = 208
                self.expression()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 209
                    self.match(SLangParser.COMMA)
                    self.state = 210
                    self.expression()
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 218
            self.match(SLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(SLangParser.INTEGER, 0)

        def FLOATING_POINT(self):
            return self.getToken(SLangParser.FLOATING_POINT, 0)

        def STRING_LITERAL(self):
            return self.getToken(SLangParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(SLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SLangParser.FALSE, 0)

        def getRuleIndex(self):
            return SLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3682304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SLangParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(SLangParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(SLangParser.STRING, 0)

        def ARRAY(self):
            return self.getToken(SLangParser.ARRAY, 0)

        def getRuleIndex(self):
            return SLangParser.RULE_typeType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeType" ):
                listener.enterTypeType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeType" ):
                listener.exitTypeType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeType" ):
                return visitor.visitTypeType(self)
            else:
                return visitor.visitChildren(self)




    def typeType(self):

        localctx = SLangParser.TypeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typeType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





