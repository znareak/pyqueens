
verde = '\033[92m'
reset = '\033[0m'
error = '\033[93m'

def rellenar(cantidad):
    tablero = []
    for i in range(0, cantidad):
        sub = []
        for i in range(0, cantidad):
            sub.append(0)
        tablero.append(sub)
    return tablero

def comprobar(tablero, x, y):
    longitud = len(tablero)
    rango = range(0, longitud)

    # comprobar fila
    for columna in rango:
        if tablero[x][columna] != 0:
            return False

    # comprobar filas
    for fila in rango:
        if tablero[fila][y] != 0:
            return False

    _x = x
    _y = y
    while _x >= 0 and _y >= 0:
        if tablero[_x][_y] != 0:
            return False
        _x -= 1
        _y -= 1

    _x = x
    _y = y
    while _x >= 0 and _y < longitud:
        if tablero[_x][_y] != 0:
            return False
        _x -= 1
        _y += 1

    return True  # es una buena casilla


def main():

    cantidad = int(input("Reinas: "))
    if cantidad == 2 or cantidad == 1:
        print(error + "[!] Para esta cantidad no existen soluciones" + reset)
        return

    if(cantidad < 1) :
        print(error + "[!] El numero debe ser >= 1" + reset)
        return
    print(f"Calculando para {cantidad}x{cantidad}...\n")
    tablero = rellenar(cantidad)
    colocadas = 0
    x = 0
    y = 0
    reinas = []

    while colocadas < cantidad:
        if y >= cantidad or x >= cantidad:
            (xAux, yAux) = reinas[-1]
            tablero[xAux][yAux] = 0
            x = xAux
            y = yAux + 1
            colocadas -= 1
            reinas.pop()

        elif comprobar(tablero, x, y):
            reinas.append((x, y))
            tablero[x][y] = 1
            colocadas += 1
            x += 1
            y = 0

        else:
            y += 1

    imprimirTablero(tablero)


def imprimitLetras(cantidad):
    tab = " " * 3
    letras = "a b c d e f g h".split(" ")
    print(tab, end="")
    for i in range(0, cantidad):
        print(letras[i] + " ", end="")
    print()
    print(tab + "_ " * cantidad)


def imprimirTablero(tablero):
    cantidad = len(tablero)
    rango = range(0, cantidad)
    imprimitLetras(cantidad)
    filaTablero = 1

    for fila in rango:
        print(str(filaTablero) + "| ", end="")
        for columna in rango:
            if tablero[fila][columna] != 0:
                print(verde + "Q " + reset, end='')
            else:
                print("# ", end='')
        print("\n")
        filaTablero += 1


if __name__ == '__main__':
    print("\nAlgoritmo de las 8 reinas usando backtracking")
    print("Coloque la cantidad de reinas: ")
    main()
