__all__ = (
    'ModeEnum',
    'ModeDetector',
)

from enum import StrEnum


class ModeEnum(StrEnum):
    RGB = 'RGB'
    RED = 'RED'
    GREEN = 'GREEN'
    BLUE = 'BLUE'

    # In future add inverted and mixed


class ModeDetector:
    _MODE_TO_FUNCTION = {

    }

