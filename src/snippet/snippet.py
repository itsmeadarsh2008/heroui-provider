import reflex as rx
from typing import Any, Literal, Optional, Union


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


# Type aliases for component props
TooltipProps = dict[str, Any]
"""Type for tooltip component properties."""

ButtonProps = dict[str, Any]
"""Type for button component properties."""


class Snippet(rx.Component):
    """A code snippet component with copy functionality and customizable appearance.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        size: The size of the snippet component.
        radius: The border radius of the snippet.
        symbol: The symbol to display before the code (string or ReactNode).
        timeout: The timeout duration for copy feedback in milliseconds.
        code_string: The code string to be copied to clipboard.
        tooltip_props: Additional props for the tooltip component.
        copy_icon: Custom icon for the copy button.
        check_icon: Custom icon shown after successful copy.
        disable_tooltip: Whether to disable the tooltip.
        disable_copy: Whether to disable copy functionality.
        hide_copy_button: Whether to hide the copy button.
        hide_symbol: Whether to hide the symbol.
        copy_button_props: Additional props for the copy button.
        disable_animation: Whether to disable animations.
    """

    library = "@heroui/snippet"
    lib_dependencies: list = lib_deps
    tag = "Snippet"

    # Props
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg"]] = "lg"
    symbol: rx.Var[Union[str, Any]] = "$"
    timeout: rx.Var[int] = 2000
    code_string: rx.Var[Optional[str]]
    tooltip_props: rx.Var[Optional[TooltipProps]]
    copy_icon: rx.Var[Optional[Any]]
    check_icon: rx.Var[Optional[Any]]
    disable_tooltip: rx.Var[bool] = False
    disable_copy: rx.Var[bool] = False
    hide_copy_button: rx.Var[bool] = False
    hide_symbol: rx.Var[bool] = False
    copy_button_props: rx.Var[Optional[ButtonProps]]
    disable_animation: rx.Var[bool] = False

    # Events
    on_copy: rx.EventHandler[lambda e: [e]]
