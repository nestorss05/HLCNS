"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from NestorssPage.pages.index import index
from NestorssPage.pages.cv import cv
from NestorssPage.pages.about import about
from NestorssPage.styles.styles import *


class State(rx.State):
    """The app state."""

    ...

app = rx.App(style=BASE_STYLE)