import reflex as rx

def rightcol() -> rx.Component:
    return rx.vstack(
        rx.text("Aptitudes de programacion", size="4"),
        rx.text("Lenguajes de programacion"),
        rx.list.unordered(
            rx.list.item("Java"),
            rx.list.item("Python"),
            rx.list.item("C#"),
            rx.list.item("JavaScript"),
        ),
        rx.text("Lenguajes de marcas"),
        rx.list.unordered(
            rx.list.item("HTML"),
            rx.list.item("CSS"),
        ),
        rx.text("Bases de datos"),
        rx.list.unordered(
            rx.list.item("SQL Server"),
            rx.list.item("MySQL"),
        ),
        rx.text("Frameworks"),
        rx.list.unordered(
            rx.list.item(".NET MAUI"),
            rx.list.item("Jetpack Compose"),
            rx.list.item("ASP.NET MVC"),
        ),
        rx.text("Aptitudes personales", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("Persona resolutiva y con facilidad para trabajar en equipo"),
                    padding_y="4px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("Dispuesto a explorar nuevas metodologias y ampliar aprendizajes"),
                    padding_y="4px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("Capacidad de planificacion y establecer objetivos y metas"),
                    padding_y="4px"
                ),
            ),
            list_style_type="none"
        ),
        rx.text("Idiomas", size="4"),
        rx.list.unordered(
            rx.list.item(
                rx.vstack(
                    rx.text("Español nativo"),
                    padding_y="4px"
                ),
            ),
            rx.list.item(
                rx.vstack(
                    rx.text("C1 en Ingles de Cambridge"),
                    padding_y="4px"
                ),
            ),
            list_style_type="none"
        ),
    )