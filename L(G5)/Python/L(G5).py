import sys
import re

def acepta(linea):
    linea = linea.strip()
    
    if not re.fullmatch(r"[ab]+", linea):
        return False
    
    if not linea or linea[0] != 'a' or linea[-1] != 'b':
        return False
    
    a_count = len(re.match(r"a+", linea).group(0)) if re.match(r"a+", linea) else 0
    b_count = len(re.match(r".*?b+$", linea).group(0).replace('a', '')) if re.match(r".*?b+$", linea) else 0
    
    return a_count == b_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} archivo.txt")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        for linea in f:
            if acepta(linea):
                print("acepta")
            else:
                print("NO acepta")
