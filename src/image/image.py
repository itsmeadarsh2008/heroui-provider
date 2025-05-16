import reflex as rx
from typing import Any, Literal, Optional

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]


class Image(rx.Component):
    """A component that displays images with various styling and loading options.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        src: The source URL of the image.
        src_set: A list of image sources for different display sizes.
        sizes: Defines the display size of the image for different viewport sizes.
        alt: Alternative text for the image for accessibility.
        width: The width of the image in pixels.
        height: The height of the image in pixels.
        radius: The border radius of the image (none, sm, md, lg, full).
        shadow: The shadow depth of the image (none, sm, md, lg, xl).
        fallback_src: The source URL of the fallback image to display when the main image fails to load.
        is_blurred: Whether to apply a blur effect to the image.
        is_zoomed: Whether to apply a zoom effect on hover.
        remove_wrapper: Whether to remove the wrapper element around the image.
        disable_skeleton: Whether to disable the skeleton loading animation.
        on_load: Event handler called when the image loads successfully.
        on_error: Event handler called when the image fails to load.
    """

    library = "@heroui/image"
    lib_dependencies: list = lib_deps
    tag = "Image"
    src: rx.Var[str]
    src_set: rx.Var[Optional[str]]
    sizes: rx.Var[Optional[str]]
    alt: rx.Var[Optional[str]]
    width: rx.Var[Optional[int]]
    height: rx.Var[Optional[int]]
    radius: rx.Var[Literal["none", "sm", "md", "lg", "full"]] = "md"
    shadow: rx.Var[Literal["none", "sm", "md", "lg", "xl"]] = "none"
    fallback_src: rx.Var[Optional[str]]
    is_blurred: rx.Var[bool] = False
    is_zoomed: rx.Var[bool] = False
    remove_wrapper: rx.Var[bool] = False
    disable_skeleton: rx.Var[bool] = False
    on_load: rx.EventHandler[lambda e: [e]]
    on_error: rx.EventHandler[lambda e: [e]]
