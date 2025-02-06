import reflex as rx

from Ejercicio2SeleniumReflex.routes import Ruta

class FormState(rx.State):
    form_data: dict = {},

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

@rx.page(route=Ruta.INDEX.value, title="Formulario de registro - Mi web")
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Formulario de registro", id="heading"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Nombre",
                    name="nombre",
                    id="nombre",
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
    )