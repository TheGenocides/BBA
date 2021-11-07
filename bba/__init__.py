from typing import Literal, NamedTuple

from .client import *
from .errors import *
from .objects import *

__title__ = "BBA"
__version__ = "0.1.0"
__author__ = "TheGenocides"
__license__ = "MIT"
__copyright__ = "Copyright 2021 TheGenocides"


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int

version_info: VersionInfo = VersionInfo(major=0, minor=1, micro=0, releaselevel="alpha", serial=0)