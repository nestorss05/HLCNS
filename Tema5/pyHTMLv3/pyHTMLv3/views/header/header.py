import reflex as rx

from pyHTMLv3.routes import Ruta
from pyHTMLv3.styles.styles import HEADER


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="NS", variant="solid"),
            rx.text("Nestor Sanchez", size="5"),
            rx.text(rx.link("Home", href=Ruta.INDEX.value), size="5"),
            rx.text(rx.link("Courses", href=Ruta.COURSES.value), size="5"),
            padding_x="20px", align="center", padding_y="30px",
        ),
    )