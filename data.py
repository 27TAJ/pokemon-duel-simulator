import requests
import time
import json

data_dictionary = {}

def cache():
    # store dictionary in a json file
    with open('data_dictionary.json', 'w') as json_file:
        json.dump(data_dictionary, json_file)

def uncache():
    # pull dictionary from json file
    with open('data_dictionary.json', 'r') as json_file:
        data_dictionary = json.load(json_file)

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
