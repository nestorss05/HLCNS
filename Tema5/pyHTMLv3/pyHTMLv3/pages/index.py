from pyHTMLv3.routes import Ruta
from pyHTMLv3.views.body.leftcol import leftcol
from pyHTMLv3.views.body.rightcol import rightcol
from pyHTMLv3.views.footer.footer import footer
from pyHTMLv3.views.header.header import header
from pyHTMLv3.styles.styles import *
import reflex as rx

@rx.page(
    route=Ruta.INDEX.value
)

def index() -> rx.Component:
    return rx.vstack(
        header(),
        rx.hstack (
            leftcol(),
            rightcol(),
            padding_x="20px",
            padding_y="30px",
            max_width=MAX_WIDTH,
        ),
        footer(),
        align="center"
    )