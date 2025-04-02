grammar analizador;

// PALABRAS RESERVADAS
PARA      : 'para';
MIENTRAS  : 'mientras';
SI        : 'si';
SINO      : 'sino';
MOSTRAR   : 'mostrar';

// SÍMBOLOS
PYC       : ';';
PARI      : '(';
PARD      : ')';
LLAVEI    : '{';
LLAVED    : '}';
ASIGNAR   : '=';
COMA      : ',';

// OPERADORES
MULT      : '*';
DIV       : '/';
MOD       : '%';   
SUMA      : '+';
RESTA     : '-';
MENOR     : '<';
MAYOR     : '>';
MENORIGUAL : '<=';
MAYORIGUAL : '>=';
IGUAL     : '==';
DIFERENTE : '!=';

// TIPOS DE DATO
NUMERO    : [0-9]+;
ID        : [a-zA-Z_][a-zA-Z0-9_]*;
TEXTO     : '"' (~["])* '"';

// IGNORAR ESPACIOS Y COMENTARIOS
ESPACIO   : [ \t\r\n]+ -> skip;
COMENTARIO: '#' ~[\r\n]* -> skip;

// REGLAS DE PRODUCCIÓN
programa  : (asignacion PYC | operacion PYC | cicloPara | cicloMientras | condicional | accion PYC)*;

cicloMientras : MIENTRAS PARI condicion PARD LLAVEI bloque LLAVED;

condicional : SI PARI condicion PARD LLAVEI bloque LLAVED (SINO LLAVEI bloque LLAVED)?;

accion : MOSTRAR PARI (TEXTO | expresion) (COMA (TEXTO | expresion))* PARD;

cicloPara : PARA PARI asignacion PYC condicion PYC asignacion PARD LLAVEI bloque LLAVED;

asignacion : ID ASIGNAR expresion;  

condicion : expresion (MENOR | MAYOR | MENORIGUAL | MAYORIGUAL | IGUAL | DIFERENTE) expresion;

operacion : ID ASIGNAR expresion SUMA expresion;

expresion
    : PARI expresion PARD
    | expresion MULT expresion  
    | expresion DIV expresion
    | expresion MOD expresion 
    | expresion SUMA expresion     
    | expresion RESTA expresion                     
    | ID
    | NUMERO;

bloque : (asignacion PYC | operacion PYC | cicloPara | cicloMientras | condicional | accion PYC)*;
>>>>>>> main
