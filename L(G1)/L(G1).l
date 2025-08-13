%{
#include "g1.tab.h"
#include <string.h>

char buffer[1024];
%}

%%
[01]+   { strcpy(buffer, yytext); return CADENA; }
\n      { return '\n'; }
[ \t\r] { /* ignorar */ }
.       { /* ignorar otros caracteres */ }
%%

int yywrap(void) {
    return 1;
}

