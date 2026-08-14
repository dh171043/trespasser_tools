import random
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Union
from archive_rules_models.arch_loadout import Weapon, allweapons
from archive_rules_models.arch_character_model import Attributes


weapon = next (w for w in allweapons if w.name == "ssword")
skill_roll = Attributes.skill_roll

@dataclass
class Craft:
    name: str
    key: str
    craft_hp: int
    feature1: str
    feature1_desc: str
    feature2: str
    feature2_desc: str

@dataclass
class Type(str, Enum):
    innate = "Innate"
    spell = "Spell"
    missile = "Missile"
    melee = "Melee"
    versatile = "Versatile"
    tool = "Tool"

@dataclass
class AttSup(str, Enum):
    attack = "Attack"
    support = "Support"


@dataclass
class VS(str, Enum):
    guard = "Guard"
    resist = "Resist"
    support = "10"

@dataclass
class Deed:
    craft: str
    strength: str
    name: str
    type: Type
    attsup: AttSup
    vs: VS
    target: str
    base: str
    hit: str
    spark: str
    special: str


# blood
blood = Craft(
    name="Blood",
    key="Might",
    craft_hp=0,
    feature1="Blood Manipulation",
    feature1_desc="do cool blood things",
    feature2="Life Affinity",
    feature2_desc="You gain a spark when doing life magic",
)

Incision = Deed(
    craft= "blood", 
    strength="Light",
    name="Incision",
    type= "versatile",
    attsup= "attack",
    vs= "guard",
    target="1 Creature",
    base="",
    hit=f"deal {weapon.damage} damage. Confer bleeding 2.",
    spark="Confer bleeding 4 instead.",
    special=""
)


# illusion
illusion = Craft(
    name = "Illusion",
    key="Intellect",
    craft_hp=0,
    feature1="Minor Projcetion",
    feature1_desc= "Create small illusions. Detailed ones may require an Intellect | Magic Check.",
    feature2= "Illusion Affinity",
    feature2_desc= "Gain a spark on casting checks when performing rituals and incantations that involves illusions, concealment, or deception."
)
repulsion = Deed(
    craft= "illusion", 
    strength="Light",
    name="Repulsion",
    type= "spell",
    attsup= "support",
    vs= "support",
    target="Personal",
    base="Until your next turn, the target gains a +2 bonus to guard checks. Enemies that attack and miss the target are pushed 2.",
    hit=f"Those enemies also gain weak 2.",
    spark="",
    special=""
)

spectral_slash = Deed(
    craft= "illusion", 
    strength="Light",
    name="Spectral Slash",
    type= "spell",
    attsup= "attack",
    vs= "guard",
    target="Path 4",
    base="",
    hit=f"deal {sum(Attributes.skill_roll + Attributes.skill_roll)} damage.",
    spark="Confer weary 2.",
    special=""
)

dazing_light = Deed(
    craft= "illusion", 
    strength="Heavy",
    name="Dazing Light",
    type= "spell",
    attsup= "attack",
    vs= "resist",
    target="1 creature",
    base=f"deal {sum(Attributes.skill_roll + Attributes.skill_roll)} damage.",
    hit=f"Confer staggered 4. An affected creature loses 1 action point at the start of its turn and can't take reactions.",
    spark="",
    special=""
)

phantom_beast = Deed(
    craft= "illusion", 
    strength="Heavy",
    name="Phantom Beast",
    type= "spell",
    attsup= "Support",
    vs= "support",
    target="Personal",
    base=f"Gain phantom beast 4. It does cool stuff.",
    hit="Gain phantom beast 6 instead.",
    spark="Gain phantom beast 8 instead.",
    special=""
)
mirror_cage = Deed(
    craft= "illusion", 
    strength="Mighty",
    name="Mirror Cage",
    type= "spell",
    attsup= "Support",
    vs= "support",
    target="Blast 4",
    base=f"Gain mirror cage 4. It does cool stuff.",
    hit="Gain mirror cage 6 instead.",
    spark="",
    special=""
)
illusion_deeds = [repulsion, spectral_slash, dazing_light, phantom_beast, mirror_cage]

storms = Craft(
    name="Storms",
    key="Agility",
    craft_hp=0,
    feature1="Bellwether",
    feature1_desc= "You know how the weather will change over the next week. Additionally, your party can travel through poor and severe weather at normal speeds.",
    feature2="Weather Affinity",
    feature2_desc="Gain a spark on casting checks when performing rituals and incantations that involves altering the weather or creating a meterological effect."

)
wilds = Craft(
    name="Wilds",
    key="Spirit",
    craft_hp=0,
    feature1="Greenblood",
    feature1_desc= "Collect and extra ingredient when using the forage camp action, even on a failure.",
    feature2= "Wild Affinity",
    feature2_desc= "Gain a spark on casting checks when performing rituals and incantations that involve flora or fauna."
)

wind = Craft(
    name="Wind",
    key="Agility",
    craft_hp=0,
    feature1="Windwarp",
    feature1_desc= "You can create minor magical effects that interact with the element of air. When creating challenging effects use Agility | Magic to determine the effect.",
    feature2= "Air Affinity",
    feature2_desc= "Gain a spark on casting checks when performing rituals and incantations that involve wind or manipulating air in some way."
)

allcrafts = [blood, illusion, storms, wilds, wind]
alldeeds = [illusion_deeds]







