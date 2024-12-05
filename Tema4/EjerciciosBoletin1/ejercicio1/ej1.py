from random import randint
from threading import Thread
from time import sleep

class Trabajador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print("Soy", self.name, "y es mi hora del curro")
        sleep(randint(1,10))