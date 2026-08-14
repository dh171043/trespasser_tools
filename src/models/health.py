# ==================== HEALTH AND HEALING ====================

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