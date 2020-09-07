import sys
import time

class Trainer:
    def __init__(self, name, pokemon, bag):
        self.name = name
        self.pokemon = pokemon
        self.bag = bag

class Pokemon:
    def __init__(self, name, level, type, attack, defense, max_health, curr_health, ko):
        self.name = name
        self.level = level
        self.type = type
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.curr_health = curr_health
        self.ko = ko

    def use_potion(self):
        self.curr_health += 20
        print(f"{self.name} gained " + str(20) + " HP!")
        print(f"{self.name} now has {self.curr_health} HP")

    def catch_pokemon(self):
        pass

    def fight_sequence(self, other_pokemon):
        pass




pikachu = Pokemon("Pikachu", 1, "Electric", 55, 40, 35, 35, "No")
pikachu.use_potion()
