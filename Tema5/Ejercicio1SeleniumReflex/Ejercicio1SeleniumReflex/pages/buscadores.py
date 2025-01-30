import reflex as rx

from Ejercicio1SeleniumReflex.routes import Ruta


@rx.page(route=Ruta.BUSCADORES.value)
def buscadores() -> rx.Component:
    return rx.vstack(
        rx.heading("Buscadores", id="page-buscadores"),
        rx.list(
            rx.list.item("Google", id="google"),
            rx.list.item("Bing", id="bing"),
            rx.list.item("Baidu", id="baidu"),
        ),
        rx.link(
            rx.text("Volver"),
            href=Ruta.INDEX.value,
            id="volver"
        ),
    )