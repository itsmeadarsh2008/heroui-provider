import reflex as rx
from provider import tailwindplugin, HeroUILinker

# Installation Process:
# 1. Import the necessary modules.
# 2. Define the tailwind plugin and HeroUI linker.
# 3. Create a configuration object for the app.
# 4. Set the app name and tailwind configuration.

config = rx.Config(
    app_name="examples",
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
