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