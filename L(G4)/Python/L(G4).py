import sys
import re

def procesar_archivo(ruta):
    
    patron_ab = re.compile(r"^ab$")   
    patron_abb = re.compile(r"^abb$") 

    try:
        with open(ruta, 'r') as f:
            for linea in f:
                linea = linea.strip()  
                if not linea:  #
                    continue

                
                if patron_ab.fullmatch(linea) or patron_abb.fullmatch(linea):
                    print("acepta")
                else:
                    print("NO acepta")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} archivo.txt")
        sys.exit(1)

    procesar_archivo(sys.argv[1])
