import sys

def es_g5(s: str) -> bool:
    L = len(s)
    if L < 2:
        return False  # Debe tener al menos "ab"

    if s[0] not in ('a', '0'):
        return False  # El primero debe ser a/0
    if s[-1] not in ('b', '1'):
        return False  # El último debe ser b/1

    i = 1
    while i < L - 1:
        if not ((s[i] in ('a', '0')) and (s[i + 1] in ('b', '1'))):
            return False
        i += 2

    return i == L - 1

def main():
    if len(sys.argv) != 2:
        print("Agregue un archivo")
        return
    nombre_archivo = sys.argv[1]
    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                print(f"{'Acepta' if es_g5(cadena) else 'No acepta'}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
if __name__ == "__main__":
    main()
