%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *s) { /* sin mensajes extra */ }
%}

%start input

%%

input
    : /* vacío */
    | input line
    ;

line
    : S '\n'           { puts("acepta"); }
    | '\n'             { /* línea vacía */ }
    | error '\n'       { yyerrok; puts("NO acepta"); }
    ;

/* G3: S → A b  */
S  : A 'b'
   ;

/* G3: A → a A b | a b  */
A  : 'a' A 'b'
   | 'a' 'b'
   | 'x' { YYERROR; }  /* carácter inválido → error inmediato */
   ;

%%

int main(void) {
    yyparse();
    return 0;
}
