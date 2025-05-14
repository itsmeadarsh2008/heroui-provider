import reflex as rx
import heroui as hero


class State(rx.State):
    """The app state."""

    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.container(
        hero.provider(
            hero.card(
                hero.input(placeholder="Enter your name"),
                hero.button("Submit", color="primary", margin="10px"),
                spacing="4",
                padding="6px",
                margin="10px"
            ),
            # Figure out why this is not working and below thing throwing rx.foreach error
            # hero.button("Increment", on_click=State.increment),
            # rx.text(f"Count: {State.count}"),
            # hero.button("Decrement", on_click=State.decrement),
        )
    )


app = rx.App()
app.add_page(index)
