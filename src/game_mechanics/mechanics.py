import random
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Union

# ==================== SPARKS AND SHADOWS ====================
@dataclass
class Sparks:
    canny: bool
    quick: bool
    quiet: bool
    safe: bool
    striking: bool


@dataclass
class Shadows:
    costly: bool
    slow: bool
    loud: bool
    harmful: bool
    daunting: bool

@dataclass
class Clock:
    total_segments: int
    completed_segments: int = 0