import reflex as rx

tailwindplugin: dict = {
    "name": "@heroui/theme",
    "import": {"name": "heroui", "from": "@heroui/theme"},
    "call": "heroui",
}

HeroUILinker: str = "./node_modules/@heroui/theme/dist/**/*.{js,ts,jsx,tsx}"
# Installation Process:
# 1. Import the necessary modules.
# 2. Define the tailwind plugin and HeroUI linker.
# 3. Create a configuration object for the app.
# 4. Set the app name and tailwind configuration.

config = rx.Config(
    app_name="examples",
    plugins=[],
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
