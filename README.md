# HeroUI Provider

Modern UI components for the Reflex Python Web Framework.
> I will update the classNames props later.

## Features

- Modern UI components with a clean, consistent design
- Built specifically for Reflex web applications
- Customizable themes and styling
- TypeScript and Python type hints
- Framer Motion animations
- Tailwind CSS integration

## Installation

```bash
uv pip install heroui-provider
```

## Quick Start

```python
import reflex as rx
import heroui as hero

# Create a state
class State(rx.State):
    count: int = 0
    
    def increment(self):
        self.count += 1
        
    def decrement(self):
        self.count -= 1

# Build your UI
def index():
    return rx.container(
        hero.provider(
            rx.vstack(
                hero.avatar(
                    name="John Doe",
                    size="lg",
                    src="https://api.dicebear.com/9.x/glass/svg?seed=Kingston",
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
            ),
        )
    )

# Create and run the app
app = rx.App()
app.add_page(index)
```

## Configuration

The HeroUI Provider comes with Tailwind configuration. In your `rxconfig.py` file:

```python
import reflex as rx

tailwindplugin: dict = {
    "name": "@heroui/theme",
    "import": {"name": "heroui", "from": "@heroui/theme"},
    "call": "heroui",
}

HeroUILinker: str = "./node_modules/@heroui/theme/dist/**/*.{js,ts,jsx,tsx}"

config = rx.Config(
    app_name="my_app",
    tailwind={
        "theme": {"extend": {}},
        "content": [HeroUILinker],
        "darkMode": "class",
        "plugins": [
            "@tailwindcss/typography",
            tailwindplugin,
        ],
    },
)
```

## Components

- `provider`: Main HeroUI provider component
- `avatar`: Profile image or initials display
- `button`: Clickable actions
- `card`: Content container with various states
- `checkbox`: Selection input
- `input`: Text input field
- `radio`: Radio button selection
- `textarea`: Multiline text input
- `alert`: Notification and message display
- More components available!

Check the [documentation](https://github.com/itsmeadarsh2008/heroui-provider) for complete component details.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Reflex Web Framework](https://reflex.dev)
- Wrapper over [HeroUI](https://www.heroui.com)