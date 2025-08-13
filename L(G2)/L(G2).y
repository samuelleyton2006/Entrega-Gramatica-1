%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *s) { /* vacío para no duplicar mensajes */ }
%}

%start input
%token XERR

%%

input
    : /* vacío */
    | input line
    ;

line
    : S '\n'           { puts("acepta"); }
    | '\n'             { /* línea vacía, sin mensaje */ }
    | error '\n'       { yyerrok; puts("NO acepta"); }
    ;

S  : A 'b'
   ;

A  : /* vacío */
   | 'a' A 'b'
   | 'x' { YYERROR; } /* token inválido provoca error inmediato */
   ;

%%

int main(void) {
    yyparse();
    return 0;
}
