SLOT_MAPPING = {
    "offhand": Placement.shield,
    "head_slot": Placement.head,
    "chest_slot": Placement.chest,
    "arms_slot": Placement.arms,
    "legs_slot": Placement.legs,
    "outer_slot": Placement.outer,
    "amulet_slot": Placement.amulet,
    "ring_slot": Placement.ring,
    "talisman_slot": Placement.talisman,
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
            if (
                isinstance(slot_value, Armor)
                and slot_value.placement != expected_placement
            ):
                raise ValueError(
                    f"{slot_name} has an error!  {slot_value.placement.value} does not match expected {expected_placement.value}"
                )

        if self.mainhand:
            if self.mainhand.properties == "two-handed" and self.offhand is not None:
                raise ValueError(
                    "Main/Offhand slot error, please double check if you are using a two-handed weapon."
                )


testequip = Equipment(
    mainhand=ssword,
    offhand=buckler,
    head_slot=hat,
    chest_slot=plate,
    arms_slot=gloves,
    legs_slot=greaves,
    outer_slot=lcoat,
    amulet_slot=dummy_amulet,
    ring_slot=dummy_ring,
    talisman_slot=dummy_talisman,
)
