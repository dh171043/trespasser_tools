@dataclass
class Amulet:
    name: str
    effect: str
    placement: Placement


dummy_amulet = Amulet(name="Dummy Amulet", effect="D", placement=Placement.amulet)


@dataclass
class Ring:
    name: str
    effect: str
    placement: Placement


dummy_ring = Ring(name="Dummy Ring", effect="R", placement=Placement.ring)


@dataclass
class Talisman:
    name: str
    effect: str
    placement: Placement


dummy_talisman = Talisman(
    name="Dummy Talisman", effect="T", placement=Placement.talisman
)