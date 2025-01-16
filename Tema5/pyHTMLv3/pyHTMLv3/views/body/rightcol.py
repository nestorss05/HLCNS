import reflex as rx

def rightcol() -> rx.Component:
    return rx.vstack(
        rx.text("Aptitudes de transportes publicos sevillanos", size="4"),
        rx.text("Metro de Sevilla"),
        rx.list.unordered(
            rx.list.item("Mal construido"),
            rx.list.item("Parece mas un tranvia"),
            rx.list.item("Se peta muy facil"),
            rx.list.item("Solo pasa por tres pueblos peste"),
        ),
        rx.text("Tranvia kk"),
        rx.list.unordered(
            rx.list.item("Es inutil"),
            rx.list.item("Cubre cuatro estaciones de metro (Puerta Jerez - Nervion)"),
        ),
        rx.text("TUSSAM"),
        rx.list.unordered(
            rx.list.item("No son electricos (menos cuatro gatos)"),
            rx.list.item("Pasan de tu culo"),
        ),
        rx.text("RENFE Cercanias"),
        rx.list.unordered(
            rx.list.item("Incomodo"),
            rx.list.item("Tardon como Miguel"),
            rx.list.item("La Jungla de la RENFE"),
        ),
        rx.text("Consorcio de Transportes", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("Llega 20 minutos tarde"),
                    padding_y="4px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("No llega a La Campana"),
                    padding_y="4px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("Horarios limitados (menos Coria y Gines)"),
                    padding_y="4px"
                ),
            ),
            list_style_type="none"
        ),
        rx.text("RENFE Media Distancia", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("Infravalorado, es goty"),
                    padding_y="4px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("Menti, se retrasa mucho"),
                    padding_y="4px"
                ),
            ),
            list_style_type="none"
        ),
    )