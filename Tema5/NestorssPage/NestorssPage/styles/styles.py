from enum import Enum
import reflex as rx

# Constantes
MAX_WIDTH = "1500px"

# Tamanios
class Size(Enum):
    SMALL = "8px",
    MEDIUM = "12px",
    DEFAULT = "16px",
    BIG = "32px"

# Estilos
BASE_STYLE = {
    rx.vstack: {
        "width":"100%",
        "height":"100%"
    },
    rx.link: {
        "text-decoration":"none"
    },
    rx.text: {
        "padding_x":"20px",
        "text-align": "justify",
    }
}

HEADER = {
    rx.vstack: {
        "width":"100%",
        "height":"100%"
    }
}