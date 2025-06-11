import reflex as rx
from typing import Any, Dict, Literal, Optional, Union

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Code(rx.Component):
    library = "@heroui/code"
    lib_dependencies: list = lib_deps
    tag = "Code"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    color: rx.Var[Literal["default", "primary", "secondary", "success", "warning", "danger"]] = "default"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "full"
    is_disabled: rx.Var[bool] = False
    children: rx.Var[Optional[Any]] = None
    code: rx.Var[Optional[str]] = None
