import reflex as rx
from typing import Any, Literal, Optional, Union

# Space type definition
SpaceType = Union[
    Literal[
        0,
        0.5,
        1,
        1.5,
        2,
        2.5,
        3,
        3.5,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        16,
        20,
        24,
        28,
        32,
        36,
        40,
        44,
        48,
        52,
        56,
        60,
        64,
        72,
        80,
        96,
        "px",
    ],
    str,  # For string values not covered by the literals
]

lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]

class Spacer(rx.Component):
    """A component that creates empty space between elements.

    Attributes:
        library: The library the component belongs to.
        lib_dependencies: Dependencies required by the component.
        tag: The tag name for the component.
        x: The amount of horizontal space to create.
        y: The amount of vertical space to create.
    """

    library = "@heroui/spacer"
    lib_dependencies: list = lib_deps
    tag = "Spacer"
    # Props
    x: rx.Var[Optional[SpaceType]] = "1"
    y: rx.Var[Optional[SpaceType]] = "1"
