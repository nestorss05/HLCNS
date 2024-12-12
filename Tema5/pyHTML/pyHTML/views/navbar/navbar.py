import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Home",
            height="40px"
        ),
        rx.text(
            "CV",
            height="40px"
        ),
        rx.text(
            "About",
            height="40px"
        ),
        width="100%",
        align="center",
        justify="center",
        position="sticky",
        bg="blue",
        padding_x="10px",
        padding_y="10px",
        z_index = 999,
    )