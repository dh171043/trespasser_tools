from dataclasses import dataclass
from enum import Enum

@dataclass
class Clock:
    total_segments: int
    completed_segments: int = 0

@dataclass
class Injury:
    name: str
    injury_clock: Clock
    effect: str

@dataclass
class Plight:
    name: str
    effect: str

@dataclass
class Health:
    current_hp: int
    max_hp: int
    current_recovery_dice: int
    maximum_recovery_dice: int
    current_endurance: int
    maximum_endurance: int
    plight1: Plight
    plight2: Plight
    plight3: Plight
    injury1: Injury
    injury2: Injury
    injury3: Injury
    


    

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


