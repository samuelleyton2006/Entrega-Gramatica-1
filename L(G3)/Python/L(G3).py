import sys
import re

def parse_A(cadena, pos):
    if pos < len(cadena) and cadena[pos] == 'a':
        pos += 1
        
        new_pos, ok = parse_A(cadena, pos)
        if ok and new_pos < len(cadena) and cadena[new_pos] == 'b':
            return new_pos + 1, True
        
        elif pos < len(cadena) and cadena[pos] == 'b':
            return pos + 1, True
    return pos, False


def parse_S(cadena):
    pos, ok = parse_A(cadena, 0)
    if ok and pos < len(cadena) and cadena[pos] == 'b':
        pos += 1
        if pos == len(cadena):
            return True
    return False

def procesar_archivo(ruta):
    patron = re.compile(r"[ab]+")  
    try:
        with open(ruta, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:  
                    continue
                if not patron.fullmatch(linea):
                    print("NO acepta")  
                    continue
                if parse_S(linea):
                    print("acepta")
                else:
                    print("NO acepta")
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} archivo.txt")
        sys.exit(1)
    procesar_archivo(sys.argv[1])
