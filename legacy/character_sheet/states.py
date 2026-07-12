from dataclasses import dataclass
from legacy.character_sheet.attributes import test
from legacy.character_sheet.gear import testequip
from legacy.character_sheet.gear import allweapons
from trespasser.character_sheet.features import HP
import random



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