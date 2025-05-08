import reflex as rx
from .types import *


class Provider(rx.Component):
    library = "@heroui/system"
    tag = "HeroUIProvider"

    # Localization
    locale: Optional[SupportedLocales] = "en-US"

    # UI Preferences
    label_placement: Optional[Literal["inside", "outside", "outside-left"]] = "inside"
    spinner_variant: Optional[
        Literal["default", "simple", "gradient", "wave", "dots", "spinner"]
    ] = "default"

    # Animation and Effects
    disable_animation: rx.Var[bool] = False
    disable_ripple: rx.Var[bool] = False
    skip_framer_motion_animations: rx.Var[bool] = False

    # Accessibility
    validation_behavior: Literal["native", "aria"] = "native"
    reduced_motion: Literal["user", "always", "never"] = "user"


tailwindplugin: dict = {
    "name": "@heroui/theme",
    "import": {"name": "heroui", "from": "@heroui/theme"},
    "call": "heroui",
}
HeroUILinker: str = "./node_modules/@heroui/theme/dist/**/*.{js,ts,jsx,tsx}"
