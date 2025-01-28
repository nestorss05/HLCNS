import reflex as rx

from NestorssPage.routes import Ruta


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(rx.avatar(fallback="NS", variant="solid", color_scheme="red"),href=Ruta.INDEX.value,),
            rx.text(rx.link("Nestor Sanchez", href=Ruta.INDEX.value, color_scheme="red"), size="5", padding_x="2px"),
            rx.text(rx.link("Acerca de", href=Ruta.ABOUT.value, color_scheme="red"), size="5", padding_x="2px"),
            padding_x="20px", align="center", padding_y="30px",
        ),
    )