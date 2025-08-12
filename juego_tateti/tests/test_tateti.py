import unittest
from src.tateti import Tateti
from src.tablero import Tablero
from src.jugador import Jugador

class TestTateti(unittest.TestCase):


    def test_ganador_columna(self):
        tateti = Tateti()
        tateti.tablero.poner_ficha(0, 0, "X")
        tateti.tablero.poner_ficha(1, 0, "X")
        tateti.tablero.poner_ficha(2, 0, "X")
        self.assertEqual(tateti.ganador(), "X")

        

    def test_ganador_fila(self):
        tateti = Tateti()
        tateti.tablero.poner_ficha(0, 0 , "X")
        tateti.tablero.poner_ficha(0, 1, "X")
        tateti.tablero.poner_ficha(0, 2, "X")
        self.assertEqual(tateti.ganador(), "X")
        

    def test_ganador_diagonal(self):
        tateti = Tateti()
        tateti.tablero.poner_ficha(0, 0 , "X")
        tateti.tablero.poner_ficha(1, 1, "X")
        tateti.tablero.poner_ficha(2, 2, "X")
        self.assertEqual(tateti.ganador(), "X")

    def test_empate(self):
        tateti = Tateti()
        tateti.tablero.poner_ficha( 0, 1 , "X")
        tateti.tablero.poner_ficha( 0, 0, "0")
        tateti.tablero.poner_ficha( 1, 0, "X")
        tateti.tablero.poner_ficha( 1,1, "0")
        tateti.tablero.poner_ficha( 2,0, "X")
        tateti.tablero.poner_ficha( 2,1, "0")
        tateti.tablero.poner_ficha( 0,2, "X")
        tateti.tablero.poner_ficha( 1,2, "0")
        tateti.tablero.poner_ficha( 2,2, "X")
        self.assertEqual(tateti.tablero_lleno(), True)
        self.assertEqual(tateti.ganador(), None)

if __name__ == '__main__':
    unittest.main()