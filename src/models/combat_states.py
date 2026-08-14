# ==================== COMBAT STATS ====================
@dataclass
class Combat_Stats:
    attributes: Attrs_Skills
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
        return (
            self.attributes.attributes.skill
            + self.attributes.attributes.agility
            + self.state_initiative
        )

    @property
    def accuracy(self):
        return (
            self.attributes.attributes.key
            + self.attributes.attributes.skill
            + self.state_accuracy
        )

    @property
    def guard(self):
        armor_bonus = 0
        for item in self.equipment:
            if item.ar:
                armor_bonus += item.ar
        return self.attributes.attributes.agility + armor_bonus + self.state_guard

    @property
    def resist(self):
        return (
            self.attributes.attributes.spirit
            + self.attributes.attributes.skill
            + self.state_resist
        )

    @property
    def prevail(self):
        return (
            self.attributes.attributes.intellect
            + self.attributes.attributes.skill
            + self.state_prevail
        )

    @property
    def tenacity(self):
        return (
            self.attributes.attributes.spirit
            + self.attributes.attributes.skill
            + self.state_tenacity
        )

    @property
    def speed(self):
        armor_weight = 0
        for item in self.equipment:
            if item.wgt:
                if item.wgt == "H":
                    armor_weight += 1
        move_speed = 5 + self.attributes.attributes.agility - armor_weight
        if move_speed < 5:
            move_speed = 5
        return move_speed

    @property
    def bleeding(self):
        text_bleed = f"While moving, your wound bleed profusely. You take {self.state_bleeding} damage."
        Health.current_hp = Health.current_hp - self.state_bleeding
        return text_bleed

    @property
    def burning(self):
        burn_dmg = 0
        for i in range(min(self.state_burning, 3)):
            burn_dmg += random.randint(1, 6)
        text_burn = f"The flames lick your flesh. You take {burn_dmg} damage."
        Health.current_hp = Health.current_hp - burn_dmg
        return text_burn
    @property
    def delirious_results(self):
        delirious_dmg =random.randint(1, self.attributes.attributes.skill_die)
        delirious_actions = {
            1: f"ACTION | Fling something at the nearest creature, dealing {delirious_dmg} damage.",
            2: f"ACTION | Hurt yourself, and suffer {delirious_dmg} damage.",
            3: f"ACTION | Stumble half {self.speed} squares in direction {random.randint(1,8)}",
            4: "ACTION | Stare blankly and do nothing.",
            5: "No Effect",
            6: "No Effect"
        }
        return delirious_actions
    @property#
    def delirious_roll(self):
        del_numbers = []
        for i in range(min(self.state_delirious, 3)):
            del_numbers.append(random.randint(1, 6))
        for i in del_numbers:
            print(self.delirious_results[i])

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
        if self.state_aiming:
            return "missile ranges are doubled"

    @property
    def covered(self):
        if self.state_covered:
            self.guard += 2
            self.resist += 2
            return self.guard, self.resist

    @property
    def flanking(self):
        if self.state_flanked:
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