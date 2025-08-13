%{
#include "g4.tab.h"
%}

%%
[ \t]+           ;               /* ignorar espacios y tabs */
a                { return 'a'; }
b                { return 'b'; }
(\r)?\n          { return '\n'; } /* soporta \n y \r\n */
.                { return 'x'; }  /* cualquier otro char → inválido */
%%

int yywrap(void) { return 1; }
