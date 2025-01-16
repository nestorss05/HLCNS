import datetime

import reflex as rx

from NestorssPage.routes import Ruta


def footer() -> rx.Component:
    return rx.hstack(
        rx.icon("hand-metal"),
        rx.text(f"{datetime.date.today().year}", padding_x="2px"),
        rx.link("Esquizo", href=Ruta.INDEX.value),
        padding_y="24px",
    )