import reflex as rx
from typing import Any, Literal, Optional


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Card(rx.Component):
    """A surface component that contains and groups related content.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        shadow: The shadow depth of the card (none, sm, md, lg).
        radius: The border radius of the card (none, sm, md, lg).
        full_width: Whether the card should take the full width of its container.
        is_hoverable: Whether the card has a hover effect.
        is_pressable: Whether the card is pressable.
        is_blurred: Whether the card has a blurred effect.
        is_footer_blurred: Whether the card footer has a blurred effect.
        is_disabled: Whether the card is disabled.
        disable_animation: Whether to disable animations.
        disable_ripple: Whether to disable the ripple effect.
        allow_text_selection_on_press: Whether to allow text selection when pressing the card.
        on_press: Event handler called when the card is pressed.
        on_press_start: Event handler called when a press interaction starts.
        on_press_end: Event handler called when a press interaction ends.
        on_press_change: Event handler called when the press state changes.
        on_press_up: Event handler called when a press is released.
    """

    library = "@heroui/card"
    lib_dependencies: list = lib_deps
    tag = "Card"

    # Props
    # variant: rx.Var[Literal["solid", "bordered", "flat", "faded", "shadow"]] = "solid"
    shadow: rx.Var[Literal["none","sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg"]] = "lg"
    full_width: rx.Var[bool] = False
    is_hoverable: rx.Var[bool] = False
    is_pressable: rx.Var[bool] = False
    is_blurred: rx.Var[bool] = False
    is_footer_blurred: rx.Var[bool] = False
    is_disabled: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False
    disable_ripple: rx.Var[bool] = False
    allow_text_selection_on_press: rx.Var[bool] = False
    

    # Events
    on_press: rx.EventHandler[lambda e: [e]]
    on_press_start: rx.EventHandler[lambda e: [e]]
    on_press_end: rx.EventHandler[lambda e: [e]]
    on_press_change: rx.EventHandler[lambda e: [e]]
    on_press_up: rx.EventHandler[lambda e: [e]]



class CardHeader(rx.Component):
    """The header section of a card.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
    """

    library = "@heroui/card"
    lib_dependencies: list = lib_deps
    tag = "CardHeader"


class CardBody(rx.Component):
    """The body section of a card.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
    """

    library = "@heroui/card"
    lib_dependencies: list = lib_deps
    tag = "CardBody"


class CardFooter(rx.Component):
    """The footer section of a card.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
    """

    library = "@heroui/card"
    lib_dependencies: list = lib_deps
    tag = "CardFooter"
