import reflex as rx
from typing import Any, Literal, Optional, Union

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Badge(rx.Component):
    library = "@heroui/badge"
    lib_dependencies: list = lib_deps
    tag = "Badge"
    content: rx.Var[Union[str, int, Any]]
    variant: rx.Var[Literal["solid", "flat", "faded", "shadow"]] = "solid"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    shape: rx.Var[Literal["circle", "rectangle"]] = "rectangle"
    placement: rx.Var[
        Literal["top-right", "top-left", "bottom-right", "bottom-left"]
    ] = "top-right"
    show_outline: rx.Var[bool] = True
    disable_outline: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False
    is_invisible: rx.Var[bool] = False
    is_one_char: rx.Var[bool] = False
    is_dot: rx.Var[bool] = False
