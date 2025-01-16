from NestorssPage.routes import Ruta
from NestorssPage.views.footer.footer import footer
from NestorssPage.styles.styles import *
import reflex as rx

from NestorssPage.views.links.linksAbout import linksAbout
from NestorssPage.views.navbar.navbar import navbar


@rx.page(
    route=Ruta.ABOUT.value
)

def about() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.text("Esta pagina web ha sido creada con intenciones sanas, con besitos y sin intenciones de animo de lucro (aun asi, nos estamos lucrando de toda tu esquizofrenia, para que mentir, es que asi podemos alentar a la dupla esquizofrenica para que mi compañera de dupla este feliz, y ya de paso ayudarle a su causa de tumbar la US)",
                size="5"
        ),
        rx.text(
            "¿Y si tumbamos Alcosa?",
            size="3"
            ),
        rx.image(
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYmQJWr3FWROEHh7rTQEuBTjOIOd5GDjsifw&s",
            alt="Big CHUNGUS",
            width="400px",
        ),
        rx.hstack (
            linksAbout(),
            padding_x="20px",
            padding_y="30px",
            max_width=MAX_WIDTH,
        ),
        rx.text(
            "Pues a ver si nos ayuda el nota este que dice ser del DLC de Torreblanca...",
            size="2"
        ),
        footer(),
        align="center",
    )