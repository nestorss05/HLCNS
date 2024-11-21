from random import randint


class Wordle:
    PALABRAS = ["ANGEL", "JAMON", "LENTO", "VERDE", "PLAYA", "HIELO", "FUEGO", "MANGO", "BANCO", "SALTO"]
    palabraJuego = ""
    pistas = [["-----", "-----"], ["-----", "-----"], ["-----", "-----"], ["-----", "-----"], ["-----", "-----"], ["-----", "-----"]]
    numIntento = 0

    @staticmethod
    def seleccionaJuego():
        i = randint(0, len(Wordle.PALABRAS) - 1)
        Wordle.palabraJuego = Wordle.PALABRAS[i]

    ## Son todas las cosas estaticas??
    def realizaIntento(self, intento):
        ## Incompleto
        self.pistas[self.numIntento][0] = self.palabraJuego

        self.numIntento += 1

    @staticmethod
    def acertado(intento):
        acertado = False
        ## Si se ha acertado la jugada, se establecera acertado a true
        if Wordle.palabraJuego == intento:
            acertado = True
        return acertado

    @staticmethod
    def pintaPistas():
        tabla = ""
        ## Recorre toda la tabla
        for i in range(0, len(Wordle.pistas)):
            ## Asigna las posiciones de cada jugada
            tabla += Wordle.pistas[i][0] + " | " + Wordle.pistas[i][1]
            ## Si no esta en la ultima linea, haz un salto de pagina
            if i < len(Wordle.pistas) - 1:
                tabla += "\n"
        return tabla