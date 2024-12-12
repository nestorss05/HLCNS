"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

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
            padding_x="25px", padding_y="30px"
        ),
        footer(),
        align="center"
    )


app = rx.App()
app.add_page(index)