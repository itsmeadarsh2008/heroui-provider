import reflex as rx
from typing import Any, Dict, Literal, Optional, Union


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Input(rx.Component):
    """A component that allows users to input text.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        variant: The visual style variant of the input.
        color: The color scheme of the input.
        size: The size of the input.
        radius: The border radius of the input.
        label: The label text of the input.
        placeholder: The placeholder text of the input.
        description: The description text of the input.
        error_message: The error message text of the input.
        type: The type of the input (text, password, etc.).
        start_content: Content to display at the start of the input.
        end_content: Content to display at the end of the input.
        label_placement: The placement of the label relative to the input.
        is_disabled: Whether the input is disabled.
        is_readonly: Whether the input is read-only.
        is_invalid: Whether the input is in an invalid state.
        is_required: Whether the input is required.
        disable_animation: Whether to disable animations.
        is_clearable: Whether the input can be cleared.
        auto_focus: Whether the input should automatically get focus when mounted.
        full_width: Whether the input should take the full width of its container.
    """

    library = "@heroui/input"
    lib_dependencies: list = lib_deps
    tag = "Input"

    # Props
    variant: rx.Var[Literal["flat", "bordered", "faded", "underlined"]] = "flat"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "md"
    label: rx.Var[Optional[str]]
    value: rx.Var[Optional[str]]
    default_value: rx.Var[Optional[str]]
    placeholder: rx.Var[Optional[str]]
    description: rx.Var[Optional[str]]
    error_message: rx.Var[Optional[str]]
    validate: rx.Var[Optional[str]]
    min_length: rx.Var[Optional[int]]
    max_length: rx.Var[Optional[int]]
    pattern: rx.Var[Optional[str]]
    type: rx.Var[
        Literal[
            "text",
            "password",
            "email",
            "number",
            "url",
            "tel",
            "search",
            "date",
            "time",
            "datetime-local",
            "month",
            "week",
        ]
    ] = "text"
    start_content: rx.Var[Optional[Any]]
    end_content: rx.Var[Optional[Any]]
    label_placement: rx.Var[Literal["inside", "outside", "outside-left"]] = "inside"
    is_disabled: rx.Var[bool] = False
    is_read_only: rx.Var[bool] = False
    is_invalid: rx.Var[bool] = False
    is_required: rx.Var[bool] = False
    is_clearable: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False
    auto_focus: rx.Var[bool] = False
    full_width: rx.Var[bool] = False

    # Events
    on_value_change: rx.EventHandler[lambda value: [value]]
    on_change: rx.EventHandler[lambda e: [e]]
