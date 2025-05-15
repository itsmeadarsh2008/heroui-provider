import reflex as rx
import heroui as hero


class State(rx.State):
    """The app state."""

    count: int = 0
    description: str = "This is a description."

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def set_description(self, value: str):
        self.description = value

    def change_body(self, value: str):
        self.description = "It is animated by default. Wrapper over @heroui"

def index() -> rx.Component:
    return rx.container(
        hero.provider(
            # hero.theme(),
            rx.vstack(
                hero.avatar(
                    name="John Doe",
                    size="lg",
                    src="https://api.dicebear.com/9.x/glass/svg?seed=Kingston",
                ),
                rx.flex(
                    # change dark mode to light mode
                    hero.button(
                        rx.icon("eclipse"),
                        color_scheme="blue",
                        on_press=rx.toggle_color_mode,
                    ),
                ),
                rx.flex(
                    hero.button(
                        "Increment",
                        on_press=State.increment,
                        color="success"
                    ),
                    rx.text(State.count),
                    hero.button(
                        "Decrement",
                        on_press=State.decrement,
                        color="danger"
                    ),
                    align="center",
                    margin="auto",
                    gap="1rem",
                ),
                hero.input(
                    placeholder="Type something...",
                    size="lg",
                    color_scheme="blue",
                    on_value_change=State.set_description,
                ),
                hero.card(
                    hero.card_body(
                        rx.text(State.description),
                    ),
                    on_press=State.change_body
                ),
            ),
        )
    )


app = rx.App()
app.add_page(index)
