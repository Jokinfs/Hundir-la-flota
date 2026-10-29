import funciones as f

t_barcos_jugador = f.crear_tablero()
t_disparo_jugador = f.crear_tablero()
t_barcos_rival = f.crear_tablero()
t_disparo_rival = f.crear_tablero()

f.colocar_barcos(t_barcos_jugador)
f.colocar_barcos(t_barcos_rival)

print("¡Bienvenido a Hundir la flota!")
f.pintar(t_barcos_jugador, t_disparo_jugador)

ganador = f.turnos(t_barcos_rival, t_disparo_rival, t_barcos_jugador, t_disparo_jugador)
print("Ha ganado:", ganador)