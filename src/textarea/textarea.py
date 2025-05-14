import reflex as rx
from typing import Any, Optional, Literal

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Textarea(rx.Component):
    """A component that allows users to input multiline text.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        variant: The visual style variant of the textarea.
        color: The color scheme of the textarea.
        size: The size of the textarea.
        radius: The border radius of the textarea.
        label: The label text of the textarea.
        placeholder: The placeholder text of the textarea.
        description: The description text of the textarea.
        error_message: The error message text of the textarea.
        min_rows: The minimum number of visible rows.
        max_rows: The maximum number of visible rows.
        disable_resize: Whether to disable resizing of the textarea.
        start_content: Content to display at the start of the textarea.
        end_content: Content to display at the end of the textarea.
        label_placement: The placement of the label relative to the textarea.
        is_disabled: Whether the textarea is disabled.
        is_readonly: Whether the textarea is read-only.
        is_invalid: Whether the textarea is in an invalid state.
        is_required: Whether the textarea is required.
        disable_animation: Whether to disable animations.
        auto_focus: Whether the textarea should automatically get focus when mounted.
        full_width: Whether the textarea should take the full width of its container.
    """

    library = "@heroui/input"
    lib_dependencies: list = lib_deps
    tag = "Textarea"

    # Props
    min_rows: rx.Var[Optional[int]]
    max_rows: rx.Var[Optional[int]]
    cache_measurements: rx.Var[bool] = False
    variant: rx.Var[Literal["flat", "bordered", "faded", "underlined"]] = "flat"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]]
    label: rx.Var[Optional[Any]]
    value: rx.Var[Optional[str]]
    default_value: rx.Var[Optional[str]]
    placeholder: rx.Var[Optional[str]]
    start_content: rx.Var[Optional[Any]]
    end_content: rx.Var[Optional[Any]]
    description: rx.Var[Optional[str]]
    error_message: rx.Var[Optional[str]]
    validate: rx.Var[Optional[str]]
    validation_behavior: rx.Var[Literal["native", "aria"]] = "native"
    label_placement: rx.Var[Literal["inside", "outside", "outside-left"]] = "inside"
    full_width: rx.Var[bool] = True
    is_required: rx.Var[bool] = False
    is_read_only: rx.Var[bool]
    is_disabled: rx.Var[bool] = False
    is_invalid: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False

    # Events
    on_change: rx.EventHandler[lambda e: [e]]
    on_value_change: rx.EventHandler[lambda value: [value]]
    on_clear: rx.EventHandler[lambda x: x]
    # not tested the below thing yet feel free to test it:
    on_height_change: rx.EventHandler[lambda height, meta: [height, meta["row_height"]]]  # noqa: F821
