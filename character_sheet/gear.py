from dataclasses import dataclass
import random
from typing import Union, Callable
from enum import Enum

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
        if self._effect == 'Add 2 weapon dice to your total damage dealt.':
            return str(random.randint(1, self.damage_dice) + random.randint(1, self.damage_dice))
        elif callable(self._effect):
            return str(self._effect())
        return self._effect

    @effect.setter
    def effect(self, value: Union[str, Callable[[], int]]):
        self._effect = value

baxe = Weapon(name= 'Battle Axe', damage_dice=8 , ranges=['melee'] , properties='-' , _effect='Confer **frail 2**.' , price=75)
cweapon = Weapon(name='Crude Weapon', damage_dice=4 , ranges=['melee' ], properties='-' , _effect='Confer **toppled**.' , price=0 )
cudgel = Weapon(name= 'Cudgel', damage_dice=6 , ranges= ['melee'], properties='-' , _effect='Confer **toppled**' , price=10)
xbow = Weapon(name= 'Crossbow', damage_dice=10 , ranges=['missile 10'] , properties='two-handed' , _effect='Confer **bleeding 4' , price=75)
dagger = Weapon(name= 'Dagger', damage_dice=4 , ranges=['melee', 'missile 4'], properties= 'thrown', _effect= 'Add 2 weapon dice to your total damage dealt.', price=10)
flail = Weapon(name='Flail', damage_dice=8, ranges=['melee'], properties='-', _effect='Confer **inaccurate 2.',price=50)
fhand = Weapon(name='Free Hand', damage_dice=4, ranges=['melee', 'spell = int + 1', 'unarmed'], properties='-', _effect='-',price=0)
gaxe = Weapon(name='Greataxe', damage_dice=10, ranges=['melee'], properties='two-handed', _effect='Confer **frail 2**.',price=150)
gsword = Weapon(name='Greatsword', damage_dice=10, ranges=['melee'], properties='two-handed', _effect='Confer **unguarded 2**.',price=200)
halberd = Weapon(name='Halberd', damage_dice=8, ranges=['melee 2'], properties='two-handed', _effect='**Sweep 1**. Confer **toppled**.',price=75)
hatchet = Weapon(name = 'hatchet', damage_dice=6, ranges = ['melee', 'missile 4'], properties='thrown', _effect='Confer **frail 2**.', price = 10)
lbow = Weapon(name='Longbow', damage_dice=10, ranges=['missile 12'], properties='two-handed', _effect='Confer **slow 2**.',price=200)
mace = Weapon(name='Mace', damage_dice=6, ranges=['melee'], properties='-', _effect='Confer **weak 2**.',price=25)
maul = Weapon(name='Maul', damage_dice=10, ranges=['melee'], properties='two-handed', _effect='Confer **inaccurate 2**.',price=200)
mstar = Weapon(name='Morning Star', damage_dice=8, ranges=['melee'], properties='-', _effect='Confer **bleeding 4**',price=75)
pike = Weapon(name='Pike', damage_dice=8, ranges=['melee 2'], properties='two-handed', _effect='**Push 2**. Confer **toppled**.',price=100)
rod = Weapon(name='Rod', damage_dice=6, ranges=['melee', 'spell 8'], properties='-', _effect='Confer **weary 2**.',price=125)
sbow = Weapon(name='Short Bow', damage_dice=8, ranges=['missile 8'], properties='two-handed', _effect='Confer **slow 2**.',price=75)
ssword = Weapon(name='Short Sword', damage_dice=6, ranges=['melee'], properties='-', _effect='Confer **unguarded 2**.',price=50)
sickle = Weapon(name='Sickle', damage_dice=6, ranges=['melee'], properties='-', _effect='Confer **bleeding 4**.',price=50)
sling = Weapon(name='Sling', damage_dice=4, ranges=['missile 8'], properties='-', _effect='Confer **inaccurate 2**.',price=10)
scythe = Weapon(name='Scythe', damage_dice=8, ranges=['melee 2'], properties='two-handed', _effect='Confer **bleeding 4**.',price=125)
spear = Weapon(name='Spear', damage_dice=6, ranges=['melee 2', 'missile 6'], properties='thrown', _effect='**Push 2**.',price=50)
staff = Weapon(name='Staff', damage_dice=6, ranges=['melee', 'spell 6'], properties='two-handed', _effect='**Sweep 1**. Confer **toppled**.',price=25)
sword = Weapon(name='Sword', damage_dice=8, ranges=['melee'], properties='-', _effect='Confer **unguarded 2**.',price=100)
torch = Weapon(name='Torch', damage_dice=6, ranges=['melee'], properties='-', _effect='Confer **burning 1**.',price=5)
wand = Weapon(name='Wand', damage_dice=0, ranges=['spell 10'], properties='-', _effect='-',price=100)
whammer = Weapon(name='War Hammer', damage_dice=8, ranges=['melee'], properties='-', _effect='Confer **weak 2**.',price=50)

allweapons = [baxe, cweapon, cudgel, xbow, dagger, flail, fhand, gaxe, gsword, halberd, hatchet, lbow, mace, maul, mstar, pike, rod, sbow, ssword, sickle, sling, scythe, spear, staff, sword, torch, wand, whammer]


class Placement(str, Enum):
    shield = 'Shield'
    head = 'Head'
    chest= 'Chest'
    arms= 'Arms'
    legs= 'Legs'
    outer= 'Outer'
    amulet= 'Amulet'
    ring= 'Ring'
    talisman = 'Talisman'

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

hat = Armor(name = 'Hat',placement=Placement.head,wgt='L', ar=1, ar_dice=6, price=10)
helm = Armor(name='Helm', placement=Placement.head,wgt='L', ar=1, ar_dice=8, price=50,)
ghelm = Armor(name='Great Helm', placement=Placement.head, wgt='H', ar=2, ar_dice=10, price=200)
quilted =Armor(name='Quilted Armor', placement=Placement.chest, wgt='L', ar=1, ar_dice=6, price=50)
leather =Armor(name='Leather Armor', placement=Placement.chest, wgt='L', ar=1, ar_dice=8, price=100)
chain =Armor(name='Chainmail', placement=Placement.chest, wgt='H', ar=2, ar_dice=8, price=200)
plate =Armor(name='Platemail', placement=Placement.chest, wgt='H', ar=3, ar_dice=10, price=300)
gloves =Armor(name='Gloves', placement=Placement.arms, wgt='L', ar=0, ar_dice=6, price=10)
bracers =Armor(name='Bracers', placement=Placement.arms, wgt='L', ar=1, ar_dice=8, price=50)
gauntlets =Armor(name='Gauntlets', placement=Placement.arms, wgt='H', ar=2, ar_dice=10, price=100)
boots =Armor(name='Boots', placement=Placement.legs, wgt='L', ar=0, ar_dice=6, price=10)
hboots =Armor(name='High Boots', placement=Placement.legs, wgt='L', ar=0, ar_dice=8, price=50)
greaves =Armor(name='Greaves', placement=Placement.legs, wgt='H', ar=1, ar_dice=10, price=100)
mantle =Armor(name='Mantle', placement=Placement.outer, wgt='L', ar=0, ar_dice=6, price=10)
cloak =Armor(name='Cloak', placement=Placement.outer, wgt='L', ar=0, ar_dice=8, price=20)
lcoat  =Armor(name='Long Coat', placement=Placement.outer, wgt='H', ar=0, ar_dice=10, price=50)
buckler =Armor(name='Buckler', placement=Placement.shield, wgt='-', ar=0, ar_dice=6, price=10)
rshield =Armor(name='Round Shield', placement=Placement.shield, wgt='-', ar=2, ar_dice=6, price=50)
hshield =Armor(name='Heater Shield', placement=Placement.shield, wgt='-', ar=2, ar_dice=8, price=100)
kshield =Armor(name='Kite Shield', placement=Placement.shield, wgt='-', ar=2, ar_dice=10, price=150)

allarmor = [hat, helm, ghelm, quilted, leather, chain, plate, gloves, bracers, gauntlets, boots, hboots, greaves, mantle, cloak, lcoat, buckler, rshield, hshield, kshield]


@dataclass
class Amulet:
    name: str
    effect: str
    placement: Placement

dummy_amulet = Amulet(name='Dummy Amulet', effect='D', placement=Placement.amulet)

@dataclass
class Ring:
    name: str
    effect: str
    placement: Placement

dummy_ring = Ring(name='Dummy Ring', effect='R', placement=Placement.ring)

@dataclass
class Talisman:
    name: str
    effect: str
    placement: Placement

dummy_talisman = Talisman(name='Dummy Talisman', effect='T', placement=Placement.talisman)


SLOT_MAPPING = {
    'offhand': Placement.shield,
    'head_slot': Placement.head,
    'chest_slot': Placement.chest,
    'arms_slot': Placement.arms,
    'legs_slot': Placement.legs,
    'outer_slot': Placement.outer,
    'amulet_slot': Placement.amulet,
    'ring_slot': Placement.ring,
    'talisman_slot': Placement.talisman
}

@dataclass
class Equipment:
    mainhand: Union[Weapon, None] = None
    offhand: Union[Weapon, Armor, None] = None
    head_slot: Union[Armor, None] = None
    chest_slot: Union[Armor, None] = None
    arms_slot: Union[Armor, None] = None
    legs_slot: Union[Armor, None] = None
    outer_slot: Union[Armor, None] = None
    amulet_slot: Union[Amulet, None] = None
    ring_slot: Union[Ring, None] = None
    talisman_slot: Union[Talisman, None] = None

    def __post_init__(self):
        for slot_name, expected_placement in SLOT_MAPPING.items():
            slot_value = getattr(self, slot_name)
            if isinstance(slot_value, Armor) and slot_value.placement != expected_placement:
                raise ValueError(
                    f'{slot_name} has an error!  {slot_value.placement.value} does not match expected {expected_placement.value}'
                )

        if self.mainhand.properties == 'two-handed' and self.offhand is not None:
            raise ValueError('Main/Offhand slot error, please double check if you are using a two-handed weapon.')

testequip = Equipment(mainhand=ssword, offhand=buckler, head_slot = hat, chest_slot = plate, arms_slot=gloves, legs_slot=greaves, outer_slot=lcoat, amulet_slot=dummy_amulet, ring_slot=dummy_ring, talisman_slot=dummy_talisman)

print(testequip.mainhand.effect, testequip.offhand.name, testequip.head_slot.ar_roll)