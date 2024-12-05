from threading import Thread, Lock
from time import sleep


class Contador(Thread):
    contador = 0
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        Contador.bloqueo.acquire()
        while Contador.contador < 1000:
            ## TODO: Que entren los demas hilos
            Contador.contador += 1
            print("Soy el hilo", self.name, "y la vais a mascar. Contador", Contador.contador)
        Contador.bloqueo.release()