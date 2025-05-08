import reflex as rx
from typing import Any, Literal, Optional


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]

class Alert(rx.Component):
    """A component that displays important messages to the user.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        title: The title text of the alert.
        icon: The icon to display in the alert.
        description: The description text of the alert.
        color: The color scheme of the alert.
        variant: The visual style variant of the alert.
        radius: The border radius of the alert.
        start_content: Content to display at the start of the alert.
        end_content: Content to display at the end of the alert.
        is_visible: Whether the alert is visible.
        is_closable: Whether the alert can be closed.
        hide_icon: Whether to hide the icon.
        hide_icon_wrapper: Whether to hide the icon wrapper.
        close_button_props: Props for the close button.
        on_close: Callback when the alert is closed.
        on_visible_change: Callback when visibility changes.
    """

    library = "@heroui/alert"
    lib_dependencies: list = lib_deps
    tag = "Alert"

    # Props
    title: rx.Var[Optional[str]]
    icon: rx.Var[Optional[Any]]
    description: rx.Var[Optional[Any]]
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    variant: rx.Var[Literal["solid", "bordered", "flat", "faded"]] = "flat"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "md"
    start_content: rx.Var[Optional[Any]]
    end_content: rx.Var[Optional[Any]]
    is_visible: rx.Var[Optional[bool]]
    is_closable: rx.Var[bool] = False
    hide_icon: rx.Var[bool] = False
    hide_icon_wrapper: rx.Var[bool] = False
    close_button_props: rx.Var[Optional[dict]]

    # Events
    on_close: rx.EventHandler[lambda x: x]
    on_visible_change: rx.EventHandler[lambda is_visible: [is_visible]]
