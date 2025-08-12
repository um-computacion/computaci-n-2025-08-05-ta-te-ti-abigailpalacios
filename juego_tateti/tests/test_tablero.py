import unittest
from src.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):

    def test_tablero_vacio(self):
        tablero = Tablero()
        for fila in tablero.tablero:
            for casilla in fila:
                self.assertEqual(casilla, "")

    def test_llenar_casilla(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        self.assertEqual(tablero.tablero[0][0], "X")

    def test_posicion_ocupada(self):
        tablero = Tablero()
        tablero.poner_ficha(0,0,"X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_ficha(0,0,"0")

    def test_error_num_fila(self):
        tablero = Tablero()
        with self.assertRaises(IndexError):
            tablero.poner_ficha(0,9, "0")

    def test_error_num_columna(self):
        tablero = Tablero()
        with self.assertRaises(IndexError):
            tablero.poner_ficha(9,0, "0")


    def test_mostrar_tablero(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        tablero.mostrar()

    