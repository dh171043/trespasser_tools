@dataclass
class Weapon:
    name: str
    damage_dice: int
    ranges: list[str]
    properties: str
    _effect: Union[str, Callable[[], int]]
    price: int

    @property
    def damage_roll(self) -> int:
        damage_calc = random.randint(1, self.damage_dice)
        return damage_calc

    @property
    def effect(self) -> str:
        if self._effect == "Add 2 weapon dice to your total damage dealt.":
            return str(
                random.randint(1, self.damage_dice)
                + random.randint(1, self.damage_dice)
            )
        elif callable(self._effect):
            return str(self._effect())
        return self._effect

    @effect.setter
    def effect(self, value: Union[str, Callable[[], int]]):
        self._effect = value


baxe = Weapon(
    name="Battle Axe",
    damage_dice=8,
    ranges=["melee"],
    properties="-",
    _effect="Confer **frail 2**.",
    price=75,
)
cweapon = Weapon(
    name="Crude Weapon",
    damage_dice=4,
    ranges=["melee"],
    properties="-",
    _effect="Confer **toppled**.",
    price=0,
)
cudgel = Weapon(
    name="Cudgel",
    damage_dice=6,
    ranges=["melee"],
    properties="-",
    _effect="Confer **toppled**",
    price=10,
)
xbow = Weapon(
    name="Crossbow",
    damage_dice=10,
    ranges=["missile 10"],
    properties="two-handed",
    _effect="Confer **bleeding 4",
    price=75,
)
dagger = Weapon(
    name="Dagger",
    damage_dice=4,
    ranges=["melee", "missile 4"],
    properties="thrown",
    _effect="Add 2 weapon dice to your total damage dealt.",
    price=10,
)
flail = Weapon(
    name="Flail",
    damage_dice=8,
    ranges=["melee"],
    properties="-",
    _effect="Confer **inaccurate 2.",
    price=50,
)
fhand = Weapon(
    name="Free Hand",
    damage_dice=4,
    ranges=["melee", "spell = int + 1", "unarmed"],
    properties="-",
    _effect="-",
    price=0,
)
gaxe = Weapon(
    name="Greataxe",
    damage_dice=10,
    ranges=["melee"],
    properties="two-handed",
    _effect="Confer **frail 2**.",
    price=150,
)
gsword = Weapon(
    name="Greatsword",
    damage_dice=10,
    ranges=["melee"],
    properties="two-handed",
    _effect="Confer **unguarded 2**.",
    price=200,
)
halberd = Weapon(
    name="Halberd",
    damage_dice=8,
    ranges=["melee 2"],
    properties="two-handed",
    _effect="**Sweep 1**. Confer **toppled**.",
    price=75,
)
hatchet = Weapon(
    name="hatchet",
    damage_dice=6,
    ranges=["melee", "missile 4"],
    properties="thrown",
    _effect="Confer **frail 2**.",
    price=10,
)
lbow = Weapon(
    name="Longbow",
    damage_dice=10,
    ranges=["missile 12"],
    properties="two-handed",
    _effect="Confer **slow 2**.",
    price=200,
)
mace = Weapon(
    name="Mace",
    damage_dice=6,
    ranges=["melee"],
    properties="-",
    _effect="Confer **weak 2**.",
    price=25,
)
maul = Weapon(
    name="Maul",
    damage_dice=10,
    ranges=["melee"],
    properties="two-handed",
    _effect="Confer **inaccurate 2**.",
    price=200,
)
mstar = Weapon(
    name="Morning Star",
    damage_dice=8,
    ranges=["melee"],
    properties="-",
    _effect="Confer **bleeding 4**",
    price=75,
)
pike = Weapon(
    name="Pike",
    damage_dice=8,
    ranges=["melee 2"],
    properties="two-handed",
    _effect="**Push 2**. Confer **toppled**.",
    price=100,
)
rod = Weapon(
    name="Rod",
    damage_dice=6,
    ranges=["melee", "spell 8"],
    properties="-",
    _effect="Confer **weary 2**.",
    price=125,
)
sbow = Weapon(
    name="Short Bow",
    damage_dice=8,
    ranges=["missile 8"],
    properties="two-handed",
    _effect="Confer **slow 2**.",
    price=75,
)
ssword = Weapon(
    name="Short Sword",
    damage_dice=6,
    ranges=["melee"],
    properties="-",
    _effect="Confer **unguarded 2**.",
    price=50,
)
sickle = Weapon(
    name="Sickle",
    damage_dice=6,
    ranges=["melee"],
    properties="-",
    _effect="Confer **bleeding 4**.",
    price=50,
)
sling = Weapon(
    name="Sling",
    damage_dice=4,
    ranges=["missile 8"],
    properties="-",
    _effect="Confer **inaccurate 2**.",
    price=10,
)
scythe = Weapon(
    name="Scythe",
    damage_dice=8,
    ranges=["melee 2"],
    properties="two-handed",
    _effect="Confer **bleeding 4**.",
    price=125,
)
spear = Weapon(
    name="Spear",
    damage_dice=6,
    ranges=["melee 2", "missile 6"],
    properties="thrown",
    _effect="**Push 2**.",
    price=50,
)
staff = Weapon(
    name="Staff",
    damage_dice=6,
    ranges=["melee", "spell 6"],
    properties="two-handed",
    _effect="**Sweep 1**. Confer **toppled**.",
    price=25,
)
sword = Weapon(
    name="Sword",
    damage_dice=8,
    ranges=["melee"],
    properties="-",
    _effect="Confer **unguarded 2**.",
    price=100,
)
torch = Weapon(
    name="Torch",
    damage_dice=6,
    ranges=["melee"],
    properties="-",
    _effect="Confer **burning 1**.",
    price=5,
)
wand = Weapon(
    name="Wand",
    damage_dice=0,
    ranges=["spell 10"],
    properties="-",
    _effect="-",
    price=100,
)
whammer = Weapon(
    name="War Hammer",
    damage_dice=8,
    ranges=["melee"],
    properties="-",
    _effect="Confer **weak 2**.",
    price=50,
)

allweapons = [
    baxe,
    cweapon,
    cudgel,
    xbow,
    dagger,
    flail,
    fhand,
    gaxe,
    gsword,
    halberd,
    hatchet,
    lbow,
    mace,
    maul,
    mstar,
    pike,
    rod,
    sbow,
    ssword,
    sickle,
    sling,
    scythe,
    spear,
    staff,
    sword,
    torch,
    wand,
    whammer,
]