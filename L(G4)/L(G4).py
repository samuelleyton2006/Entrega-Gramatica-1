import sys

def es_g4(s: str) -> bool:
    return (len(s) == 2 and s[0] in ('a', '0') and s[1] in ('b', '1')) or \
           (len(s) == 3 and s[0] in ('a', '0') and s[1] in ('b', '1') and s[2] in ('b', '1'))
def main():
    if len(sys.argv) != 2:
        print("Agregue un archivo")
        return
    nombre_archivo = sys.argv[1]
    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                print(f"{'Acepta' if es_g4(cadena) else 'No acepta'}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
if __name__ == "__main__":
    main()
