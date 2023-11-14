import random

class Casilla:
    def __init__(self):
        self.espacio_disp = "   |"
        self.coordenada_x = 0
        self.coordenada_y = 0
        self.estado = 1

class Barco:
    def __init__(self, nombre, numero_casillas):
        self.casilla_inicial_x = 3
        self.casilla_inicial_y = 3
        self.posicion = 1
        self.numero_casillas = numero_casillas
        self.nombre = nombre
        self.area = []

class Jugador:
    def __init__(self):
        self.flota = []
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)]
        self.ataque = []

class Tiro:
    def __init__(self):
        self.coordenadas = Casilla()
        self.resultado = 0

class BatallaNaval:
    def __init__(self):
        self.jugador1 = Jugador()
        self.jugador2 = Jugador()
        self.turno_colocar_barcos = 1
        self.turno_disparo = 1
        self.barcos_por_jugador = 5
        self.barcos_pequenos = [Barco("pequenos", 3) for _ in range(self.barcos_por_jugador)]
        self.barcos_grandes = [Barco("grandes", 2) for _ in range(self.barcos_por_jugador)]
        self.barco_actual = 0

    def mostrar_turno_colocar_barcos(self):
        print(f"\nJugador {self.turno_colocar_barcos}, coloca tus barcos:")

    def mostrar_turno_disparo(self):
        print(f"\nJugador {self.turno_disparo}, es tu turno de disparar.")

    def imprimir_tablero(self, jugador, mostrar_barcos=False):
        nombre_jugador = "Jugador 1" if jugador == self.jugador1 else "Jugador 2"
        tablero = [[' ' if c == 'X' or (mostrar_barcos and c == 'O') else c for c in fila] for fila in jugador.tablero]
        print(f"\nTablero de {nombre_jugador}")
        print("   1 2 3 4 5 6 7 8 9 10")
        for i, fila in enumerate(tablero):
            fila_str = chr(ord('A') + i) + ' |' + '|'.join(fila) + '|'
            print(fila_str)

    def colocar_barco(self, jugador, barco_actual):
        tablero = jugador.tablero

        while True:
            try:
                posicion = input(f"Ingrese la posición del barco {barco_actual.nombre} (por ejemplo, B5): ")
                fila, columna = ord(posicion[0].upper()) - ord('A'), int(posicion[1:]) - 1
                orientacion = input("Ingrese la orientación del barco (H para horizontal, V para vertical): ").upper()

                if orientacion == 'H' and columna + barco_actual.numero_casillas <= 10:
                    for i in range(barco_actual.numero_casillas):
                        if tablero[fila][columna + i] == ' ':
                            barco_actual.area.append((fila, columna + i))
                            tablero[fila][columna + i] = 'X'
                        else:
                            raise ValueError
                elif orientacion == 'V' and fila + barco_actual.numero_casillas <= 10:
                    for i in range(barco_actual.numero_casillas):
                        if tablero[fila + i][columna] == ' ':
                            barco_actual.area.append((fila + i, columna))
                            tablero[fila + i][columna] = 'X'
                        else:
                            raise ValueError
                else:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print("Posición no válida. Inténtelo de nuevo.")
        jugador.flota.append(barco_actual)

    def colocar_barcos_manualmente(self):
        self.mostrar_turno_colocar_barcos()
        barcos_actuales = self.barcos_pequenos if self.barco_actual < self.barcos_por_jugador else self.barcos_grandes
        jugador_actual = self.jugador1 if self.turno_colocar_barcos == 1 else self.jugador2

        for barco in barcos_actuales:
            self.imprimir_tablero(jugador_actual)
            self.colocar_barco(jugador_actual, barco)

        self.barco_actual += 1
        if self.barco_actual == self.barcos_por_jugador * 2:
            self.turno_colocar_barcos = 3  # Ambos jugadores han colocado sus barcos

    def disparar(self, jugador, oponente):
        self.mostrar_turno_disparo()
        while True:
            self.imprimir_tablero(jugador, mostrar_barcos=True)
            try:
                disparo = input("Ingrese la posición del disparo (por ejemplo, B5): ")
                fila, columna = ord(disparo[0].upper()) - ord('A'), int(disparo[1:]) - 1

                if oponente.tablero[fila][columna] == 'X':
                    print("¡Acertaste en un barco!")
                    oponente.tablero[fila][columna] = 'O'
                    for barco in oponente.flota:
                        if (fila, columna) in barco.area:
                            barco.numero_casillas -= 1
                            if barco.numero_casillas == 0:
                                oponente.flota.remove(barco)
                                print(f"Hundiste un barco {barco.nombre} del {nombre_jugador}!")
                                if not oponente.flota:
                                    print(f"{nombre_jugador} ha ganado!")
                                    exit()
                    return True
                elif oponente.tablero[fila][columna] == ' ':
                    print("¡Fallaste!")
                    oponente.tablero[fila][columna] = '-'
                    return False
                else:
                    print("Ya has disparado en esa posición. Inténtelo de nuevo.")
            except (ValueError, IndexError):
                print("Posición no válida. Inténtelo de nuevo.")

    def jugar(self):
        print("¡Bienvenido a la Batalla Naval!")
        while True:
            if self.turno_colocar_barcos <= 2:
                self.colocar_barcos_manualmente()
                self.turno_colocar_barcos += 1
            else:
                if self.turno_disparo == 1:
                    self.disparar(self.jugador1, self.jugador2)
                    self.turno_disparo = 2
                else:
                    self.disparar(self.jugador2, self.jugador1)
                    self.turno_disparo = 1

if __name__ == "__main__":
    juego = BatallaNaval()
    juego.jugar()
