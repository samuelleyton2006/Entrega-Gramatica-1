import sys
import re

def es_palindromo(s: str) -> bool:
    return s == s[::-1]

def procesar_archivo(ruta):
    patron = re.compile(r"[01]+")  
    try:
        with open(ruta, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:  
                    continue
                
                match = patron.fullmatch(linea)
                if match:
                    cadena = match.group(0)
                    if es_palindromo(cadena):
                        print("acepta")
                    else:
                        print("NO acepta")
                else:
                    print("NO acepta")
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} archivo.txt")
        sys.exit(1)
    
    procesar_archivo(sys.argv[1])
