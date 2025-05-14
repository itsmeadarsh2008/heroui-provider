import reflex as rx
from typing import Any, Dict, Literal, Optional, Union


lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Avatar(rx.Component):
    """A component that displays a user's profile picture, initials, or fallback icon.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        src: The source URL of the image.
        alt: Alternative text for the image for accessibility.
        name: The name of the user to derive initials from.
        icon: Custom icon to display when image fails to load.
        size: The size of the avatar.
        radius: The border radius of the avatar.
        color: The color scheme of the avatar.
        variant: The visual style variant of the avatar.
        is_bordered: Whether the avatar has a border.
        is_disabled: Whether the avatar is disabled.
        show_fallback: Whether to show fallback content when image fails to load.
        disable_animation: Whether to disable animations.
    """

    library = "@heroui/avatar"
    lib_dependencies: list = lib_deps
    tag = "Avatar"

    # Props
    src: rx.Var[Optional[str]]
    alt: rx.Var[Optional[str]]
    name: rx.Var[Optional[str]]
    icon: rx.Var[Optional[Any]]
    fallback: rx.Var[Optional[Any]]
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "full"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
    variant: rx.Var[Literal["solid", "bordered", "flat", "faded"]] = "solid"
    is_bordered: rx.Var[bool] = False
    is_disabled: rx.Var[bool] = False
    is_focusable: rx.Var[bool] = False
    img_component: rx.Var[Optional[str]] = "img"
    img_props: rx.Var[Optional[Dict[str, Any]]] = {}
    show_fallback: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False


class AvatarGroup(rx.Component):
    """A component that displays a group of avatars.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        max: Maximum number of avatars to display before showing the count.
        is_grid: Whether to display avatars in a grid layout.
        is_bordered: Whether all avatars in the group have borders.
        is_disabled: Whether all avatars in the group are disabled.
        disable_animation: Whether to disable animations.
        size: The size of all avatars in the group.
        radius: The border radius of all avatars in the group.
        color: The color scheme of all avatars in the group.
    """

    library = "@heroui/avatar"
    lib_dependencies: list = lib_deps
    tag = "AvatarGroup"

    # Props
    max: rx.Var[Optional[int]] = 5
    is_grid: rx.Var[bool] = False
    is_bordered: rx.Var[bool] = False
    is_disabled: rx.Var[bool] = False
    disable_animation: rx.Var[bool] = False
    render_count: rx.Var[Optional[int]]  # Kind of suspicious, take a look at this
    size: rx.Var[Literal["sm", "md", "lg"]] = "md"
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "full"
    color: rx.Var[
        Literal["default", "primary", "secondary", "success", "warning", "danger"]
    ] = "default"
