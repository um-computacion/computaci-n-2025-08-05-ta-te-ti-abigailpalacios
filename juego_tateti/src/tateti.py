from .tablero import Tablero
from .jugador import Jugador

class Tateti:
    def __init__(self):
        self.jugador1 = Jugador(input("Nombre del jugador 1: "), "X")
        self.jugador2 = Jugador(input("Nombre del jugador 2: "), "O")
        self.turno = self.jugador1
        self.tablero = Tablero()

    def ocupar_casilla(self, fil, col):
        self.tablero.poner_ficha(fil, col, self.turno.ficha)
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1

    def ganador(self):
        for i in range(2):
            if self.tablero.tablero[i][0] == self.tablero.tablero[i][1] == self.tablero.tablero[i][2]:
                return self.tablero.tablero[i][0]
            if self.tablero.tablero[0][i] == self.tablero.tablero[1][i] == self.tablero.tablero[2][i]:
                return self.tablero.tablero[0][i]
            if self.tablero.tablero[0][0] == self.tablero.tablero[1][1] == self.tablero.tablero[2][2]:
                return self.tablero.tablero[0][0]
            if self.tablero.tablero[0][2] == self.tablero.tablero[1][1] == self.tablero.tablero[2][0]:
                return self.tablero.tablero[0][2]
        return None
    
    def tablero_lleno(self):
        return all(casilla != "" for fila in self.tablero.tablero for casilla in fila)
