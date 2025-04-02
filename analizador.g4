grammar analizador;

FOR      : 'for';
WHILE    : 'while';
IF       : 'if';
ELSE     : 'else';
PRINT    : 'mostrar';
RETURN   : 'return';

INT      : 'int';
FLOAT    : 'float';
BOOL     : 'bool';
STRING_T : 'string';

TRUE     : 'true';
FALSE    : 'false';

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

NUM      : [0-9]+ ('.' [0-9]+)?;
ID       : [a-zA-Z_][a-zA-Z0-9_]*;
STRING   : '"' (~["\r\n])* '"';

WS       : [ \t\r\n]+ -> skip;
COMMENT  : '#' ~[\r\n]* -> skip ;

// -------------------- REGLAS --------------------

programa 
    : (funcionDecl SEMICOL)* ID LBRACE (instruccion SEMICOL)* RBRACE EOF
    ;

instruccion 
    : declaracion
    | asignacion
    | suma
    | accion
    | returnStmt
    | forLoop
    | whileLoop
    | ifElse
    | funcionDecl
    ;

declaracion 
    : tipo ID (ASSIGN expresion)?
    ;

tipo 
    : INT | FLOAT | BOOL | STRING_T
    ;

asignacion 
    : ID ASSIGN expresion
    ;

suma 
    : ID ASSIGN expresion ADD expresion
    ;

accion 
    : PRINT LPAREN (STRING | expresion) (COMMA (STRING | expresion))* RPAREN
    ;

returnStmt 
    : RETURN expresion
    ;

funcionDecl 
    : tipo ID LPAREN parametros? RPAREN LBRACE bloque RBRACE
    ;

parametros 
    : parametro (COMMA parametro)*
    ;

parametro 
    : tipo ID
    ;

llamadaFuncion 
    : ID LPAREN argumentos? RPAREN
    ;

argumentos 
    : expresion (COMMA expresion)*
    ;


forLoop 
    : FOR LPAREN asignacion SEMICOL expresion SEMICOL asignacion RPAREN LBRACE bloque RBRACE
    ;


whileLoop 
    : WHILE LPAREN expresion RPAREN LBRACE bloque RBRACE
    ;

ifElse 
    : IF LPAREN expresion RPAREN LBRACE bloque RBRACE (ELSE LBRACE bloque RBRACE)?
    ;


bloque 
    : (instruccion SEMICOL)*
    ;


expresion
    : LPAREN expresion RPAREN
    | expresion MUL expresion
    | expresion DIV expresion
    | expresion MOD expresion
    | expresion ADD expresion
    | expresion SUB expresion
    | expresion LT expresion
    | expresion GT expresion
    | expresion LEQ expresion
    | expresion GEQ expresion
    | expresion EQ expresion
    | expresion NEQ expresion
    | llamadaFuncion
    | ID
    | NUM
    | TRUE
    | FALSE
    | STRING
    ;
