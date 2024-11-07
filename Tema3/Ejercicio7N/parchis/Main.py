from parchis.Parchis import Parchis

def main():
    gano = False
    ganador = ""
    turno = 1
    jugador1 = input("Dame nombre J1: ")
    jugador2 = input("Dame nombre J2: ")
    while jugador1 == jugador2:
        jugador2 = input("Dame nombre J2. Venga, no puede ser el mismo. ")
    partida = Parchis(jugador1, jugador2)
    while not gano:
        dobles = False
        ganador = partida.esGanador()
        if ganador != "":
            gano = True
            break
        else:
            jugadorJugando = jugador1 if turno == 1 else jugador2
            input("Dale ya a enter para lanzar el dado, fiera")
            print("Turno de " + jugadorJugando)
            Parchis.tiraDados()
            print("Tiro 1: " + str(partida.dado1))
            print("Tiro 2: " + str(partida.dado2))
            if partida.dado1 == partida.dado2:
                dobles = True
            Parchis.avanzaPosiciones(partida, turno)
            print(Parchis.pintaTablero(partida))
            Parchis.estadoCarrera(partida)
            if not dobles:
                turno = 2 if turno == 1 else 1
    print("Ganador: " + ganador)

if __name__ == "__main__":
    main()