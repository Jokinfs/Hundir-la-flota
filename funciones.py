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

tablero = crear_tablero()
flota = crear_flota()
print("FLOTA: ")
print(flota)

for barco in flota:
    colocar_barco(barco, tablero)

print("TABLERO")
print(tablero)


def disparo(tablero_rival,tablero_disparos, fila, columna):
    if tablero_rival[fila, columna] == "O":
        tablero_rival[fila, columna]= "X"
        tablero_disparos[fila, columna] = "X"
        print("tocado")
        return True
    else:
        tablero_rival[fila, columna] = "A"
        tablero_disparos[fila, columna] = "A"
        print("agua")
        return False

def pintar(t_barcos_jugador, t_disparos_jugador):
    print("********** TUS BARCOS **********")
    print(t_barcos_jugador)
    print()
    print("********** TUS DISPAROS **********")
    print(t_disparos_jugador)
    print()

def turnos(t_barcos_rival, t_disparo_rival, t_barcos_jugador, t_disparo_jugador):
    ganador = ""
    turno_jugador = True
    while True:
        if turno_jugador == True:
            print("Turno jugador")
            while True:
                fila = int(input("Fila (0-9): "))
                col = int(input("Columna (0-9): "))
                if fila < 0 or fila > 9 or col < 0 or col > 9:
                    print("Fuera del tablero. Elige números entre 0 y 9")
                elif t_disparo_jugador[fila, col] != "_":
                    print("Ya has disparado ahí. Elige otra casilla")
                else:
                    break
            disparo(t_barcos_rival, t_disparo_jugador, fila, col)
            turno_jugador = False
            pintar(t_barcos_jugador, t_disparo_jugador)
        else:
            print("Turno rival")
            while True:
                fila = np.random.randint(10)
                col = np.random.randint(10)
                if t_disparo_rival[fila, col] == "_":
                    break
            disparo(t_barcos_jugador, t_disparo_rival, fila, col)
            turno_jugador = True
            pintar(t_barcos_jugador, t_disparo_jugador)

        if "O" not in t_barcos_rival:
            ganador = "jugador"
            break
        if "O" not in t_barcos_jugador:
            ganador = "rival"
            break
    return ganador


