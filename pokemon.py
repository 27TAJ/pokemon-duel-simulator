import requests
import random
from PIL import Image, ImageTk
from io import BytesIO


#pokemon logic

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
            pokemon_list = data["results"]
            all_pokemon.extend(pokemon_list)

            url = data["next"]

        except requests.exceptions.RequestException as e:
            print(f"Error getting all pokemon data: {e}")
            break
    
        remove_pokemon_arr = ["lurantis-totem", "salazzle-totem", "kommo-o-totem", "araquanid-totem","togedemaru-totem", "pikachu-starter", "eevee-starter", "pikachu-world-cap","zygarde-10", "cramorant-gulping", "cramorant-gorging", "morpeko-hangry","koraidon-limited-build", "koraidon-sprinting-build", "koraidon-swimming-build","koraidon-gliding-build", "miraidon-low-power-mode", "miraidon-drive-mode","miraidon-aquatic-mode", "miraidon-glide-mode"]
    
        all_pokemon = [pokemon for pokemon in all_pokemon if pokemon["name"] not in remove_pokemon_arr]
    return all_pokemon

def get_pokemon_image(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}/"
    
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    sprite_url = data["sprites"]["front_default"]
    image_response = requests.get(sprite_url)
    image_response.raise_for_status()
    image = Image.open(BytesIO(image_response.content))
    return image

def init_team(team):
     for x in range(0,6):
        random_pokemon = random.choice(all_pokemon)
        team.append(random_pokemon)






if __name__ == "__main__":
    all_pokemon = fetch_all_pokemon()
    print("done")
