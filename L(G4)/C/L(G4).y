%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *s) { /* silencioso */ }
%}

%start input

%%

/* Varias líneas */
input
    : /* vacío */
    | input line
    ;

/* Cada línea: o coincide con una forma válida, o marca NO acepta y continúa */
line
    : 'a' 'b' '\n'         { puts("acepta"); }   /* ab */
    | 'a' 'b' 'b' '\n'     { puts("acepta"); }   /* abb */
    | '\n'                 { /* línea vacía: no imprime */ }
    | error '\n'           { yyerrok; puts("NO acepta"); }  /* consume hasta fin de línea */
    ;

%%

int main(void) {
    return yyparse();
}
