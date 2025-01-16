import reflex as rx

def leftcol() -> rx.Component:
    return rx.vstack(
        rx.text("Experiencia laboral", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("Prenzl Repair, Berlin, Alemania: Practicas", size="4"),
                    rx.text("Marzo del 2023 - Junio del 2023"),
                    rx.text(
                        "Mantenimiento y reparacion de ordenadores y telefonos moviles: reemplazo de pantallas, camaras, baterias y puertos de carga"),
                    padding_y="15px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("Chiocciola Computer, Montesilvano, Italia: Practicas", size="4"),
                    rx.text("Julio del 2022"),
                    rx.text(
                        "Mantenimiento y reparacion de ordenadores y dispositivos electronicos: cambio de discos duros e instalacion de sistemas operativos"),
                    padding_y="15px"
                ),
            ),
            list_style_type="none"
        ),
        rx.text("Formacion academica", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("IES Nervion, en Sevilla", size="4"),
                    rx.text("Septiembre del 2023 - presente"),
                    rx.text("Tecnico Superior en Desarrollo de Aplicaciones Multiplataforma"),
                    padding_y="15px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("IES Juan de Mairena, en Mairena del Aljarafe", size="4"),
                    rx.text("Septiembre del 2021 - Junio del 2023"),
                    rx.text("Tecnico Medio en Sistemas Microinformaticos y Redes"),
                    rx.text("Mejor expediente de la clase (Media: 9,3)"),
                    padding_y="15px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("IES Cavaleri, en Mairena del Aljarafe", size="4"),
                    rx.text("Septiembre del 2017 - Junio del 2021"),
                    rx.text("Educacion Secundaria Obligatoria"),
                    padding_y="15px"
                ),
            ),
            list_style_type="none"
        ),
        rx.text("Experiencia relevante", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("Reparacion de ordenadores a familiares"),
                    padding_y="15px"
                ),
            ),
            list_style_type="none"
        ),
    )