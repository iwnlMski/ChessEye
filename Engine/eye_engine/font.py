from enum import Enum


class Font(str, Enum):
    BLUE = '\033[94m'
    RED = "\x1b[31;1m"
    CLEAR = '\033[0m'
    WHITE = CLEAR
