"""
Pokedex API
"""

from tkinter import *
import requests

from PIL import ImageTk, Image #For importing images
from urllib.request import urlopen #For using url to import images


#API Variables------------------------------------------------------
#base URL
apiURL = "https://pokeapi.co/api/v2"

#Takes ONLY the first 151 pokemon from the first generation
namesURL = "https://pokeapi.co/api/v2/pokemon?limit=151&offset=0"

# url = f"{apiURL}/pokemon/{name}"
apiResponse = requests.get(apiURL)
nameResponse = requests.get(namesURL)
pokemon_data = apiResponse.json()
name_data = nameResponse.json()
#-------------------------------------------------------------------

#Functions for getting the info of the pokemon by name------------------------
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
#------------------------------------------------------------------------------


#typing colors-----------------------------------------------------------------\
colors = {"normal":"gray", "fighting":"#ce406a", "flying":"#8fa9de", "poison":"#aa6bc8",
       "ground":"#d97845", "rock":"#c5b78c", "bug":"#91c12f", "ghost":"#5269ad",
       "steel":"#5a8ea2", "fire":"#ff9d55", "water":"#5090d6",
       "grass":"#63bc5a","electric":"#f4d23c","psychic":"#fa7179","ice":"#73cec0",
       "dragon":"#0b6dc3","dark":"#5a5465","fairy":"#ec8fe6"}

#-------------------------------------------------------------------------------

#changes colors to the Pokemon's types-----------------------------------------
primaryColor = colors.get("grass")
secondaryColor = colors.get("poison")
def changeColor():
    global primaryColor
    global secondaryColor
    primaryColor = colors.get(typing[0])
    if len(typing) == 2:
        secondaryColor = colors.get(typing[1])
    else:
        secondaryColor = primaryColor
    extraBorder.configure(highlightbackground=primaryColor)
    labelImage.configure(highlightbackground=secondaryColor)
    infoFrame.configure(highlightbackground=primaryColor)
    labelTyping1.configure(bg=primaryColor)
    listbox.configure(bg=primaryColor, selectbackground=secondaryColor)
    buttonFrame.configure(highlightbackground=primaryColor)
    selectButton.configure(bg=secondaryColor)
    if len(typing) == 2:
        labelTyping2.configure(bg=secondaryColor)
    else:
        labelTyping2.configure(bg="#357EC7")

#------------------------------------------------------------------------------


#Variables for pokemon data-----------------------------------------------------------------
pokemon_name = "bulbasaur"
data = name_data["results"]
pokemon_info = getInfo(pokemon_name)
abilities = [ability_info["ability"]["name"] for ability_info in pokemon_info["abilities"]]
typing = [type_info["type"]["name"] for type_info in pokemon_info["types"]]
weightKG = pokemon_info["weight"] / 10
heightCM = pokemon_info["height"] * 10
pokeName = pokemon_info["name"].capitalize()
pokeHeight = f"{heightCM} cm"
pokeWeight = f"{weightKG} cm"
spriteImg = pokemon_info["sprites"]
spriteURL = spriteImg["front_default"]
#-------------------------------------------------------------------------------------------
    

#Tkinter------------------------------------------------------------------------------------
root = Tk()
root.title("Pokedex - Generation 1")
root.configure(bg="#357EC7")
root.geometry("800x600")

#Makes a listbox of all the pokemon from Generation 1-------------
listbox = Listbox(root, borderwidth=0, bg=primaryColor, selectbackground=secondaryColor, fg="white")
listbox.grid (column=0, row=3, pady=15, padx=15)
nameList = []
for k in data:
    nameList.append(k["name"].capitalize())
for i in nameList:
    listbox.insert("end", i)
#-----------------------------------------------------------------

#Pokemon Image-----------------------------------------------------------------
#Shows the Image of the Pokemon as well as colored borders depicting the type
#Bulbasaur is set as default
extraBorder = Frame(root, highlightthickness=4, highlightbackground=primaryColor)
extraBorder.grid(column=0, row=0, pady=10, padx=15)
pokeImage  = urlopen(spriteURL)
imageData = pokeImage.read()
pokeImage.close()
photo = ImageTk.PhotoImage(data=imageData)
labelImage = Label(extraBorder, image = photo, highlightthickness=4, highlightbackground=secondaryColor)
labelImage.image = photo
labelImage.grid(column=0, row=0)
#------------------------------------------------------------------------------


#Info Labels-------------------------------------------------------------------
infoFrame = Frame (root, padx=15, pady=15, highlightthickness=8, highlightbackground=primaryColor)
infoFrame.grid(column=1, row=0, rowspan=5)

if len(typing) == 2:
    labelTyping1 = Label(root, text=typing[0], fg="white", bg=primaryColor)
    labelTyping2 = Label(root, text=typing[1], fg="white", bg=secondaryColor)
    labelTyping1.grid(column=0, row=1)
    labelTyping2.grid(column=0, row=2, pady=5)
else:
    labelTyping1 = Label(root, text=typint[0])
    labelTyping2 = Label(root, text="")
    labelTyping1.grid(column=0, row=1)
    labelTyping2.grid(column=0, row=2, pady=5)

labelID = Label(infoFrame, text=f"{pokemon_info["id"]}")
labelID.grid(column=0, row=0)

labelName = Label(infoFrame, text=pokeName)
labelName.grid(column=1, row=0)

labelHeight = Label(infoFrame, text="Height")
labelHeight.grid(column=0, row=1)

labelHeightVal = Label(infoFrame, text=pokeHeight)
labelHeightVal.grid(column=1, row=1)

labelWeight = Label(infoFrame, text="Weight")
labelWeight.grid(column=0, row=2)

labelWeightVal = Label(infoFrame, text=pokeWeight)
labelWeightVal.grid(column=1, row=2)

labelAbilities = Label(infoFrame, text="Abilities")
labelAbilities.grid(column=0, row=3, columnspan=2)

labelAV1 = Label(infoFrame, text=abilities[0].capitalize())
labelAV1.grid(column=0, row=4, columnspan=2)

labelAV2 = Label(infoFrame, text=abilities[1].capitalize())
labelAV2.grid(column=0, row=5, columnspan=2)


#Some pokemon don't have a 3rd ability, this will try to print the third ability
#If there is no third ability, it will print ---
try:
    labelAV3 = Label(infoFrame, text=abilities[2].capitalize())
    labelAV3.grid(column=0, row=6, columnspan=2)
except:
    labelAV3 = Label(infoFrame, text="---")
    labelAV3.grid(column=0, row=6, columnspan=2)    

#------------------------------------------------------------------------------

#Pokemon Selector-------------------------------------------------------------

#redefines the variables
def varUpdate():
    global pokemon_info, pokemon_info, abilities, typing, weightKG, heightCM, pokeName, pokeHeight, pokeWeight, spriteImg, spriteURL
    global pokeImage, imageData, photo
    pokemon_info = getInfo(pokemon_name)
    abilities = [ability_info["ability"]["name"] for ability_info in pokemon_info["abilities"]]
    typing = [type_info["type"]["name"] for type_info in pokemon_info["types"]]
    weightKG = pokemon_info["weight"] / 10
    heightCM = pokemon_info["height"] * 10
    pokeName = pokemon_info["name"].capitalize()
    pokeHeight = f"{heightCM} cm"
    pokeWeight = f"{weightKG} cm"
    spriteImg = pokemon_info["sprites"]
    spriteURL = spriteImg["front_default"]
    pokeImage  = urlopen(spriteURL)
    imageData = pokeImage.read()
    pokeImage.close()
    photo = ImageTk.PhotoImage(data=imageData)

#selects a new pokemon, and configures the labels
def changeInfo():
    global pokemon_name
    newPoke = listbox.get(ANCHOR).lower()
    pokemon_name = newPoke
    varUpdate()
    print(pokemon_name)
    labelImage.configure(image=photo)
    changeColor()
    if len(typing) == 2:
        labelTyping1.configure(text=typing[0])
        labelTyping2.configure(text=typing[1])
    else:
        labelTyping1.configure(text=typing[0])
        labelTyping2.configure(text="")
    labelID.configure(text=f"{pokemon_info["id"]}")
    labelName.configure(text=pokeName)
    labelHeightVal.configure(text=pokeHeight)
    labelWeightVal.configure(text=pokeWeight)
    labelAV1.configure(text=abilities[0].capitalize())
    labelAV2.configure(text=abilities[1].capitalize())
    try:
        labelAV3.configure(text=abilities[2].capitalize())
    except:
        labelAV3.configure(text=abilities[2].capitalize())

buttonFrame = LabelFrame(root, highlightthickness=8, highlightbackground=primaryColor)
buttonFrame.grid(column=0, row=5, pady=15, padx=15)        
selectButton = Button (buttonFrame, text = "Select Pokemon", command=changeInfo, bg=secondaryColor, fg="white")
selectButton.pack()
#------------------------------------------------------------------------------


root.mainloop()
#Tkinter------------------------------------------------------------------------------------



# if pokemon_info:
#     print(f"{pokemon_info["id"]}")
    
#     print(f"{pokemon_info["name"]}".capitalize())
    
#     print(heightCM, "cm")
    
#     print(weightKG, "kg")
    
#     #prints types
#     if len(typing) == 2:
#         print(f"{typing[0].capitalize()} / {typing[1].capitalize()}")
#     else:
#         print(typing[0].capitalize())
    
#     #prints abilities, if there is a 3rd ability it will try to print it but will pass if not
#     print(abilities[0].capitalize())    
#     print(abilities[1].capitalize())
#     try:
#         print(abilities[2].capitalize())
#     except:
#         pass
    
