# A pokemon class that will be use to hold information and actions
# related to the pokemon being imported. This file may be merged with 
# the pokemon file.

import requests
import random

def generate_team():
    num_team = random.sample(range(1,1026), 6) # replace constants w variable names
    final_team = []

    for p in num_team:
        #fetch information for the given pokemon
        url = f"https://pokeapi.co/api/v2/pokemon/{p}/"
        
        try:  
            response = requests.get(url)
            response.raise_for_status()
            poke_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting all pokemon data: {e}")

        #add pokemon object to list
        final_team.append(Pokemon(poke_data))
    return final_team

class Pokemon:
    def __init__(self, poke_data): # add data as we need it
        self.id = poke_data['id']
        self.name = poke_data['name']
        self.types = [type_name['type']['name'] for type_name in poke_data['types']]
        self.moves = self.get_pokemon_moves(poke_data)
        
        self.hp = self.get_base_stat_value(poke_data, "hp")
        self.attack = self.get_base_stat_value(poke_data, "attack")
        self.defense = self.get_base_stat_value(poke_data, "defense")
        self.special_attack = self.get_base_stat_value(poke_data, "special-attack")
        self.special_defense = self.get_base_stat_value(poke_data, "special-defense")
        self.speed = self.get_base_stat_value(poke_data, "speed")

    def get_base_stat_value(self, poke_data, stat_name): # returns base value of specified stat
        return next(stat['base_stat'] for stat in poke_data['stats'] if stat['stat']['name'] == stat_name)
            
    def get_pokemon_moves(self, poke_data):
        moves = []
        possible_moves = poke_data.get('moves', [])
        move_names = [move['move']['name'] for move in possible_moves]
        pokemon_moves = random.sample(move_names, min(4, len(move_names)))
        
        for move in pokemon_moves:
            url = f"https://pokeapi.co/api/v2/move/{move}/"
            try:  
                response = requests.get(url)
                response.raise_for_status()
                move_data = response.json()
                moves.append(Move(move_data))
            except requests.exceptions.RequestException as e:
                print(f"Error getting all move data: {e}")
        return moves

    def __str__(self):
        move_strings = [str(move) for move in self.moves]
    
        return (f"{self.name}" + " " + f"ID: {self.id}\n" + f"Moves:{move_strings}")

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