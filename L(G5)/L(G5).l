/* g5.l */
%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
%}

/* reglas */
%%
"a"      { return 'a'; }
"b"      { return 'b'; }
[ \t\r]+ { /* Ignorar espacios y tabs y CR */ }
\n       { return 0; }    /* tratamos newline como fin de la entrada para esa línea */
.        { /* cualquier otro carácter regresará su propio valor y causará error de parseo */ return yytext[0]; }
<<EOF>>  { return 0; }
%%
