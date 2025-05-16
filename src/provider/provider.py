import reflex as rx
from typing import Literal, Optional
from .types import SupportedLocales


class Provider(rx.Component):
    """A provider component that manages global HeroUI settings and theme.

    Attributes:
        library: The library the component belongs to.
        tag: The tag name for the component.
        locale: The locale setting for internationalization.
        label_placement: The default placement for input labels (inside, outside, outside-left).
        spinner_variant: The default visual style for spinners.
        disable_animation: Whether to disable animations globally.
        disable_ripple: Whether to disable ripple effects globally.
        skip_framer_motion_animations: Whether to skip Framer Motion animations.
        validation_behavior: The validation behavior to use (native, aria).
        reduced_motion: How to handle motion reduction for accessibility.
    """

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
