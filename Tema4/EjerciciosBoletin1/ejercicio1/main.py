from ej1 import Trabajador

if __name__ == "__main__":
    hilo1 = Trabajador("O Focas")
    hilo2 = Trabajador("Paquito Paco")
    hilo3 = Trabajador("La chari")

    hilo1.start()
    hilo2.start()
    hilo3.start()

    hilo1.join()
    hilo2.join()
    hilo3.join()