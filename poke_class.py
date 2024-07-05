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
        self.types = poke_data['types']
        self.moves = []

    def __str__(self):
        return f"{self.name}\n (ID: {self.id})" # format info later
    
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
    def __init__(self, move_data): # add data as we need it
        self.id
        self.name
        self.type

    def __str__(self):
        return f"{self.name}\n (ID: {self.id})" # format info later

my_team = generate_team()
for p in my_team:
    print(p)
    p.get_possible_moves()