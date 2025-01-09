"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from pyHTML.styles.styles import *
from pyHTML.views.body.leftcol import leftcol
from pyHTML.views.body.rightcol import rightcol
from pyHTML.views.footer.footer import footer
from pyHTML.views.header.header import header

class State(rx.State):
    """The app state."""

    ...


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


app = rx.App(style=BASE_STYLE)
app.add_page(index)