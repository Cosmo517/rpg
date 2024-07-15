import random

from player.player import Player


class Warrior(Player):
    def __init__(self, name='Adventurer', hp=15, armor_class=10):
        super().__init__(name, hp, armor_class)
        self.weapons = ['Short Sword']
        self.armor = ['Chain Mail']

    def attack(self):
        # Generate a 'hit value'
        to_hit = random.randint(1, 20)
        attack_damage = random.randint(0, 6)
        return to_hit, attack_damage
