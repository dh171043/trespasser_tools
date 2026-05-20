from dataclasses import dataclass


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





