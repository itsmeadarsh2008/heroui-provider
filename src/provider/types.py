from typing import Callable, Dict, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired, Protocol

# Basic types
Href = Union[str, Dict[str, str]]
"""Type for navigation href that can be either a string or a dictionary with URL parameters."""

RouterOptions = Dict[str, any]
"""Type for router options used in navigation."""


# Calendar related types
class CalendarDate:
    """Represents a date without any time components in a specific calendar system.

    This class is used for calendar-related functionality in the HeroUI components.
    """

    pass


class Calendar(Protocol):
    """Protocol for calendar system implementations.

    This protocol defines the interface that calendar implementations must follow.
    """

    pass


SupportedCalendars = Literal[
    "gregory", "hebrew", "islamic-civil", "ethiopic", "persian"
]
"""Supported calendar systems for date handling in HeroUI components."""

# Locale types
SupportedLocales = Literal[
    "ar-AE",
    "ar-BH",
    "ar-DZ",
    "ar-EG",
    "ar-IQ",
    "ar-JO",
    "ar-KW",
    "ar-LB",
    "ar-LY",
    "ar-MA",
    "ar-OM",
    "ar-QA",
    "ar-SA",
    "ar-SY",
    "ar-TN",
    "ar-YE",
    "cs-CZ",
    "da-DK",
    "de-AT",
    "de-CH",
    "de-DE",
    "el-GR",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-US",
    "en-ZA",
    "es-AR",
    "es-BO",
    "es-CL",
    "es-CO",
    "es-CR",
    "es-DO",
    "es-EC",
    "es-ES",
    "es-GT",
    "es-HN",
    "es-MX",
    "es-NI",
    "es-PA",
    "es-PE",
    "es-PR",
    "es-PY",
    "es-SV",
    "es-UY",
    "es-VE",
    "fi-FI",
    "fr-BE",
    "fr-CA",
    "fr-CH",
    "fr-FR",
    "he-IL",
    "hi-IN",
    "hu-HU",
    "id-ID",
    "it-CH",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "nl-BE",
    "nl-NL",
    "no-NO",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "sk-SK",
    "sv-SE",
    "th-TH",
    "tr-TR",
    "zh-CN",
    "zh-HK",
    "zh-TW",
]
"""Supported locale codes for internationalization in HeroUI components."""


class DefaultDatesType(TypedDict):
    """Type for default dates range that can be selected in the calendar.

    Attributes:
        minDate: The minimum selectable date in the calendar.
        maxDate: The maximum selectable date in the calendar.
    """

    minDate: NotRequired[Optional[CalendarDate]]
    maxDate: NotRequired[Optional[CalendarDate]]


# Provider prop types
class HeroUIProviderProps(TypedDict):
    """Type definitions for HeroUIProvider props.

    This TypedDict defines all the configuration options that can be passed to
    the HeroUIProvider component to customize its behavior globally.
    """

    # Routing
    navigate: NotRequired[Optional[Callable[[Href, Optional[RouterOptions]], None]]]
    useHref: NotRequired[Optional[Callable[[Href], str]]]

    # Localization
    locale: NotRequired[Optional[SupportedLocales]]

    # Calendar
    defaultDates: NotRequired[Optional[DefaultDatesType]]
    createCalendar: NotRequired[
        Optional[Callable[[SupportedCalendars], Optional[Calendar]]]
    ]

    # UI Preferences
    labelPlacement: NotRequired[Optional[Literal["inside", "outside", "outside-left"]]]
    spinnerVariant: NotRequired[
        Optional[Literal["default", "simple", "gradient", "wave", "dots", "spinner"]]
    ]

    # Animation and Effects
    disableAnimation: NotRequired[bool]
    disableRipple: NotRequired[bool]
    skipFramerMotionAnimations: NotRequired[bool]

    # Accessibility
    validationBehavior: NotRequired[Literal["native", "aria"]]
    reducedMotion: NotRequired[Literal["user", "always", "never"]]
