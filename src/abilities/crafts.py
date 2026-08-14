@dataclass
class Craft:
    name: str
    key: str
    craft_hp: int
    feature1: str
    feature1_desc: str
    feature2: str
    feature2_desc: str


# blood
blood = Craft(
    name="Blood",
    key="Might",
    craft_hp=0,
    feature1="Blood Manipulation",
    feature1_desc="do cool blood things",
    feature2="Life Affinity",
    feature2_desc="You gain a spark when doing life magic",
)

# illusion
illusion = Craft(
    name = "Illusion",
    key="Intellect",
    craft_hp=0,
    feature1="Minor Projcetion",
    feature1_desc= "Create small illusions. Detailed ones may require an Intellect | Magic Check.",
    feature2= "Illusion Affinity",
    feature2_desc= "Gain a spark on casting checks when performing rituals and incantations that involves illusions, concealment, or deception."
)

storms = Craft(
    name="Storms",
    key="Agility",
    craft_hp=0,
    feature1="Bellwether",
    feature1_desc= "You know how the weather will change over the next week. Additionally, your party can travel through poor and severe weather at normal speeds.",
    feature2="Weather Affinity",
    feature2_desc="Gain a spark on casting checks when performing rituals and incantations that involves altering the weather or creating a meterological effect."

)
wilds = Craft(
    name="Wilds",
    key="Spirit",
    craft_hp=0,
    feature1="Greenblood",
    feature1_desc= "Collect and extra ingredient when using the forage camp action, even on a failure.",
    feature2= "Wild Affinity",
    feature2_desc= "Gain a spark on casting checks when performing rituals and incantations that involve flora or fauna."
)

wind = Craft(
    name="Wind",
    key="Agility",
    craft_hp=0,
    feature1="Windwarp",
    feature1_desc= "You can create minor magical effects that interact with the element of air. When creating challenging effects use Agility | Magic to determine the effect.",
    feature2= "Air Affinity",
    feature2_desc= "Gain a spark on casting checks when performing rituals and incantations that involve wind or manipulating air in some way."
)

allcrafts = [blood, illusion, storms, wilds, wind]