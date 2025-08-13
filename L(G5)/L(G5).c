#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int es_g5(const char *s) {
    size_t len = strlen(s);
    if (len < 2) return 0; // Debe tener al menos "ab"

    if (!(s[0] == 'a' || s[0] == '0')) return 0; 
    if (!(s[len - 1] == 'b' || s[len - 1] == '1')) return 0; 

    int i = 1;
    while (i < (int)len - 1) {
        if (!((s[i] == 'a' || s[i] == '0') && (s[i + 1] == 'b' || s[i + 1] == '1'))) return 0;
        i += 2;
    }

    return (i == (int)len - 1);
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

        if (es_g5(linea)) {
            printf("Acepta\n");
        } else {
            printf("No acepta\n");
        }
    }

    fclose(archivo);
    return 0;
}
