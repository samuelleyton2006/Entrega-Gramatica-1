#include <stdio.h>
#include <string.h>
#include <stdbool.h>  


bool es_g2(const char *s) {
    int i = 0;
    int n = 0;
    int len = strlen(s);

    // Contar la cantidad de a o 0
    while (i < len && (s[i] == 'a' || s[i] == '0')) {
        i++;
        n++;  // Incrementar el contador de 'a' o '0'
    }

    // verificar que los caracteres restantes sean 'b' o '1'
    for (int j = i; j < len; j++) {
        if (s[j] != 'b' && s[j] != '1') {
            return false; 
        }
    }

    
    return (len - i) == n + 1;
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

        if (es_g2(linea)) {
            printf("Acepta\n");
        } else {
            printf("No acepta\n");
        }
    }

    fclose(archivo);
    return 0;
}
