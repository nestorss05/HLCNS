from threading import Event

import reflex as rx

from Ejercicio2SeleniumReflex.routes import Ruta

class FormState(rx.State):
    form_data: dict = {},
    nombre = ""
    apellidos = ""
    correo = ""
    novs: bool = True

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setApellidos(self, apellidos: str):
        self.apellidos = apellidos

    def setCorreo(self, correo: str):
        self.correo = correo

    def setNovs(self, novs: bool):
        self.novs = novs

@rx.page(route=Ruta.INDEX.value, title="Formulario de registro - Mi web")
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Formulario de registro", id="heading"),
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.text("Nombre: "),
                    rx.input(
                        placeholder="Nombre",
                        value=FormState.nombre,
                        on_change=FormState.setNombre,
                        id="nombre",
                        type="text",
                        max_length=50,
                    ),
                ),
                rx.hstack(
                    rx.text("Apellidos: "),
                    rx.input(
                        placeholder="Apellidos",
                        value=FormState.apellidos,
                        on_change=FormState.setApellidos,
                        id="apellidos",
                        type="text",
                        max_length=50,
                    ),
                ),
                rx.hstack(
                    rx.text("Correo: "),
                    rx.input(
                        placeholder="Correo",
                        value=FormState.correo,
                        on_change=FormState.setCorreo,
                        id="correo",
                        type="text",
                    ),
                ),
                rx.hstack(
                    rx.checkbox(
                        on_change=FormState.setNovs,
                        checked=FormState.novs
                    ),
                    rx.text("Deseo recibir informacion sobre novedades y ofertas: "),
                    id="novs",
                ),
                rx.button(
                    rx.text("Enviar"),
                    type="submit",
                    id="enviar",
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
    )