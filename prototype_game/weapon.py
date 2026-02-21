import copy


class Weapon:

    def __init__(self, name, damage):

        self.name = name

        self.damage = damage

    def clone(self):

        return copy.deepcopy(self)
