import numpy as np
def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_")
    return tablero

def disparar(casilla, tablero):
    fila, columna = casilla
    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
    elif tablero[fila, columna] == "_":
        tablero[fila, columna] = "A"
    return tablero
def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla]="O"
    return tablero
def crear_barco_eslora_2(eslora):
    barco = []
    pos_ini = (np.random.randint(10), np.random.randint(10))
    barco.append(pos_ini)
    direccion = np.random.choice(("V", "H"))
    p = 1

    if direccion == "V":
        for pos in range(eslora -1):
            barco.append((pos_ini[0] + p, pos_ini[1]))
            p = p + 1
    else:
        for pos in range(eslora -1):
            barco.append((pos_ini[0], pos_ini[1] + p))
            p = p + 1
    return barco
def crear_flota():
    esloras_flota = [4, 3, 3, 2, 2, 2]
    flota = []
    for eslora in esloras_flota:
        flota.append(crear_barco_eslora_2(eslora))
    for barco in flota:
        for coor in barco:
            for i in coor:
                if i < 0 or i > 9:
                    return crear_flota()
    ocupadas = []
    for barco in flota:
        for coor in barco:
            if coor in ocupadas:
                print("solapamiento, generando flota de nuevo...")
                return crear_flota()
            
            ocupadas.append(coor)
    print("Flota creada")
    return flota
def colocar_barcos(tablero):
    flota = crear_flota()
    for barco in flota:
        colocar_barco(barco, tablero)
    return tablero

