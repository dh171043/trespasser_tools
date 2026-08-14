def create_record() -> Record:
    """CLI input of Record subclass."""
    print("\n=== Character Record ===")
    player = input("Enter Player Name: ")
    trespasser_name = input("Enter Character Name: ")
    words_to_live_by = input("Enter Words to Live by: ")

    return Record(
        player = player,
        trespasser_name = trespasser_name,
        words_to_live_by = words_to_live_by
    )

def create_past_life(attributes: Attributes, skills: Skills) -> PastLife:
    """CLI input for character past life."""
    print("\n=== PAST LIFE ===")
    past_life = input("Past Life Name: ")
    choice_attributes = [a.value for a in Attributes]
    bonus_attr = get_choice_input("Bonus Attribute", choice_attributes)
    choice_skill = [s.value for s in Skills]
    skill = get_choice_input("Bonus Skill", choice_skill)
    possessions = input("Keepsake: ")

    return PastLife(
        past_life=past_life,
        bonus_attr=bonus_attr,
        skill=skill,
        possessions=possessions
    )
def create_advancement(lineage: Lineage, past_life: PastLife) -> Advancement:
    """Create advancement through user input."""
    print("\n=== ADVANCEMENT ===")
    past_life = create_past_life()
    lineage = human
    level = get_int_input("Character level [1]: ", 1, 9) or 1
    xp_current = 0
    
    # Choose calling
    calling_options = [c.value for c in Calling]
    calling_choice = get_choice_input("Choose your calling:", calling_options)
    calling = list(Calling)[calling_choice]
    
    # Create alignments
    print("\nFirst Alignment:")
    align1_name = input("Name: ")
    align1 = Alignment(name=align1_name)
    
    print("\nSecond Alignment:")
    align2_name = input("Name: ")
    align2 = Alignment(name=align2_name)
    
    return Advancement(
        level=level,
        xp_current=xp_current,
        lineage=lineage,
        past_life=past_life,
        calling=calling,
        alignment1=align1,
        alignment2=align2
    )

def create_attributes(past_life: PastLife, advancement: Advancement) -> Attributes:
    """Directs user to select attributes."""
    print(f"\n=== ATTRIBUTES ===")
    print(f"Assign {7+advancement.level} attribute points. (5+ {advancement.level} + past life)")
    print(f"Your past life attribute is {past_life.bonus_attr}")

    might = get_int_input("Might: ", 0, 5)
    agi = get_int_input("Agility: ", 0, 5)
    int = get_int_input("Intellect: ", 0, 5)
    spirit = get_int_input("Spirit: ", 0, 5)
    skill = 2 + (advancement.level//3)
    skill_die = 6 + 2* (advancement.level//3)
    

    return Attributes(
        might=might,
        agility=agi,
        intellect=int,
        spirit=spirit,
        skill=skill,
        skill_die=skill_die
    )

def create_skills(past_life: PastLife, attributes: Attributes) -> Skills:
    """Directs user to Select Skills"""
    print(f"\n=== SKILLS ===")
    print(f"Your past life skill is {past_life.skill}.")
    print(f"Select {1+attributes.intellect} skills.")
    


    return Skills(
        alchemy=get_bool_input("Alchemy"),
        athletics=get_bool_input("Athletics"),
        crafting=get_bool_input("Crafting"),
        folklore=get_bool_input("Folklore"),
        letters=get_bool_input("Letters"),
        magic=get_bool_input("Magic"),
        nature=get_bool_input("Nature"),
        perception=get_bool_input("Perception"),
        speech=get_bool_input("Speech"),
        stealth=get_bool_input("Stealth"),
        tinkering=get_bool_input("Tinkering")
    )

def create_attrs_skills() -> Attrs_Skills:
    attributes = create_attributes()
    skills = create_skills()
    return Attrs_Skills(
        attributes=attributes,
        skills= skills
    )
def create_chassis(attributes: Attributes, calling: Calling) -> Chassis:
    """Directs user to select a calling and crafts."""


    # Choose crafts
    crafts = []
    craft_options = [c.value for c in calling]
    craft_choice = get_choice_input("Choose your craft:", craft_options)
    craft = list(calling)[craft_choice]
    crafts = crafts.append(craft)
    craft_options = [c.value for c in calling]
    craft_choice = get_choice_input("Choose your craft:", craft_options)
    craft = list(calling)[craft_choice]
    crafts = crafts.append(craft)

    return Chassis(
        crafts=crafts
    )

def select_deeds(chassis: Chassis, crafts: Craft) -> Deed:
    deeds = []
    craft_choice = get_choice_input("Choose your craft:", chassis.crafts)
    deed_options = alldeeds[f"{craft_choice}_deeds"]
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    craft_choice = get_choice_input("Choose your craft:", chassis.crafts)
    deed_options = alldeeds[f"{craft_choice}_deeds"]
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)
    deed_choice = get_choice_input("Choose a deed:", deed_options)
    deeds = deeds.append(deed_choice)

    
def create_health(attributes: Attributes, chassis: Chassis, advancement: Advancement) -> Health:

    max_hp = (5 + attributes.might)*advancement.level + chassis.calling_hp
    current_hp = max_hp
    maximum_endurance = 10 + attributes.spirit
    current_endurance = maximum_endurance
    maximum_recovery_dice = maximum_endurance
    current_recovery_dice = maximum_recovery_dice
    plight1 =empty_plight
    plight2 =empty_plight
    plight3 =empty_plight
    injury1 =empty_injury
    injury2 =empty_injury
    injury3 =empty_injury

    return Health(
        current_hp = current_hp,
        max_hp =max_hp,
        current_recovery_dice =current_recovery_dice,
        maximum_recovery_dice =maximum_recovery_dice,
        current_endurance =current_endurance,
        maximum_endurance=maximum_endurance,
        plight1 =plight1,
        plight2 =plight2,
        plight3 =plight3,
        injury1 =injury1,
        injury2 =injury2,
        injury3 =injury3
    )

def create_combat_stats(attrs_skils: Attrs_Skills)-> Combat_Stats:
    return Combat_Stats(
        attributes= attrs_skils.attributes
    )

def create_equipment():
    print("filler")

def main():
    view_character_model()
    record = create_record()
    attrs_skills = create_attrs_skills()
    advancement = create_advancement ()
    chassis = create_chassis()
    health_healing = create_health()
    combat_stats = create_combat_stats()
    equipment = create_equipment()
    return Character(
        record=record,
        attributes_skills=attrs_skills,
        advancement=advancement,
        chassis=chassis,
        health_healing=health_healing,
        combat_stats=combat_stats,
        equipment=equipment
    )


if __name__ == "__main__":
    test_character = main()
    print(test_character)