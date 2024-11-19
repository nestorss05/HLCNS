import random

class Parchis:
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0

    def __init__(self, nomJ1, nomJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        if len(nomJ1) <= 7:
            self.nomJ1 = nomJ1
        else:
            self.nomJ1 = nomJ1[0:7]
        if len(nomJ2) <= 7:
            self.nomJ2 = nomJ2
        else:
            self.nomJ2 = nomJ2[0:7]

    @staticmethod
    def tiraDados():
        Parchis.dado1 = random.randint(1, 6)
        Parchis.dado2 = random.randint(1, 6)

    def pintaTablero(self):
        tabla = ""
        for i in range(3):
            for j in range(Parchis.TAM_TABLERO+2):
                if j==0:
                    if i==0:
                        tabla += "\t\t"
                    elif i==1:
                        if len(self.nomJ1) < 4:
                            tabla += self.nomJ1 + "\t\t"
                        else:
                            tabla += self.nomJ1 + "\t"
                    else:
                        if len(self.nomJ2) < 4:
                            tabla += self.nomJ2 + "\t\t"
                        else:
                            tabla += self.nomJ2 + "\t"
                elif j==1:
                    tabla += "I\t"
                elif j==Parchis.TAM_TABLERO+1:
                    tabla += "F"
                else:
                    if i==0:
                        tabla += str(j-1) + "\t"
                    elif i==1:
                        if j == self.fichaJ1+1:
                            tabla += "O\t"
                        else:
                            tabla += "\t"
                    else:
                        if j == self.fichaJ2+1:
                            tabla += "O\t"
                        else:
                            tabla += "\t"
            tabla += "\n"
        return tabla

    def avanzaPosiciones(self, jugador: int):
        if jugador == 1:
            self.fichaJ1 += Parchis.dado1 + Parchis.dado2
            if self.fichaJ1 > Parchis.TAM_TABLERO:
                diferencia = self.fichaJ1 - Parchis.TAM_TABLERO
                self.fichaJ1 = Parchis.TAM_TABLERO - diferencia
        else:
            self.fichaJ2 += Parchis.dado1 + Parchis.dado2
            if self.fichaJ2 > Parchis.TAM_TABLERO:
                diferencia = self.fichaJ2 - Parchis.TAM_TABLERO
                self.fichaJ2 = Parchis.TAM_TABLERO - diferencia

    def estadoCarrera(self):
        vaGanando = ""
        if self.fichaJ1 > self.fichaJ2:
            vaGanando = self.nomJ1
        else:
            vaGanando = self.nomJ2
        print(vaGanando)
        return vaGanando

    def esGanador(self):
        ganador = ""
        if self.fichaJ1 == 20:
            ganador = self.nomJ1
        elif self.fichaJ2 == 20:
            ganador = self.nomJ2
        return ganador