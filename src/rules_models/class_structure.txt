from dataclasses import dataclass
from enum import Enum
import random
from typing import Union, Callable

# ==================== CHARACTER RECORD ====================
@dataclass
class Record:
    player: str
    trespasser_name: str
    words_to_live_by: str

# ==================== ATTRIBUTES AND SKILLS ====================
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

# ==================== HEALTH AND HEALING ====================
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
    
# ==================== ADVANCEMENT ====================
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
        xp_next = self.level*10
        return xp_next

test = Advancement(2, 10)

print('xp_next =', test.xp_next)

# ==================== FEATURES AND TALENS ====================
HP = 12

@dataclass
class Craft:
    name: str
    key: str
    feature1: str
    feature1_desc: str
    feature2: str
    feature2_desc: str

blood = Craft(name = 'Blood', key = 'Might', feature1 = 'Blood Manipulation', feature1_desc = 'do cool blood things', feature2 =  'Life Affinity', feature2_desc = 'You gain a spark when doing life magic')

print(blood.name)

@dataclass
class Weapon:
    name: str
    damage: int
    range: list[str]
    properties: str
    effect: str
    price: int

weapon = Weapon(name = 'hatchet', damage=6, range = ['melee', 'missile 4'], properties='thrown', effect='Confer frail 2.', price = 10)

@dataclass
class Deed:
    name: str
    type: str
    target: str
    strength: str
    base: str
    hit: str
    spark: str
    special: str

Incision = Deed(name='Incision', type = 'VERSATILE ATTACK VS. GUARD', target= '1 Creature', strength='Light', base='', hit = f'deal {weapon.damage} damage. Confer bleeding 2.', spark='Confer bleeding 4 instead.', special='')


@dataclass
class Talent:
    name: str
    desc: str

blank_talent = Talent(name = 'Blank Talent', desc = 'Blank Talent')

@dataclass
class Enhancement:
    name: str
    desc: str

blank_enhancement = Enhancement(name = 'Blank Enhancement', desc = 'Blank Enhancement')

@dataclass
class Feature:
    name: str
    description: str

ex_fort = Feature('Expert Fortitude', 'When you take up this calling, your hit points increase by an extra +5. This makes your hit point total at second level equal to 15 + 2 (MIGHT).')
sac_spell = Feature('Sacred Incantations', 'Cast spells')
devo = Feature('Aspect of Devotion', "gain an aspect appropriate to your god")
revelation = Feature('Revelation', 'Gain the revelation special deed and do things with it')


@dataclass
class Chassis:
    features: list[Feature]
    crafts: list[Craft]
    light_deeds: list[Deed]
    heavy_deeds: list[Deed]
    mighty_deeds: list[Deed]
    talents: list[Talent]
    enhancements: list[Enhancement]

cleric = Chassis(features= [ex_fort, sac_spell, devo, revelation], crafts=[blood], light_deeds=[Incision], heavy_deeds=[], mighty_deeds=[], talents=[], enhancements=[])

print(cleric.crafts[0])

# ==================== SPARKS AND SHADOWS ====================
@dataclass
class Sparks:
    canny: bool
    quick: bool
    quiet: bool
    safe: bool
    striking: bool

@dataclass
class Shadows:
    costly: bool
    slow: bool
    loud: bool
    harmful: bool
    daunting: bool

# ==================== EQUIPMENT AND INVENTORY ====================
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

# ==================== EQUIPMENT AND INVENTORY ====================
@dataclass
class Combat_Stats:
    attributes: object
    resolve: int
    state_initiative: int
    state_accuracy: int
    state_guard: int
    state_resist: int
    state_prevail: int
    state_tenacity: int
    state_speed: int
    state_damage_dealt: int
    state_damage_taken: int
    state_health: int
    state_burning: int
    state_bleeding: int
    state_delirious: int
    state_toppled: int
    state_sleeping: int
    state_aiming: bool
    state_covered: bool
    state_flanked: bool
    state_mshadow: bool
    state_pshadow: bool
    


    @property
    def initiative(self):
        return self.attributes.skill + self.attributes.agility + self.state_initiative
    @property
    def accuracy(self):
        return self.attributes.key + self.attributes.skill + self.state_accuracy
    @property
    def guard(self):
        armor_bonus = 0
        for item in testequip:
            if item.ar == True:
                armor_bonus += item.ar
        return self.attributes.agility + armor_bonus + self.state_guard
    @property
    def resist(self):
        return self.attributes.spirit + self.attributes.skill + self.state_resist
    @property
    def prevail(self):
        return self.attributes.intellect + self.attributes.skill + self.state_prevail
    @property
    def tenacity(self):
        return self.attributes.spirit + self.attributes.skill + self.state_tenacity
    @property
    def speed(self):
        armor_weight = 0
        for item in testequip:
            if item.wgt == True:
                if item.wgt == "H":
                    armor_bonus += 1
        move_speed = 5 + self.attributes.agility - armor_weight
        if move_speed<5:
            move_speed = 5
        return move_speed
    @property
    def bleeding(self):
        text_bleed = f"While moving, your wound bleed profusely. You take {self.state_bleeding} damage."
        HP = HP-self.state_bleeding
        return text_bleed
    @property
    def burning(self):
        burn_dmg = 0
        for i in range(min(self.state_burning, 3)):
            burn_dmg += random.randint(1,6)
        text_burn = f"The flames lick your flesh. You take {burn_dmg} damage."
        HP = HP-burn_dmg
        return text_burn
    
    delirious_actions = {
        1: f"ACTION | Fling something at the nearest creature, dealing {random.randint(1, attributes.skill_die)}",
        2: f"ACTION | Hurt yourself, and suffer {random.randint(1, attributes.skill_die)} damage.",
        3: f"ACTION | Stumble {speed//2} squares in direction {random.randint(1,8)}",
        4: "ACTION | Stare blankly and do nothing.",
        5: "No Effect",
        6: "No Effect"
    }

    @property
    def delirious(self, delirious_actions):
        del_numbers = []
        for i in range(min(self.state_delirious, 3)):
            del_numbers.append(random.randint(1,6))
        for i in del_numbers:
            print(delirious_actions[i])
        
    @property
    def toppled(self):
        self.state_accuracy -= 2
        self.state_guard -= 2
        return self.state_accuracy, self.state_guard
    @property
    def sleeping(self):
        return f"Take no turn, and make a prevail at end of the round {random.randint(1, 20)+ self.prevail}"
    @property
    def aiming(self):
        if self.state_aiming == True:
            return "missile ranges are doubled"
    @property
    def covered(self):
        if self.state_covered == True:
            self.guard += 2
            self.resist += 2
            return self.guard, self.resist
    @property
    def flanking(self):
        if self.state_flanked == True:
            self.accuracy += 2
            return self.accuracy
    @property
    def mshadowed(self):
        self.accuracy += 4
        self.guard += 4
        self.resist += 4
        return self.accuracy, self.guard, self.resist
    @property
    def pshadowed(self):
        self.accuracy += 2
        self.guard += 2
        self.resist += 2
        return self.accuracy, self.guard, self.resist
    
    


print(Combat_Stats.initiative)