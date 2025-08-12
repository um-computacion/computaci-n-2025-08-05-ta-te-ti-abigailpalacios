class PosOcupadaException(Exception):
    pass


class Tablero:
    def __init__(self):
        self.tablero = [
            ["", "", "",],
            ["", "", "",],
            ["", "", "",]
        ]

    def poner_ficha(self, fil, col, ficha):
        if 0<= fil < 3 and 0 <= col < 3: 
            if self.tablero[fil][col] == "":
                self.tablero[fil][col] = ficha
            else:
                raise PosOcupadaException("posición ocupada!")
        else: 
            raise IndexError(f"No existe la casilla {fil}, {col}")
        
    def mostrar(self):
        for i, fila in enumerate(self.tablero):
            print(" | ".join(c if c != "" else " " for c in fila))
            if i < 2:
                print("-" * 9)
            