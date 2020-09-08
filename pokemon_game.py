import sys
import time
#Trainer class - when user chooses to battle a trainer
class Trainer:
    def __init__(self, name, pokemon, bag, wallet):
        self.name = name
        self.pokemon = pokemon
        self.bag = bag
        self.wallet = wallet

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

#heals pokemon. I need to make sure they do not exceep max HP
    def use_potion(self):
        self.curr_health += 20
        if self.curr_health > self.max_health:
            self.curr_health = self.max_health
        print(f"{self.name} gained " + str(20) + " HP!")
        print(f"{self.name} now has {self.curr_health} HP")


#would like to include type weakness and strength
    def fight_sequence(self, other_pokemon):
        pass

#exploring will allow the user to fight a randomly selected pokemon, who they can choose to catch.
#maybe i can make odds of catching better if opponent pokemon is at lower health
    def explore(self):
        pass

#not sure if I need this method, might be able to use it in the explore method
    def catch_pokemon(self):
        pass

#different pokemon to be used. I will probably try to make a dictionary
pikachu = Pokemon("Pikachu", 1, "Electric", 55, 40, 35, 35, "No")

#The player's trainer should have a name. This will determine that. This will
#also introduce them to professor oak. If I choose to add a pokedex, make sure
#to include in dialogue
player_name = input("Hello there! Welcome to the world of Pokemon!\n"
"My name is Professor Dolittle!\n"
"For now, I'm only here so the game knows what to call you\n"
"So please, tell me, what is your name?:")

the_user = Trainer(player_name, None, None, 95)
print("==================\n"
f"Right! So your name is {the_user.name}!\n"
"It's time to pick your first Pokemon!")
