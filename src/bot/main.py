from dataclasses import fields

import rules_models.class_structure.Character as Character
# from rules_models.class_structure import Character

for f in fields(Character):
    print(f)
