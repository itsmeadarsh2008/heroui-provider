import reflex as rx
from typing import Any, Literal, Optional

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Switch(rx.Component):
    library = "@heroui/switch"
    lib_dependencies: list = lib_deps
    tag = "Switch"
    value: rx.Var[str]
    name: rx.Var[str]
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    thumb_icon: rx.Var[Optional[Any]]
    start_content: rx.Var[Optional[Any]]
    end_content: rx.Var[Optional[Any]]
    is_selected: rx.Var[Optional[bool]]
    default_selected: rx.Var[Optional[bool]]
    is_read_only: rx.Var[Optional[bool]]
    is_disabled: rx.Var[Optional[bool]] = False
    disable_animation: rx.Var[Optional[bool]] = False
    on_change: rx.EventHandler[lambda e: [e]]
    on_value_change: rx.EventHandler[lambda is_selected: [is_selected]]
