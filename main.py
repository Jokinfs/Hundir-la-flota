
import funciones as f

t_barcos_jugador = f.crear_tablero()
t_barcos_rival = f.crear_tablero()

f.colocar_barcos(t_barcos_jugador)
f.colocar_barcos(t_barcos_rival)

print("JUGADOR")
print(t_barcos_jugador)
print("RIVAL")
print(t_barcos_rival)