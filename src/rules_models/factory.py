from character_model import(
    Record, Attributes, Skills, Attrs_Skills, Health, Injury, Plight,
    Lineage, PastLife, Calling, Alignment, Advancement, Combat_Stats, Character
)
import chassis
from loadout import Equipment, Placement, allarmor, allweapons
from mechanics import Clock, Shadows, Sparks
import json
import random
from dataclasses import fields

def view_character_model():
    for section in fields(Character):

        field_type = section.type

        try:
            subfields = fields(field_type)
            print(f"\n{section.name}:")
            for value in subfields:
                print(f"  - {value.name}")
        except TypeError:
            print(f"\n{section.name}: {field_type}")

def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Allows an int input to have constraints"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be smaller than {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_bool_input(prompt: str)-> bool:
    """Validates Yes/No from user."""
    while True:
        response = input(f"{prompt} (y/n)").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n','no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def get_choice_input(prompt: str, options: list) -> int:
    """Displays options as a list to allow the user to pick easily"""
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        choice = get_int_input("Enter your choice: ", 1, len(options))
        return choice -1

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

def create_attributes(past_life = PastLife, advancement = Advancement) -> Attributes:
    """Directs user to select attributes."""
    print(f"\n=== ATTRIBUTES ===")
    print("Assign attributes scores (5+ lvl + past life)")
    print(f"Your past life attribute is {PastLife.bonus_attr}")

    might = get_int_input("Might: ", 0, 5)
    agi = get_int_input("Agility: ", 0, 5)
    int = get_int_input("Intellect: ", 0, 5)
    spirit = get_int_input("Spirit: ", 0, 5)
    skill = 2 + (Advancement.level//3)
    skill_die = 6 + 2(Advancement.level//3)
    

    return Attributes(
        might=might,
        agility=agi,
        intellect=int,
        spirit=spirit,
        skill=skill,
        skill_die=skill_die
    )
