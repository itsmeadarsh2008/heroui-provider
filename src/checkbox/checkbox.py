import reflex as rx
from typing import Any, Literal, Optional


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Checkbox(rx.Component):
    """A component that allows users to select multiple options from a set.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        color: The color scheme of the checkbox.
        size: The size of the checkbox.
        radius: The border radius of the checkbox.
        label: The label text of the checkbox.
        description: The description text of the checkbox.
        line_through: Whether to apply a line-through style to the label when checked.
        value: The value of the checkbox.
        name: The name attribute of the checkbox input element.
        icon: Custom icon to display when the checkbox is checked.
        is_disabled: Whether the checkbox is disabled.
        is_invalid: Whether the checkbox is in an invalid state.
        is_required: Whether the checkbox is required.
        is_indeterminate: Whether the checkbox is in an indeterminate state.
        is_selected: Whether the checkbox is selected (controlled component).
        default_selected: Whether the checkbox is selected by default.
    """

    library = "@heroui/checkbox"
    lib_dependencies: list = lib_deps
    tag = "Checkbox"

    # Props
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "primary"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "md"
    # label: rx.Var[Optional[str]]
    # description: rx.Var[Optional[str]]
    line_through: rx.Var[bool] = False
    value: rx.Var[Optional[str]]
    name: rx.Var[Optional[str]]
    icon: rx.Var[Optional[Any]]
    is_disabled: rx.Var[bool] = False
    is_invalid: rx.Var[bool] = False
    is_required: rx.Var[bool] = False
    is_indeterminate: rx.Var[Optional[bool]]
    is_selected: rx.Var[Optional[bool]]
    default_selected: rx.Var[Optional[bool]]
    validation_state: rx.Var[Optional[Literal["valid", "invalid"]]]
    disable_animation: rx.Var[bool] = False

    # Events
    on_value_change: rx.EventHandler[lambda is_selected: [is_selected]]
    on_change: rx.EventHandler[lambda e: [e]]


class CheckboxGroup(rx.Component):
    """A group of checkboxes.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        label: The label text of the checkbox group.
        description: The description text of the checkbox group.
        value: The current value of the checkbox group.
        default_value: The default value of the checkbox group.
        name: The name attribute of the checkbox group.
        orientation: The orientation of the checkbox group.
        color: The color scheme of all checkboxes in the group.
        size: The size of all checkboxes in the group.
        radius: The border radius of all checkboxes in the group.
        is_disabled: Whether all checkboxes in the group are disabled.
        is_invalid: Whether the checkbox group is in an invalid state.
        is_required: Whether the checkbox group is required.
    """

    library = "@heroui/checkbox"
    lib_dependencies: list = lib_deps
    tag = "CheckboxGroup"
    # Props
    orientation: rx.Var[Literal["horizontal", "vertical"]] = "vertical"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "primary"
    size: rx.Var[Literal["xs", "sm", "md", "lg", "xl"]] = "md"
    radius: rx.Var[Literal["none", "base", "xs", "sm", "md", "lg", "xl", "full"]] = "md"
    name: rx.Var[Optional[str]]
    label: rx.Var[Optional[str]]
    value: rx.Var[Optional[list[str]]]
    line_through: rx.Var[bool] = False
    default_value: rx.Var[Optional[list[str]]]
    is_invalid: rx.Var[bool] = False
    validation_state: rx.Var[Optional[Literal["valid", "invalid"]]]  # deprecated
    description: rx.Var[Optional[Any]]
    error_message: rx.Var[Optional[Any]]
    validate: rx.Var[bool]
    validation_behavior: rx.Var[Optional[Literal["native", "aria"]]] = "native"
    is_disabled: rx.Var[bool] = False
    is_required: rx.Var[bool] = False
    is_read_only: rx.Var[bool]
    disable_animation: rx.Var[bool] = False
    on_change: rx.EventHandler[lambda value: [value]]
