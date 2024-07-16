import requests
import time
import json

def get_data(type, id):
    url = f"https://pokeapi.co/api/v2/{type}/{id}/"

    try:  
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting all pokemon data: {e}")
    
    time.sleep(0.05) # limit to 20 api calls a second
    return data