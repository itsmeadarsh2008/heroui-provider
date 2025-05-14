import reflex as rx
# from alert import alert
from provider import provider
from button import button
from card import *
from avatar import avatar
from textarea import textarea


class State(rx.State):
    """The app state."""

    markdown: str = "# Hello, World!"
    color: str = "primary"

    def change_markdown(self, value: str) -> None:
        """Change the markdown value."""
        self.markdown = value


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


# colors = ["default", "primary", "secondary", "success", "warning", "danger"]


def index() -> rx.Component:
    return rx.container(
        provider(
            rx.spacer(),
            avatar(src="https://i.pravatar.cc/150?u=a042581f4e29026024d", size="lg"),
            textarea(
                placeholder="Type something...",
                label="Input",
                color=State.color,
                size="lg",
                variant="bordered",
                is_disabled=False,
                is_readonly=False,
                is_invalid=False,
                is_required=True,
                disable_animation=False,
                auto_focus=True,
                full_width=True,
                padding=10,
                on_value_change=State.change_markdown,
            ),
            rx.container(
                rx.markdown(
                    State.markdown,
                    padding=10,
                    color=State.color,
                    size="lg",
                    variant="bordered",
                    is_disabled=False,
                    is_readonly=False,
                    is_invalid=False,
                    is_required=True,
                    disable_animation=False,
                    auto_focus=True,
                    full_width=True,
                ),
                padding=10,
            ),
            dark_mode_toggle(),
        ),
    )


app = rx.App()
app.add_page(index)
