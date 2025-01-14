import reflex as rx

from pyHTML.components.button_link import button_link


def links() -> rx.Component:
    return rx.vstack(
        button_link("Bombardeen", "https://institutonervion.es/"),
        button_link("YouTube", "https://www.youtube.com/"),
        align="center",
    )