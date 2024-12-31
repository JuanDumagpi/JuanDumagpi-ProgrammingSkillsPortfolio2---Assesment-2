"""
Pokedex API
"""

from tkinter import *
import requests

apiURL = "https://pokeapi.co/api/v2/"


def getInfo(name):
    url = f"{apiURL}/pokemon/{name}"
    response = requests.get(url)
    pokemon_data = response.json()
    return pokemon_data
    if response.status_code == 200:
        print("API connected!")
        pokemon_data = response.json()
    else :
        print("Couldn't connect to the API, please check your connection.")

pokemon_name = "minccino"
pokemon_info = getInfo(pokemon_name)
abilities = [ability_info["ability"]["name"] for ability_info in pokemon_info["abilities"]]
typing = [type_info["type"]["name"] for type_info in pokemon_info["types"]]
weightKG = pokemon_info["weight"] / 10
heightCM = pokemon_info["height"] * 10

if pokemon_info:
    print(f"{pokemon_info["id"]}")
    
    print(f"{pokemon_info["name"]}".capitalize())
    
    print(heightCM, "cm")
    
    print(weightKG, "kg")
    
    #prints types
    if len(typing) == 2:
        print(f"{typing[0].capitalize()} / {typing[1].capitalize()}")
    else:
        print(typing[0].capitalize())
    
    #prints abilities, if there is a 3rd ability it will try to print it but will pass if not
    print(abilities[0].capitalize())    
    print(abilities[1].capitalize())
    try:
        print(abilities[2].capitalize())
    except:
        pass