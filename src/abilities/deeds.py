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