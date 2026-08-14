import random
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Union

# ==================== CHARACTER RECORD ====================
@dataclass
class Record:
    player: str
    trespasser_name: str
    words_to_live_by: str


# ==================== ATTRIBUTES AND SKILLS ====================
@dataclass
class Attributes:
    might: int
    agility: int
    intellect: int
    spirit: int
    skill: int
    _key: str
    skill_die: int

    @property
    def key(self):
        return getattr(self, self._key)
    @property
    def skill_roll(self) -> int:
        roll = random.randint(1, self.skill_die)
        return roll


@dataclass
class Skills:
    alchemy: bool
    athletics: bool
    crafting: bool
    folklore: bool
    letters: bool
    magic: bool
    nature: bool
    perception: bool
    speech: bool
    stealth: bool
    tinkering: bool


@dataclass
class Attrs_Skills:
    attributes: Attributes
    skills: Skills


# ==================== ADVANCEMENT ====================
@dataclass
class Lineage:
    race: str
    curse: str
    gift: str


@dataclass
class PastLife:
    past_life: str
    bonus_attr: list[str]
    skill: list[str]
    possessions: list[str]