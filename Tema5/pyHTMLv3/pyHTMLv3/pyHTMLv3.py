"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from pyHTMLv3.pages.courses import courses
from pyHTMLv3.pages.index import index
from pyHTMLv3.styles.styles import *


class State(rx.State):
    """The app state."""

    ...

app = rx.App(style=BASE_STYLE)