from dataclasses import dataclass
from enum import Enum

class Health:
    def __init__(self, HP, recovery_dice, endurance,
                 injury1, injury1_name, injury1_clock, injury1_effect,
                 injury2, injury2_name, injury2_clock, injury2_effect,
                 injury3, injury3_name, injury3_clock, injury3_effect):
        self.HP = HP
        self.recover_dice = recovery_dice
        self.endurance = endurance
        self.injury1 = [injury1_name, injury1_clock, injury1_effect]
        self.injury2 = [injury2_name, injury2_clock, injury2_effect]
        self.injury3 = [injury3_name, injury3_clock, injury3_effect]



@dataclass
class Alignment:
    name: str
    affirm: int = 0
    deny: int = 0



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



human = Lineage(race='Race of Man', curse='Curse of Power', gift='Human Ingenuity')

@dataclass
class Calling(str, Enum):
    cleric = 'Cleric'
    diabolist= 'Diabolist'
    invoker= 'Invoker'
    knight = 'Knight'
    magician = 'Magician'
    marauder = 'Marauder'
    thief = 'Thief'
    warrior = 'Warrior'

@dataclass
class Advancement:
    level: int
    xp_current: int
    lineage: Lineage
    past_life: PastLife
    calling: Calling
    alignment1: Alignment
    alignment2: Alignment
    _xp_next: int = 10


    @property
    def xp_next(self):
        xp_next = self.level*10
        return xp_next

test = Advancement(2, 10)

print('xp_next =', test.xp_next)


