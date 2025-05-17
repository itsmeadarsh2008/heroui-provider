import reflex as rx
from typing import Any, Literal, Optional

lib_deps:list = ["@heroui/theme", "@heroui/system", "framer-motion"]

class Spinner(rx.Component):
    """A component that displays a loading spinner with various styling options.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        size: The size of the spinner (sm, md, lg).
        color: The color of the spinner (default, primary, secondary, success, warning, danger).
        variant: The visual style of the spinner (default, simple, gradient, wave, dots, spinner).
        label_color: The color of the spinner label (default, primary, secondary, success, warning, danger).
    """

    library = "@heroui/spinner"
    lib_dependencies: list = lib_deps
    tag = "Spinner"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    variant: rx.Var[
        Literal["default", "simple", "gradient", "wave", "dots", "spinner"]
    ] = "default"
    label_color: rx.Var[Literal["default", "primary", "secondary", "success", "warning", "danger"]] = "default"