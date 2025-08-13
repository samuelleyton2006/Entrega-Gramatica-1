%{
#include "g3.tab.h"
%}

%%
[ \t]+           ;               /* ignorar espacios y tabs */
a                { return 'a'; }
b                { return 'b'; }
(\r)?\n          { return '\n'; }
.                { return 'x'; } /* cualquier otro char → símbolo especial de error */
%%

int yywrap(void) { return 1; }
