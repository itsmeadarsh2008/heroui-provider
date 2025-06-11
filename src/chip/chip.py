import reflex as rx
from typing import Any, Dict, Literal, Optional, Union

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]

class Chip(rx.Component):
    library = "@heroui/chip"
    lib_dependencies: list = lib_deps
    tag = "Chip"
    variant: rx.Var[Literal["solid","bordered","light", "flat","faded", "shadow", "dot"]] = "solid"
    color: rx.Var[Literal["default", "primary", "secondary", "success", "warning", "danger"]] = "default"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "full"
    avatar: rx.Var[Optional[Any]]
    icon: rx.Var[Optional[Any]]
    start_content: rx.Var[Optional[Any]]
    end_content: rx.Var[Optional[Any]]
    is_disabled: rx.Var[bool] = False
    on_close: rx.EventHandler[lambda e: [e]]