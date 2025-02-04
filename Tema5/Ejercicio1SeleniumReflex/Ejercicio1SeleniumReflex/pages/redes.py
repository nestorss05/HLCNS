import reflex as rx

from Ejercicio1SeleniumReflex.routes import Ruta


@rx.page(route=Ruta.REDES.value)
def redes() -> rx.Component:
    return rx.vstack(
        rx.heading("Redes Sociales", id="page-redes"),
        rx.list(
            rx.list.item(
                rx.link(
                    rx.text("Instagram"),
                    href="https://www.instagram.com",
                    id="instagram",
                    is_external=True,
                ),
            ),
            rx.list.item(
                rx.link(
                    rx.text("TikTok"),
                    href="https://www.tiktok.com/es/",
                    id="tiktok",
                    is_external=True,
                ),
            ),
            rx.list.item(
                rx.link(
                    rx.text("Facebook"),
                    href="https://www.facebook.com",
                    id="facebook",
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