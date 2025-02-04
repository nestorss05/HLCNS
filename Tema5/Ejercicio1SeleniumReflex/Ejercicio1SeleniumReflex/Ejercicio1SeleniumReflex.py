"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from Ejercicio1SeleniumReflex.pages.index import index
from Ejercicio1SeleniumReflex.pages.buscadores import buscadores
from Ejercicio1SeleniumReflex.pages.redes import redes

class State(rx.State):
    """The app state."""

    ...

app = rx.App()