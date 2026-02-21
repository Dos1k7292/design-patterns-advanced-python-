from character import Character
from weapon import Weapon
from armor import Armor
from skill import Skill


warrior = Character("Warrior")

warrior.weapon = Weapon("Sword", 50)

warrior.armor = Armor("Plate", 40)

warrior.skills.append(Skill("Slash"))


clone = warrior.clone()

clone.name = "Super Warrior"

clone.weapon.name = "Magic Sword"


print("Original:")

warrior.show()


print("\nClone:")

clone.show()
