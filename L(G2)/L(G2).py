import sys
def es_g2(s):
    i = 0
    n = 0
    L = len(s)
    while i < L and s[i] == '0':
        i += 1
        n += 1
    restante = L - i
    if restante != n + 1:
        return False
    for ch in s[i:]:
        if ch != '1':  # '1' representa 'b'
            return False
    return True
def main():
    if len(sys.argv) != 2:
        print("Agregue un archivo")
        return
    nombre_archivo = sys.argv[1]
    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                print(f"{'Acepta' if es_g2(cadena) else 'No acepta'}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
if __name__ == "__main__":
    main()
