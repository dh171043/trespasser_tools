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