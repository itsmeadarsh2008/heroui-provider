import reflex as rx
from typing import Any, Literal, Optional


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Radio(rx.Component):
    """A radio button component that allows users to select a single option from a set.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        color: The color scheme of the radio button.
        size: The size of the radio button.
        value: The value of the radio button.
        label: The label text of the radio button.
        description: The description text of the radio button.
        name: The name attribute of the radio input element.
        is_disabled: Whether the radio button is disabled.
        is_invalid: Whether the radio button is in an invalid state.
        is_required: Whether the radio button is required.
        line_through: Whether to apply a line-through style to the label when selected.
    """

    library = "@heroui/radio"
    lib_dependencies: list = lib_deps
    tag = "Radio"

    # Props
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "primary"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    value: rx.Var[str]
    label: rx.Var[Optional[str]]
    description: rx.Var[Optional[str]]
    name: rx.Var[Optional[str]]
    is_disabled: rx.Var[bool] = False
    is_invalid: rx.Var[bool] = False
    is_required: rx.Var[bool] = False
    line_through: rx.Var[bool] = False


class RadioGroup(rx.Component):
    """A group of radio buttons that allows users to select a single option from a set.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        label: The label text of the radio group.
        description: The description text of the radio group.
        value: The current value of the radio group.
        default_value: The default value of the radio group.
        name: The name attribute of all radio buttons in the group.
        orientation: The orientation of the radio buttons in the group.
        color: The color scheme of all radio buttons in the group.
        size: The size of all radio buttons in the group.
        is_disabled: Whether all radio buttons in the group are disabled.
        is_invalid: Whether the radio group is in an invalid state.
        is_required: Whether the radio group is required.
    """

    library = "@heroui/radio"
    lib_dependencies: list = lib_deps
    tag = "RadioGroup"

    # Props
    label: rx.Var[Optional[str]]
    description: rx.Var[Optional[str]]
    value: rx.Var[Optional[str]]
    default_value: rx.Var[Optional[str]]
    name: rx.Var[Optional[str]]
    orientation: rx.Var[Literal["horizontal", "vertical"]] = "vertical"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "primary"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    is_disabled: rx.Var[bool] = False
    is_invalid: rx.Var[bool] = False
    is_required: rx.Var[bool] = False

    # Events
    on_value_change: rx.EventHandler[lambda value: [value]]
