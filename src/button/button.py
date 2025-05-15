import reflex as rx
from typing import Any, Literal, Optional, Union


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Button(rx.Component):
    """A clickable button component that triggers an action or event.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        children: The content of the button.
        variant: The visual style variant of the button.
        color: The color scheme of the button.
        size: The size of the button.
        radius: The border radius of the button.
        start_content: Content to display at the start of the button.
        end_content: Content to display at the end of the button.
        spinner: Custom spinner component to show when loading.
        spinner_placement: Where to place the spinner in the button.
        full_width: Whether the button should take the full width of its container.
        is_icon_only: Whether the button contains only an icon.
        is_disabled: Whether the button is disabled.
        is_loading: Whether the button is in a loading state.
        disable_ripple: Whether to disable the ripple effect.
        disable_animation: Whether to disable animations.
    """

    library = "@heroui/button"
    lib_dependencies: list = lib_deps
    tag = "Button"

    # Props
    # children: rx.Var[Any]
    variant: rx.Var[
        Literal["solid", "bordered", "light", "flat", "faded", "shadow", "ghost"]
    ] = "solid"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]]
    start_content: rx.Var[Optional[Any]]
    end_content: rx.Var[Optional[Any]]
    spinner: rx.Var[Optional[Any]]
    spinner_placement: rx.Var[Literal["start", "end"]] = "start"
    full_width: rx.Var[bool] = False
    is_icon_only: rx.Var[bool] = False
    is_disabled: rx.Var[bool] = False
    is_loading: rx.Var[bool] = False
    disable_ripple: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False

    # Events
    on_press: rx.EventHandler[lambda e: [e]]
    on_press_start: rx.EventHandler[lambda e: [e]]
    on_press_end: rx.EventHandler[lambda e: [e]]
    on_press_change: rx.EventHandler[lambda is_pressed: [is_pressed]]
    on_press_up: rx.EventHandler[lambda e: [e]]
    on_key_down: rx.EventHandler[lambda e: [e]]
    on_key_up: rx.EventHandler[lambda e: [e]]
    on_click: rx.EventHandler[lambda e: [e]]


class ButtonGroup(rx.Component):
    """A group of buttons with consistent styling.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        children: The content of the button group (buttons).
        variant: The visual style variant for all buttons in the group.
        color: The color scheme for all buttons in the group.
        size: The size for all buttons in the group.
        radius: The border radius for the button group.
        full_width: Whether the button group should take the full width of its container.
        is_disabled: Whether all buttons in the group are disabled.
    """

    library = "@heroui/button"
    lib_dependencies: list = lib_deps
    tag = "ButtonGroup"

    # Props
    # children: rx.Var[Union[Any, list[Any]]]
    variant: rx.Var[
        Literal["solid", "bordered", "light", "flat", "faded", "shadow", "ghost"]
    ] = "solid"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "xl"
    full_width: rx.Var[bool] = False
    is_disabled: rx.Var[bool] = False
