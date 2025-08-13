#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int es_g4(const char *s) {
    if (strlen(s) == 2 && (s[0] == 'a' || s[0] == '0') && (s[1] == 'b' || s[1] == '1')) return 1;
    if (strlen(s) == 3 && (s[0] == 'a' || s[0] == '0') && (s[1] == 'b' || s[1] == '1') && (s[2] == 'b' || s[2] == '1')) return 1;
    return 0;
}
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Porfavor agregue un archivo");
        return 1; 
    }

    char *nombre_archivo = argv[1];
    FILE *archivo = fopen(nombre_archivo, "r");

    if (archivo == NULL) {
        perror("Error al abrir el archivo"); 
        return 1; 
    }

    char linea[256]; 

    while (fgets(linea, sizeof(linea), archivo) != NULL) {

        linea[strcspn(linea, "\n")] = 0;  

        if (es_g4(linea)) {
            printf("Acepta\n");
        } else {
            printf("No acepta\n");
        }
    }

    fclose(archivo);
    return 0;
}
