from NestorssPage.routes import Ruta
from NestorssPage.views.footer.footer import footer
from NestorssPage.styles.styles import *
import reflex as rx

from NestorssPage.views.links.links import links
from NestorssPage.views.navbar.navbar import navbar


@rx.page(
    route=Ruta.INDEX.value
)

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.text("Néstor Sánchez", size="7"),
        rx.image(
            src="https://avatars.githubusercontent.com/u/145675254?s=400&u=4703bb96f07501e4b701f2e015d15b9c1bc32ad1&v=4",
            alt="Mi cara",
            width="200px",
        ),
        rx.text("19 años, apasionado por la IA y por los moviles", size="4"),
        rx.text(
            "Lorem perezitsum es que me da pereza una descripcion mas detallada y encima Miguel llega tarde. Quien se fue a Sevilla, perdio su silla, pero yo llegue el primero a Sevilla asi que fui el ultimo en reirme. No saber coger un Consorcio desde Gelves no es excusa para llegar tarde, y lo mismo digo para ser esquizofrenico.",
            size="4",
        ),
        rx.hstack (
            links(),
            padding_x="20px",
            padding_y="30px",
            max_width=MAX_WIDTH,
        ),
        footer(),
        align="center"
    )