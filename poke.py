import requests
import random

trainer_team = []
enemy_team = []

def fetch_all_pokemon():
    base_url = "https://pokeapi.co/api/v2/"
    endpoint = "pokemon"
    url = base_url + endpoint

    all_pokemon = []

    while url:
        try:  
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            pokemon_list = data['results']
            all_pokemon.extend(pokemon_list)

            url = data['next']

        except requests.exceptions.RequestException as e:
            print(f"Error getting all pokemon data: {e}")
            break
    
    return all_pokemon

def init_team(team):
     for x in range(0,6):
        random_pokemon = random.choice(all_pokemon)
        team.append(random_pokemon)

if __name__ == "__main__":
    all_pokemon = fetch_all_pokemon()
    init_team(trainer_team)
    init_team(enemy_team)
    print("This is your team: ")
    for x in trainer_team:
        print(x["name"])
    print("This is the enemy team: ")
    for x in enemy_team:
        print(x["name"])
