from tateti import Tateti


def main():
    print("Bienvenido al juego de Tateti")
    juego = Tateti()
    while True:
        print("Tablero: ")
        juego.tablero.mostrar()
        print("Turno: ")
        print(f"Turno de: {juego.turno}")
        try:
            fil = int(input("Ingrese fila: ")) - 1
            col = int(input("Ingrese columna: ")) - 1
            juego.ocupar_casilla(fil, col)
        except Exception as e:
            print(e)
        if juego.ganador():
            print(f"¡El ganador es {juego.ganador()}!")
            break
        if juego.tablero_lleno():
            print("¡Empate!")
            break



if __name__ == '__main__':
    main()
