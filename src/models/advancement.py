@dataclass
class Calling(str, Enum):
    cleric = "Cleric"
    diabolist = "Diabolist"
    invoker = "Invoker"
    knight = "Knight"
    magician = "Magician"
    marauder = "Marauder"
    thief = "Thief"
    warrior = "Warrior"


@dataclass
class Alignment:
    name: str
    affirm: int = 0
    deny: int = 0


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
        xp_next = self.level * 10
        return xp_next