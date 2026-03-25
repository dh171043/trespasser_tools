from dataclasses import dataclass


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


@dataclass
class Skills:
    alchemy: bool
    athletics: bool
    crafting: bool
    folklore: bool
    letters: bool
    nature: bool
    perception: bool
    speech: bool
    stealth: bool
    tinkering: bool


@dataclass
class Attrs_Skills:
    attributes: Attributes
    skills: Skills

test = Attrs_Skills(
    Attributes(1, 2, 1, 1, 1, 'agility', 6), 
    Skills(alchemy=True, athletics=True, crafting=False, folklore=True, letters=False, nature=True, perception=True, speech=False, stealth=True, tinkering=True)
)

accuracy = (test.attributes.key + test.attributes.skill)
print(accuracy, )