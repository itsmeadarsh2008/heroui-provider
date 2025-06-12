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
                hero.badge(
                    hero.avatar(
                        name="John Doe",
                        size="lg",
                        src="https://api.dicebear.com/9.x/glass/svg?seed=Kingston",
                    ),
                    content="1",
                ),
                hero.snippet(
                    rx.el.span("echo 'Hello, World!'"),
                ),
                hero.alert(
                    color="success",
                    title="🐚 Sea of Packages",
                    description="Don't forget to check out the documentation.",
                    # variant="solid",
                ),
                rx.flex(
                    hero.button("Increment", on_press=State.increment, color="success"),
                    rx.text(State.count),
                    hero.button("Decrement", on_press=State.decrement, color="danger"),
                    align="center",
                    margin="auto",
                    gap="1rem",
                ),
                hero.switch(
                    default_selected=False,
                    on_value_change=rx.toggle_color_mode,
                    start_content=rx.icon("sun"),
                    end_content=rx.icon("moon"),
                    color="success",
                    size="lg",
                ),
                hero.input(
                    placeholder="Type something...",
                    size="lg",
                    color_scheme="blue",
                    on_value_change=State.set_description,
                ),
                hero.spacer(x="2", y="2"),
                hero.card(
                    hero.card_body(
                        rx.text(State.description),
                    )
                ),
                hero.image(
                    src="https://app.requestly.io/delay/5000/https://heroui.com/images/hero-card-complete.jpeg",
                    height=200,
                    width=300,
                    is_blurred=True,
                    is_zoomed=True,
                ),
                hero.chip(
                    "v1.0.0 has been released!", variant="faded", color="success"
                ),
                hero.code("uv pip install heroui-provider"),
                hero.spinner(
                    size="lg",
                    variant="default",
                ),
            ),
        )
    )


app = rx.App()
app.add_page(index)
