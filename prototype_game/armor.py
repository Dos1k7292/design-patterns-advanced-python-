import copy


class Armor:

    def __init__(self, name, defense):

        self.name = name

        self.defense = defense

    def clone(self):

        return copy.deepcopy(self)
