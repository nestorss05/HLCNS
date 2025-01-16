import reflex as rx

from NestorssPage.components.button_link import button_link
from NestorssPage.routes import Ruta


def links() -> rx.Component:
    return rx.vstack(
        button_link("LinkedIn", "https://shorturl.at/j29yg"),
        button_link("GitHub", "https://github.com/nestoorss"),
        button_link("CV", Ruta.CV.value),
        align="center",
    )