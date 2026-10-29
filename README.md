# Hundir la flota

Juego de Hundir la flota en Python contra la máquina, ejecutable desde terminal.

## Cómo jugar

    git clone <URL del repositorio>
    cd Hundir-la-flota
    py main.py

Introduce la fila y la columna (0-9) del disparo. La máquina dispara al azar.
Gana quien hunda primero todos los barcos del rival.

## Símbolos

- `_` mar
- `O` barco
- `X` tocado
- `A` agua

## Estructura

- `main.py`: flujo de la partida
- `funciones.py`: funciones del juego (tableros, barcos, disparos y turnos)

## Requisitos

Python 3 y NumPy.
