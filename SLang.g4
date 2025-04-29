    grammar SLang;

    /*
     * Lexer Rules
     */

    // Whitespace
    WS:             [ \t\r\n]+ -> skip;

    // Comments
    COMMENT:        '//' .*? '\n' -> skip;

    // Keywords
    VAR:            'var';
    PRINT:          'print';
    IF:             'if';
    ELSE:           'else';
    WHILE:          'while';
    FOR:            'for';
    IN:             'in';
    TRUE:           'true';
    FALSE:          'false';

    // Data Types
    INT:            'int';
    FLOAT:          'float';
    BOOLEAN:        'boolean';
    STRING:         'string';
    ARRAY:          'array';

    // Literals
    INTEGER:        [0-9]+;
    FLOATING_POINT: [0-9]+ '.' [0-9]+;
    STRING_LITERAL: '"' .*? '"';

    // Identifiers
    IDENTIFIER:     [a-zA-Z_][a-zA-Z_0-9]*;

    // Operators
    ASSIGN:         '=';
    PLUS:           '+';
    MINUS:          '-';
    MULT:           '*';
    DIV:            '/';
    MOD:            '%';
    EQUAL:          '==';
    NOT_EQUAL:      '!=';
    LESS_THAN:      '<';
    LESS_THAN_OR_EQUAL: '<=';
    GREATER_THAN:   '>';
    GREATER_THAN_OR_EQUAL: '>=';
    AND:            '&&';
    OR:             '||';
    NOT:            '!';

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
        | whileStatement
        | ifStatement
        | forLoop
        | expressionStatement
        // Add a block statement to handle compound statements
        ;
    block
        : LBRACE statement* RBRACE
        ;


    // Variable declaration
    variableDeclaration:
        VAR typeType IDENTIFIER ASSIGN expression
        ;

    // Assignment statement (support for arrays with index)
    assignmentStatement:
        IDENTIFIER ('[' expression ']')? ASSIGN expression
        ;

    // Print statement
    printStatement:
        PRINT expression
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