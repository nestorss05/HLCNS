import datetime

import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.icon("hand-metal"),
        rx.text(f"{datetime.date.today().year}"),
        rx.link("SECCO", href="http://localhost:3000/"),
        padding_y="24px"
    )