import reflex as rx

from NestorssPage.components.button_link import button_link
from NestorssPage.routes import Ruta


def links() -> rx.Component:
    return rx.vstack(
        button_link("LinkedIn", "https://shorturl.at/j29yg", "linkedin"),
        button_link("GitHub", "https://github.com/nestoorss", "github"),
        button_link("CV", Ruta.CV.value, "cv"),
        align="center",
    )