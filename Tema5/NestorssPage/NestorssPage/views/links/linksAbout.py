import reflex as rx

from NestorssPage.components.button_link import button_link
from NestorssPage.routes import Ruta


def linksAbout() -> rx.Component:
    return rx.vstack(
        button_link("Mas info", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        align="center",
    )