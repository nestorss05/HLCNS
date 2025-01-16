import reflex as rx

def leftcol() -> rx.Component:
    return rx.vstack(
        rx.text("Odio a RENFE", size="4"),
        rx.image(
          src="https://imagenes.heraldo.es/files/image_640_360/files/fp/uploads/imagenes/2023/08/08/64d1f708b0d35.r_d.384-554-9083.jpeg",
            alt="QUE SE QUEME",
            width="500px",
        ),
        rx.text("Odio a TUSSAM", size="4"),
        rx.image(
            src="https://s1.abcstatics.com/abc/sevilla/media/201401/23/tussam-quemado-autobus--644x362.jpg",
            alt="QUE SE QUEME",
            width="500px",
        ),
        rx.text("Odio al Metro y al Consorcio", size="4"),
        rx.image(
            src="https://static.grupojoly.com/clip/b86a999e-588f-4220-b565-2c5b68bc39a2_source-aspect-ratio_1600w_0.jpg",
            alt="QUE SE QUEME",
            width="500px",
        ),
    )