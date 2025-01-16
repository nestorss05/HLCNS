import reflex as rx

from NestorssPage.routes import Ruta
from NestorssPage.views.body.leftcol import leftcol
from NestorssPage.views.body.rightcol import rightcol
from NestorssPage.views.footer.footer import footer
from NestorssPage.views.header.header import header
from NestorssPage.styles.styles import *
from NestorssPage.views.navbar.navbar import navbar


@rx.page(
    route=Ruta.CV.value
)

def cv() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        rx.hstack(
            leftcol(),
            rightcol(),
            padding_x="20px",
            padding_y="30px",
            max_width=MAX_WIDTH,
        ),
        footer(),
        align="center"
    )