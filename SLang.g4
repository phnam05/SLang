grammar SLang;

/*
 * Lexer Rules
 */

// Whitespace
WS:             [ \t\r\n]+ -> skip;

// Comments
COMMENT:        '//' .*? '\n' -> skip;

// Keywords
VAR:            'var' | 'yo' | 'ayo';
PRINT:          'print' | 'holla' | 'spit' | 'yap';
IF:             'if' | 'when';
ELSE:           'else';
WHILE:          'while' ;
FOR:            'for' | 'those';
IN:             'in';
TRUE:           'true' | 'fr' | 'legit';
FALSE:          'false' | 'nah';
BREAK:          'break' | 'bruh';

// Data Types
INT:            'int';
FLOAT:          'float';
BOOLEAN:        'boolean';
STRING:         'string' ;
ARRAY:          'array' | 'gang';

// Literals
INTEGER:        [0-9]+;
FLOATING_POINT: [0-9]+ '.' [0-9]+;
STRING_LITERAL: '"' .*? '"';



// Operators
ASSIGN:         '=' | 'be';
PLUS:           '+';
MINUS:          '-';
MULT:           '*';
DIV:            '/';
MOD:            '%';
EQUAL:          '==' | 'is';
NOT_EQUAL:      '!=' | 'aint';
LESS_THAN:      '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN:   '>';
GREATER_THAN_OR_EQUAL: '>=';
AND:            '&&' | 'and';
OR:             '||' | 'or';
NOT:            '!' | 'not';

// Delimiters
LPAREN:         '(';
RPAREN:         ')';
LBRACKET:       '[';
RBRACKET:       ']';
COMMA:          ',';
SEMI:           ';';
LBRACE: '{';
RBRACE: '}';


/*
 * Parser Rules
 */

program: statement+ EOF;

statement:
      variableDeclaration
    | assignmentStatement
    | printStatement
    | ifStatement
    | forLoop
    | whileStatement
    | breakStatement
    | expressionStatement
    // Add a block statement to handle compound statements
    ;

block
    : LBRACE statement* RBRACE
    ;

// Break statement
breakStatement:
    BREAK
    ;

// Variable declaration
variableDeclaration:
    typeType IDENTIFIER ASSIGN expression
    ;

// Assignment statement (support for arrays with index)
assignmentStatement:
    IDENTIFIER ('[' expression ']')? ASSIGN expression
    ;

// Print statement
printStatement:
    PRINT expression (',' expression)*
    ;

// If statement
ifStatement:
    IF LPAREN expression RPAREN block (ELSE block)?
    ;

whileStatement
    : WHILE LPAREN expression RPAREN block
    ;

// For loop (over array only for now)
forLoop:
    FOR IDENTIFIER IN expression block
    ;

// Expression statement (e.g., just an expression by itself)
expressionStatement:
    expression
    ;

// Expressions
expression:
    conditionalExpression
    ;

conditionalExpression:
    logicalOrExpression ('?' expression ':' expression)?
    ;

logicalOrExpression:
    logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression:
    equalityExpression (AND equalityExpression)*
    ;

equalityExpression:
    relationalExpression ((EQUAL | NOT_EQUAL) relationalExpression)*
    ;

relationalExpression:
    additiveExpression ((LESS_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN | GREATER_THAN_OR_EQUAL) additiveExpression)*
    ;

additiveExpression:
    multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression:
    unaryExpression ((MULT | DIV | MOD) unaryExpression)*
    ;

unaryExpression:
    (PLUS | MINUS | NOT) unaryExpression
    | primaryExpression
    ;

primaryExpression:
      IDENTIFIER ('[' expression ']')?
    | literal
    | LPAREN expression RPAREN
    | functionCall
    | arrayLiteral
    ;

arrayLiteral:
    LBRACKET (expression (COMMA expression)*)? RBRACKET
    ;

functionCall:
    IDENTIFIER LPAREN (expression (COMMA expression)*)? RPAREN
    ;

// Literals
literal:
      INTEGER
    | FLOATING_POINT
    | STRING_LITERAL
    | TRUE
    | FALSE
    ;

// Data types
typeType:
      INT
    | FLOAT
    | BOOLEAN
    | STRING
    | ARRAY
    ;
// Identifiers
IDENTIFIER:     [a-zA-Z_][a-zA-Z_0-9]*;