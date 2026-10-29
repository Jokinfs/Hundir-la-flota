
import funciones as f

t_barcos_jugador = f.crear_tablero()
t_disparo_jugador = f.crear_tablero()
t_barcos_rival = f.crear_tablero()
t_disparo_rival = f.crear_tablero

flota_jugador = f.crear_flota
flota_rival = f.crear_flota


t_barcos_juagdor = f.colocar_barco(flota_jugador, t_barcos_jugador)
t_barcos_rival = f.colocar_barco(flota_rival, t_barcos_rival)


print("*****************TABLEROS************************")
print("JUGADOR")
print(t_barcos_rival)
print("RIVAL")
print(t_barcos_jugador)