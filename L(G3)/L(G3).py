import sys
def es_g3(s: str) -> bool:
    i = 0
    n = 0
    L = len(s)

    while i < L and s[i] in ('a', '0'):
        i += 1
        n += 1

    if any(ch not in ('b', '1') for ch in s[i:]):
        return False

    return (L - i) == n + 1
def main():
    if len(sys.argv) != 2:
        print("Agregue un archivo")
        return
    nombre_archivo = sys.argv[1]
    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                print(f"{'Acepta' if es_g3(cadena) else 'No acepta'}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
if __name__ == "__main__":
    main()
