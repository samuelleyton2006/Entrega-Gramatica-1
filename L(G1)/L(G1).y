%{
#include <stdio.h>
#include <string.h>
extern FILE *yyin;
extern char buffer[1024];

int yylex(void);
void yyerror(const char *s);

int es_palindromo(const char *s) {
    int i = 0, j = strlen(s) - 1;
    while (i < j) {
        if (s[i] != s[j]) return 0;
        i++; j--;
    }
    return 1;
}
%}

%token CADENA

%%

input:
    /* vacío */
  | input line
  ;

line:
    CADENA '\n' {
        if (es_palindromo(buffer))
            printf("acepta\n");
        else
            printf("NO acepta\n");
    }
  | '\n' { /* línea vacía */ }
  ;

%%

void yyerror(const char *s) {
    printf("NO acepta\n");
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }
    yyin = fopen(argv[1], "r");
    if (!yyin) {
        perror("fopen");
        return 1;
    }
    yyparse();
    fclose(yyin);
    return 0;
}

