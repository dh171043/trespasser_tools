import character_model
import chassis
import loadout
import mechanics
import json
from dataclasses import fields

for section in fields(character_model.Character):
    for value in fields(character_model.Character.section):
        print(f"{section}: {value.name}")

