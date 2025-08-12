import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    
    def test_crear_jugador1(self):
        jugador = Jugador("Martin", "X")
        self.assertEqual(jugador.nombre, "Martin")
        self.assertEqual(jugador.ficha, "X")

    def test_crear_jugador2(self):
        jugador = Jugador("Abi", "0")
        self.assertEqual(jugador.nombre, "Abi")
        self.assertEqual(jugador.ficha, "0")

    def test_dos_jugadores(self):
        jugador1 = Jugador("Abi", "X")
        jugador2 = Jugador("martin", "0")
        self.assertEqual(jugador1.nombre, "Abi")
        self.assertEqual(jugador2.nombre, "martin")

    def test_str_jugador(self):
        jugador = Jugador("Abi", "X")
        self.assertEqual(str(jugador), "Abi (X)")

    def test_mismo_nombre(self):
        jugador1 = Jugador("Tita", "X")
        jugador2 = Jugador("Tita", "0")
        self.assertEqual(jugador1.nombre, jugador2.nombre)