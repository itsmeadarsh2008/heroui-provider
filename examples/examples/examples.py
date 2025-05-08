import reflex as rx
from alert import alert
from provider import provider
from button import button
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
            ],
            rx.flex(
                button("Hello World", color="primary"),
                button("Hello World", color="secondary"),
                button("Hello World", color="success"),
                button("Hello World", color="warning"),
                button("Hello World", color="danger"),
                button("Hello World", color="default"),
                spacing="3",
            ),
        ),    )


app = rx.App()
app.add_page(index)
