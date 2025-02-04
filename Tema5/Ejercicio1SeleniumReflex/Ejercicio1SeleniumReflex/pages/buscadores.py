import reflex as rx

from Ejercicio1SeleniumReflex.routes import Ruta


@rx.page(route=Ruta.BUSCADORES.value)
def buscadores() -> rx.Component:
    return rx.vstack(
        rx.heading("Buscadores", id="page-buscadores"),
        rx.list(
            rx.list.item(
                rx.link(
                    rx.text("Google"),
                    href="https://www.google.es/",
                    id="google",
                    is_external=True,
                ),
            ),
            rx.list.item(
                rx.link(
                    rx.text("Bing"),
                    href="https://www.bing.com/?brdr=1",
                    id="bing",
                    is_external=True,
                ),
            ),
            rx.list.item(
                rx.link(
                    rx.text("Baidu"),
                    href="https://www.baidu.com/",
                    id="baidu",
                    is_external=True,
                ),
            ),
        ),
        rx.link(
            rx.text("Volver"),
            href=Ruta.INDEX.value,
            id="volver"
        ),
    )