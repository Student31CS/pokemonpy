import sys
import time
#Trainer class - when user chooses to battle a trainer
class Trainer:
    def __init__(self, name, pokemon, bag, wallet):
        self.name = name
        self.pokemon = []
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
        self.ko = None

#prints pokemon stats to console
    def print_stats(self):
        print(f"{self.name.upper()}:\n"
        f"LVL: {self.level}\n"
        f"ATK: {self.attack}\n"
        f"DEF: {self.defense}\n"
        f"HP: {self.curr_health}")

#determines if pokemon has run out of health or not
    def knocked_out(self):
        if self.curr_health > 0:
            self.ko = False
        elif self.curr_health <= 0:
            self.ko = True


#heals pokemon. I need to make sure they do not exceep max HP
    def use_potion(self):
        if self.ko == False:
            self.curr_health += 20
            if self.curr_health > self.max_health:
                self.curr_health = self.max_health
        print(f"{self.name} gained " + str(20) + " HP!")
        print(f"{self.name} now has {self.curr_health} HP")\

#exploring will allow the user to fight a randomly selected pokemon, who they can choose to catch.
#maybe i can make odds of catching better if opponent pokemon is at lower health
    def explore(self):
        pass

#not sure if I need this method, might be able to use it in the explore method
    def catch_pokemon(self, wild_pokemon):
        pass

#would like to include type weakness and strength
    def fight_sequence(self, pokemon1, pokemon2):
        while pokemon1.ko == False and pokemon2.ko == False:
            print("")

#different pokemon to be used. I will probably try to make a dictionary
#or place in a seperate file. Here for now
#I got each pokemons stats from "https://bulbapedia.bulbagarden.net"

pikachu = Pokemon("Pikachu", 1, "Electric", 55, 30, 35, 35, False)
bulbasaur = Pokemon("Bulbasaur", 1, "Grass", 49, 49, 45, 45, False)
charmander = Pokemon("Charmander", 1, "Fire", 52, 43, 39, 39, False)
squirtle = Pokemon("Squirtle", 1, "Water", 48, 65, 44, 44, False)

pokemon_list = (pikachu, bulbasaur, charmander, squirtle)

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
"It's time to pick your first Pokemon!\n")

time.sleep(2)

first_pick = input("Please type a number to choose your Pokemon:\n"
"1. Pikachu\n"
"2. Bulbasaur\n"
"3. Charmander\n"
"4. Squirtle\n")

if first_pick == "1":
    the_user.pokemon.append(pikachu)
    print("==================\n"
    "You picked Pikachu!\n")
    time.sleep(2)
    pikachu.print_stats()
elif first_pick == "2":
    the_user.pokemon.append(bulbasaur)
    print("==================\n"
    "You picked Bulbasaur!\n")
    time.sleep(2)
    bulbasaur.print_stats()
elif first_pick == "3":
    the_user.pokemon.append(charmander)
    print("==================\n"
    "You picked Charmander!\n")
    time.sleep(2)
    charmander.print_stats()
else:
    the_user.pokemon.append(squirtle)
    print("==================\n"
    "You picked Squirtle!\n")
    time.sleep(2)
    squirtle.print_stats()
