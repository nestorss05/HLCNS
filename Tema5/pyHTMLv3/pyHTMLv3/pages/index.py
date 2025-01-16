from pyHTMLv3.routes import Ruta
from pyHTMLv3.views.footer.footer import footer
from pyHTMLv3.views.header.header import header
from pyHTMLv3.styles.styles import *
import reflex as rx

from pyHTMLv3.views.links.links import links


@rx.page(
    route=Ruta.INDEX.value
)

def index() -> rx.Component:
    return rx.vstack(
        header(),
        rx.hstack (
            links(),
            padding_x="20px",
            padding_y="30px",
            max_width=MAX_WIDTH,
        ),
        footer(),
        align="center"
    )