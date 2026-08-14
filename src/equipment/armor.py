class Placement(str, Enum):
    shield = "Shield"
    head = "Head"
    chest = "Chest"
    arms = "Arms"
    legs = "Legs"
    outer = "Outer"
    amulet = "Amulet"
    ring = "Ring"
    talisman = "Talisman"


@dataclass
class Armor:
    name: str
    placement: Placement
    wgt: str
    ar: int
    ar_dice: int
    price: int

    @property
    def ar_roll(self) -> int:
        ar_calc = random.randint(1, self.ar_dice)
        return ar_calc


hat = Armor(name="Hat", placement=Placement.head, wgt="L", ar=1, ar_dice=6, price=10)
helm = Armor(
    name="Helm", placement=Placement.head, wgt="L", ar=1, ar_dice=8, price=50,
)
ghelm = Armor(
    name="Great Helm", placement=Placement.head, wgt="H", ar=2, ar_dice=10, price=200
)
quilted = Armor(
    name="Quilted Armor", placement=Placement.chest, wgt="L", ar=1, ar_dice=6, price=50
)
leather = Armor(
    name="Leather Armor", placement=Placement.chest, wgt="L", ar=1, ar_dice=8, price=100
)
chain = Armor(
    name="Chainmail", placement=Placement.chest, wgt="H", ar=2, ar_dice=8, price=200
)
plate = Armor(
    name="Platemail", placement=Placement.chest, wgt="H", ar=3, ar_dice=10, price=300
)
gloves = Armor(
    name="Gloves", placement=Placement.arms, wgt="L", ar=0, ar_dice=6, price=10
)
bracers = Armor(
    name="Bracers", placement=Placement.arms, wgt="L", ar=1, ar_dice=8, price=50
)
gauntlets = Armor(
    name="Gauntlets", placement=Placement.arms, wgt="H", ar=2, ar_dice=10, price=100
)
boots = Armor(
    name="Boots", placement=Placement.legs, wgt="L", ar=0, ar_dice=6, price=10
)
hboots = Armor(
    name="High Boots", placement=Placement.legs, wgt="L", ar=0, ar_dice=8, price=50
)
greaves = Armor(
    name="Greaves", placement=Placement.legs, wgt="H", ar=1, ar_dice=10, price=100
)
mantle = Armor(
    name="Mantle", placement=Placement.outer, wgt="L", ar=0, ar_dice=6, price=10
)
cloak = Armor(
    name="Cloak", placement=Placement.outer, wgt="L", ar=0, ar_dice=8, price=20
)
lcoat = Armor(
    name="Long Coat", placement=Placement.outer, wgt="H", ar=0, ar_dice=10, price=50
)
buckler = Armor(
    name="Buckler", placement=Placement.shield, wgt="-", ar=0, ar_dice=6, price=10
)
rshield = Armor(
    name="Round Shield", placement=Placement.shield, wgt="-", ar=2, ar_dice=6, price=50
)
hshield = Armor(
    name="Heater Shield",
    placement=Placement.shield,
    wgt="-",
    ar=2,
    ar_dice=8,
    price=100,
)
kshield = Armor(
    name="Kite Shield", placement=Placement.shield, wgt="-", ar=2, ar_dice=10, price=150
)

allarmor = [
    hat,
    helm,
    ghelm,
    quilted,
    leather,
    chain,
    plate,
    gloves,
    bracers,
    gauntlets,
    boots,
    hboots,
    greaves,
    mantle,
    cloak,
    lcoat,
    buckler,
    rshield,
    hshield,
    kshield,
]