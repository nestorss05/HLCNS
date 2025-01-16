import reflex as rx

def button_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True,
        color_scheme="crimson"
    )