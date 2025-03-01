grammar analizador;

// Tokens
FOR      : 'for';
WHILE    : 'while';
IF       : 'if';
ELSE     : 'else';
PRINT    : 'mostrar';
SEMICOL  : ';';
LPAREN   : '(';
RPAREN   : ')';
LBRACE   : '{';
RBRACE   : '}';
ASSIGN   : '=';
COMMA    : ',';
MUL      : '*';
DIV      : '/';
MOD      : '%';   
ADD      : '+';
SUB      : '-';
LT       : '<';
GT       : '>';
LEQ      : '<=';
GEQ      : '>=';
EQ       : '==';
NEQ      : '!=';
NUM      : [0-9]+;
ID       : [a-zA-Z_][a-zA-Z0-9_]*;
STRING   : '"' (~["])* '"';
WS       : [ \t\r\n]+ -> skip;
COMMENT  : '#' ~[\r\n]* -> skip ;



programa : (asignacion SEMICOL | suma SEMICOL | forLoop | whileLoop | ifElse | accion SEMICOL)*;

whileLoop : WHILE LPAREN condicion RPAREN LBRACE bloque RBRACE;

ifElse  : IF LPAREN condicion RPAREN LBRACE bloque RBRACE (ELSE LBRACE bloque RBRACE)?;

accion  : PRINT LPAREN (STRING | expresion) (COMMA (STRING | expresion))* RPAREN;

forLoop  : FOR LPAREN asignacion SEMICOL condicion SEMICOL asignacion RPAREN LBRACE bloque RBRACE;

asignacion : ID ASSIGN expresion;  

condicion : expresion (LT | GT | LEQ | GEQ | EQ | NEQ) expresion;

suma : ID ASSIGN expresion ADD expresion;

expresion
    : LPAREN expresion RPAREN
    | expresion MUL expresion  
    | expresion DIV expresion
    | expresion MOD expresion 
    | expresion ADD expresion     
    | expresion SUB expresion                     
    | ID
    | NUM;

bloque : (asignacion SEMICOL | suma SEMICOL | forLoop | whileLoop | ifElse | accion SEMICOL)*;
