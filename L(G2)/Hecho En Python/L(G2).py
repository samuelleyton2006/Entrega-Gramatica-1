import sys
import re

def acepta_cadena(cadena: str) -> bool:
    """
    Devuelve True si la cadena cumple la gramática:
      S -> A 'b'
      A -> ε | 'a' A 'b'
    Y no contiene 'x'.
    """
    # Rechazar si hay 'x'
    if 'x' in cadena:
        return False

    # Implementar la gramática de forma recursiva
    def parse_A(s):
        if not s:
            return ""  # A vacío
        if s.startswith('a') and s.endswith('b') and len(s) >= 2:
            return parse_A(s[1:-1])
        return None  # No cumple

    if not cadena:
        return False

    # S -> A 'b'
    if cadena.endswith('b'):
        resto = cadena[:-1]  # quitar la última 'b'
        return parse_A(resto) == ""
    return False

def procesar_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:  # línea vacía
                    continue
                if acepta_cadena(linea):
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
