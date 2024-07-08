import requests
import time

data_dictionary = {}

def cache():
    # store dictionary in a json file
    pass

def uncache():
    # pull dictionary from json file
    pass


def get_data(type, id):
    url = f"https://pokeapi.co/api/v2/{type}/{id}/"

    if url in data_dictionary: return data_dictionary[url]

    try:  
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting all pokemon data: {e}")
    
    data_dictionary[url] = data 
    time.sleep(0.05) # limit to 20 api calls a second
    return data
