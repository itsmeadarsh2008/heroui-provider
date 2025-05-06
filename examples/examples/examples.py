"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from alert import alert
from provider import provider
from rxconfig import config
# from iconify import icon


class State(rx.State):
    """The app state."""

    ...


from reflex.style import set_color_mode, color_mode


def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )


colors = ["default", "primary", "secondary", "success", "warning", "danger"]


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        dark_mode_toggle(),
        provider(
            *[
                rx.container(
                    alert(
                        title=f"This is a {color} alert",
                        description="This is how description looks like 🤩",
                        color=color,
                        is_closable=True,
                    )
                )
                for color in colors
            ]
        ),
    )


app = rx.App()
app.add_page(index)
