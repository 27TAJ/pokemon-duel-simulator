# A pokemon class that will be use to hold information and actions
# related to the pokemon being imported. This file may be merged with 
# the pokemon file.

import requests
import random
import math
from data import data_dictionary
from data import get_data

def generate_team(): # does not need to be a function in future
    return [Pokemon(id) for id in random.sample(range(1,1026), 6)]
class Pokemon:
    def __init__(self, id): # add data as we need it
        poke_data = get_data("pokemon", id)

        self.id = poke_data['id']
        self.name = poke_data['name']
        self.level = random.randint(75,90)
        self.types = [type_name['type']['name'] for type_name in poke_data['types']]
        self.moves = self.get_pokemon_moves(poke_data)
        
        stats = self.get_base_stats(poke_data)

        self.hp = stats["hp"]
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.special_attack = stats["special-attack"]
        self.special_defense = stats["special-defense"]
        self.speed = stats["speed"]

        '''
        self.hp = self.get_stat_value(poke_data, self.level, "hp")
        self.attack = self.get_stat_value(poke_data, self.level, "attack")
        self.defense = self.get_stat_value(poke_data, self.level, "defense")
        self.special_attack = self.get_stat_value(poke_data, self.level, "special-attack")
        self.special_defense = self.get_stat_value(poke_data, self.level, "special-defense")
        self.speed = self.get_stat_value(poke_data, self.level, "speed")'''
        
        self.nature = self.get_rand_nature()


    def get_rand_nature(self):
        nature_data = get_data("nature", random.randint(1,25))
        
        if nature_data['decreased_stat'] is not None:

            decreased_stat = nature_data['decreased_stat']['name']
            increased_stat = nature_data['increased_stat']['name']
        
            map = {"attack" : self.attack, "defense" : self.defense, "special-attack" : self.special_attack, 
                   "special-defense" : self.special_defense, "speed" : self.speed}

            map[decreased_stat] *= 0.9
            map[increased_stat] *= 1.1

            self.attack = int(map["attack"])
            self.defense = int(map["defense"])
            self.special_attack = int(map["special-attack"])
            self.special_defense = int(map["special-defense"])
            self.speed = int(map["speed"])

        return nature_data['name']

    def get_base_stats(self, poke_data):
        stats_dict = {}
        for stat in poke_data['stats']:
            name = stat['stat']['name']
            base = stat['base_stat']

            if name == "hp":
                base = math.floor(0.01 * (2 * base * self.level) + self.level + 10)
            else:
                base = math.floor(0.01 * (2 * base * self.level) + self.level + 5)

            stats_dict[name] = base

        return stats_dict
        

    '''
    def get_base_stat_value(self, poke_data, stat_name): # returns base value of specified stat
        return next(stat['base_stat'] for stat in poke_data['stats'] if stat['stat']['name'] == stat_name)

    
    def get_stat_value(self, poke_data, level, stat_name):
        base = self.get_base_stat_value(poke_data, stat_name)
        if (stat_name == "hp"):
            return math.floor(0.01 * (2 * base * level) + level + 10)
        else:
            return math.floor(0.01 * (2  *base * level) + level + 5)
    '''
    
    def get_pokemon_moves(self, poke_data):
        moves = []
        possible_moves = poke_data.get('moves', [])
        move_names = [move['move']['name'] for move in possible_moves]
        pokemon_moves = random.sample(move_names, min(4, len(move_names)))
        
        for move in pokemon_moves:
            move_data = get_data("move", move)
            try:  
                moves.append(Move(move_data))
            except requests.exceptions.RequestException as e:
                print(f"Error getting all move data: {e}")
        return moves

    def __str__(self):
        move_strings = [str(move) for move in self.moves]
    
        return (f"{self.name}" + " " + f"LVL: {self.level}" + " " + f"ID: {self.id}\n" + f"Moves:{move_strings}" + 
                f"Nature:{self.nature}\nhp:{self.hp}\nattack:{self.attack}\ndefense:{self.defense}\nspecial-attack:{self.special_attack}\n"
                + f"special-defense:{self.special_defense}\nspeed:{self.speed}\n")

class Move: 
    def __init__(self, move_data):
        self.id = move_data['id']
        self.name = move_data['name']
        self.type = move_data['type']['name']
        self.accuracy = move_data['accuracy']
        self.pp = move_data['pp']
        self.power = move_data['power']

    def __str__(self):
       return f"{self.name}"
        

my_team = generate_team()
for p in my_team:
    print(p)

mew = Pokemon(150)
print(mew)