import reflex as rx

from Ejercicio1SeleniumReflex.routes import Ruta


@rx.page(route=Ruta.INDEX.value)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.heading("Enlaces favoritos", id="enlaces"),
        rx.list(
            rx.list.item(
                rx.link(
                rx.text("Buscadores"),
                href=Ruta.BUSCADORES.value,
                id="buscadores"
                ),
            ),
            rx.list.item("Redes sociales", id="redes"),
        )
    )