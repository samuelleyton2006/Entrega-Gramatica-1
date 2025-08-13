/* g5.y */
%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex(void);
extern void *yy_scan_string(const char *);
extern void yy_delete_buffer(void *);

void yyerror(const char *s) {
    /* suprimimos impresión de errores para que la salida sea sólo "acepta"/"NO acepta" */
    (void)s;
}
%}

%start S

%%

S: A 'b' ;
A: 'a'
 | A 'a' 'b'
 ;

%%

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("fopen"); return 1; }

    char line[8192];
    while (fgets(line, sizeof(line), f)) {
        /* preparar el buffer del scanner con la línea actual */
        void *buf = yy_scan_string(line);
        int res = yyparse(); /* 0 = success, !=0 = error */
        if (res == 0) printf("acepta\n");
        else printf("NO acepta\n");
        yy_delete_buffer(buf);
    }

    fclose(f);
    return 0;
}
