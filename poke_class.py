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
        self.types = poke_data['types']
        self.moves = []

    def __str__(self):
        return f"{self.name} (ID: {self.id})" # format info later
    
    #add getters
    def get_possible_moves(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.id}/"

        try:  
            response = requests.get(url)
            response.raise_for_status()
            poke_data = response.json()
            possible_moves = poke_data.get('moves', [])
            move_names = [move['move']['name'] for move in possible_moves]
            self.moves = random.sample(move_names, min(4, len(move_names)))  #adds 4 or fewer moves to pokemon
            print(self.moves)
        except requests.exceptions.RequestException as e:
            print(f"Error getting possible moves: {e}")

    #add functions

class Move:
    def __init__(self, move_id): # add data as we need it
        self.id
        self.name
        self.type

    def __str__(self):
        return f"{self.name} (ID: {self.id})" # format info later

my_team = generate_team()
for p in my_team:
    print(p)
    p.get_possible_moves()

for key in data.data_dictionary:
    print(key)