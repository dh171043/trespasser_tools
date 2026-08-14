import random
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Union
from archive_rules_models.arch_loadout import Weapon, allweapons
from archive_rules_models.arch_craft_deed import Craft, Deed, allcrafts, alldeeds


# ==================== FEATURES AND TALENS ====================
HP = 12



weapon = Weapon



@dataclass
class Talent:
    name: str
    desc: str




@dataclass
class Enhancement:
    name: str
    desc: str



@dataclass
class Feature:
    name: str
    description: str

blank_talent = Talent(name="Blank Talent", desc="Blank Talent")

blank_enhancement = Enhancement(name="Blank Enhancement", desc="Blank Enhancement")

ex_fort = Feature(
    "Expert Fortitude",
    "When you take up this calling, your hit points increase by an extra +5. This makes your hit point total at second level equal to 15 + 2 (MIGHT).",
)
sac_spell = Feature("Sacred Incantations", "Cast spells")
devo = Feature("Aspect of Devotion", "gain an aspect appropriate to your god")
revelation = Feature(
    "Revelation", "Gain the revelation special deed and do things with it"
)


@dataclass
class Chassis:
    calling_hp = int
    features: list[Feature]
    crafts: list[Craft]
    light_deeds: list[Deed]
    heavy_deeds: list[Deed]
    mighty_deeds: list[Deed]
    talents: list[Talent]
    enhancements: list[Enhancement]


cleric = Chassis(
    calling_hp= 5,
    features=[ex_fort, sac_spell, devo, revelation],
    crafts=[blood],
    light_deeds=[Incision],
    heavy_deeds=[],
    mighty_deeds=[],
    talents=[],
    enhancements=[],
)

