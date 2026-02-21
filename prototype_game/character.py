import copy


class Character:

    def __init__(self, name):

        self.name = name

        self.health = 100

        self.weapon = None

        self.armor = None

        self.skills = []

    def clone(self):

        return copy.deepcopy(self)

    def show(self):

        print(self.name)

        print("Health:", self.health)

        print("Weapon:", self.weapon.name)

        print("Armor:", self.armor.name)

        print("Skills:", [s.name for s in self.skills])
