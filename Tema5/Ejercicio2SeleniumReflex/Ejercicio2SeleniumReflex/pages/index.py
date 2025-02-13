from threading import Event

import reflex as rx

from Ejercicio2SeleniumReflex.routes import Ruta

class FormState(rx.State):
    form_data: dict = {},
    nombre = ""
    apellidos = ""
    sexo = ""
    correo = ""
    checkbox1: bool = True
    checkbox2: bool

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setApellidos(self, apellidos: str):
        self.apellidos = apellidos

    def setSexo(self, sexo: str):
        self.sexo = sexo

    def setCorreo(self, correo: str):
        self.correo = correo

    def setCheckbox1(self, checkbox1: bool):
        self.checkbox1 = checkbox1

    def setCheckbox2(self, checkbox2: bool):
        self.checkbox2 = checkbox2

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
                    rx.text("Sexo: "),
                    rx.radio_group(
                        [
                            "Masculino", "Femenino",
                        ],
                        id="sexo",
                        on_change=FormState.setSexo,
                    ),
                    rx.input(value=FormState.sexo, id="sexoEscogido", type="hidden"),
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
                        on_change=FormState.setCheckbox1,
                        checked=FormState.checkbox1,
                        id="checkbox1",
                    ),
                    rx.text("Deseo recibir informacion sobre novedades y ofertas: "),
                ),
                rx.hstack(
                    rx.checkbox(
                        on_change=FormState.setCheckbox2,
                        checked=FormState.checkbox2,
                        id="checkbox2",
                    ),
                    rx.text("Declaro haber leido y aceptar las condiciones generales del programa y la normativa sobre proteccion de datos: "),
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