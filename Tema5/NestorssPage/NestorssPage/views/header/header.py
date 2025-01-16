import reflex as rx

from NestorssPage.routes import Ruta
from NestorssPage.styles.styles import HEADER


def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src="https://avatars.githubusercontent.com/u/145675254?s=400&u=4703bb96f07501e4b701f2e015d15b9c1bc32ad1&v=4",
                    alt="Mi cara",
                    width="100px",
                ),
                rx.text("Nestor Sanchez", size="5"), align="center", padding_y="30px",
            ),
            rx.flex(
                rx.text(
                    "Tengo 19 años, y soy una persona muy formal, responsable y metódica, interesado en la IA. Desde siempre he estado atraído por la informática, y más en concreto por los móviles, por lo que he podido desarrollar habilidades autodidactas sobre el tema."),
            ),
            padding_x="20px",
        ),
        rx.vstack(
            rx.text(
                "Primera parte de domicilio"),
            rx.text(
                "41927 Mairena del Aljarafe (Sevilla)"),
            rx.text(
                "+34 Telefono"),
            rx.text(
                "Correo"),
            padding_x="20px", padding_y="30px"
        )
    )