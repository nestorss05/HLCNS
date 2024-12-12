import reflex as rx

def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback="NS", variant="solid"),
                rx.text("Nestor Sanchez", size="5"),
                padding_x="20px", align="center", padding_y="30px",
            ),
            rx.flex(
                rx.text(
                    "Tengo 19 años, y soy una persona muy formal, responsable y metódica, interesado en la IA. Desde siempre he estado atraído por la informática, y más en concreto por los móviles, por lo que he podido desarrollar habilidades autodidactas sobre el tema."),
                padding_x="20px"
            ),
        ),
        rx.vstack(
            rx.text(
                "Primera parte de domicilio"),
            rx.text(
                "41927 Mairena del Aljarafe (Sevilla)"),
            rx.text(
                "+34 Telefono"),
            rx.text(
                "Correo"),
            padding_x="20px", padding_y="30px"
        )
    )