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
        secondaryColor = colors.get(typing[0])
    leftFrame.configure(highlightbackground=primaryColor, bg=secondaryColor)
    labelImage.configure(bg=secondaryColor)
    infoFrame.configure(highlightbackground=primaryColor, bg=secondaryColor)
    infoFrameTop.configure(bg=secondaryColor)
    infoFrameBot.configure(bg=secondaryColor)
    labelTyping1.configure(bg=primaryColor)
    listbox.configure(bg=primaryColor, selectbackground=secondaryColor, highlightbackground=primaryColor)
    buttonFrame.configure(highlightbackground=primaryColor)
    selectButton.configure(bg=secondaryColor)
    labelID.configure(bg=secondaryColor)
    labelName.configure(bg=secondaryColor)
    labelHeight.configure(bg=secondaryColor)
    labelHeightVal.configure(bg=secondaryColor)
    labelWeight.configure(bg=secondaryColor)
    labelWeightVal.configure(bg=secondaryColor)
    labelAbilities.configure(bg=secondaryColor)
    labelAV1.configure(bg=secondaryColor)
    labelAV2.configure(bg=secondaryColor)
    labelAV3.configure(bg=secondaryColor)
    statsFrame.configure(highlightbackground=primaryColor, bg=secondaryColor)
    labelStatHP.configure(bg=secondaryColor)
    labelStatHPVal.configure(bg=secondaryColor)
    labelStatAtk.configure(bg=secondaryColor)
    labelStatAtkVal.configure(bg=secondaryColor)
    labelStatDef.configure(bg=secondaryColor)
    labelStatDefVal.configure(bg=secondaryColor)
    labelStatSpA.configure(bg=secondaryColor)
    labelStatSpAVal.configure(bg=secondaryColor)
    labelStatSpD.configure(bg=secondaryColor)
    labelStatSpDVal.configure(bg=secondaryColor)
    labelStatSpe.configure(bg=secondaryColor)
    labelStatSpeVal.configure(bg=secondaryColor)
    if len(typing) == 2:
        labelTyping2.configure(bg=secondaryColor)
    else:
        labelTyping2.configure(bg=primaryColor)

#------------------------------------------------------------------------------


#Variables for pokemon data-----------------------------------------------------------------
pokemon_name = "bulbasaur"
data = name_data["results"]
pokemon_info = getInfo(pokemon_name)
abilities = [ability_info["ability"]["name"] for ability_info in pokemon_info["abilities"]]
pokeID = pokemon_info["id"]
typing = [type_info["type"]["name"] for type_info in pokemon_info["types"]]
weightKG = pokemon_info["weight"] / 10
heightCM = pokemon_info["height"] * 10
pokeName = pokemon_info["name"].capitalize()
pokeHeight = f"{heightCM} cm"
pokeWeight = f"{weightKG} cm"
spriteImg = pokemon_info["sprites"]
spriteURL = spriteImg["front_default"]
pokeStats = [stat["base_stat"]for stat in pokemon_info["stats"]]
#-------------------------------------------------------------------------------------------
    

#Tkinter------------------------------------------------------------------------------------
root = Tk()
root.title("Pokedex - Generation 1")
root.iconbitmap("pokeball.ico")
root.configure(bg="white")
leftFrame = Frame(root, highlightthickness=8, highlightbackground=primaryColor, bg=secondaryColor)
leftFrame.grid(column=0, row=0, padx=(5, 5), pady=15)

#Makes a listbox of all the pokemon from Generation 1---------------------------------------
listbox = Listbox(root, borderwidth=0, bg=primaryColor, selectbackground=secondaryColor, fg="white", highlightthickness=4, highlightbackground=primaryColor)
listbox.grid (column=0, row=1, padx=15)
nameList = []
for k in data:
    nameList.append(k["name"].capitalize())
for i in nameList:
    listbox.insert("end", i)
#-------------------------------------------------------------------------------------------

#Pokemon Image-----------------------------------------------------------------
#Shows the Image of the Pokemon as well as colored borders depicting the type
#Bulbasaur is set as default
pokeImage  = urlopen(spriteURL)
imageData = pokeImage.read()
pokeImage.close()
photo = ImageTk.PhotoImage(data=imageData)
labelImage = Label(leftFrame, image = photo, bg=secondaryColor)
labelImage.image = photo
labelImage.grid(column=0, row=0, padx=5)
#------------------------------------------------------------------------------


#Info Labels-------------------------------------------------------------------
infoFrame = Frame (root, bg=secondaryColor, highlightthickness=8, highlightbackground=primaryColor)
infoFrame.grid(column=1, row=0, padx=(5, 15), pady=10)

infoFrameTop = Frame (infoFrame, bg=secondaryColor) 
infoFrameTop.grid(column=0, row=0, pady=(0,5))
infoFrameBot = Frame (infoFrame, bg=secondaryColor) 
infoFrameBot.grid(column=0, row=1)

if len(typing) == 2:
    labelTyping1 = Label(leftFrame, text=typing[0], fg="white", bg=primaryColor)
    labelTyping2 = Label(leftFrame, text=typing[1], fg="white", bg=secondaryColor)
    labelTyping1.grid(column=0, row=1)
    labelTyping2.grid(column=0, row=2, pady=5)
else:
    labelTyping1 = Label(leftFrame, text=typing[0])
    labelTyping2 = Label(leftFrame, text="")
    labelTyping1.grid(column=0, row=1)
    labelTyping2.grid(column=0, row=2, pady=5)

labelID = Label(infoFrameTop, text=pokeID, bg=secondaryColor, fg="white")
labelID.grid(column=0, row=0)

labelName = Label(infoFrameTop, text=pokeName, bg=secondaryColor, fg="white")
labelName.grid(column=1, row=0)

labelHeight = Label(infoFrameTop, text="Height", bg=secondaryColor, fg="white")
labelHeight.grid(column=0, row=1)

labelHeightVal = Label(infoFrameTop, text=pokeHeight, bg=secondaryColor, fg="white")
labelHeightVal.grid(column=1, row=1)

labelWeight = Label(infoFrameTop, text="Weight", bg=secondaryColor, fg="white")
labelWeight.grid(column=0, row=2)

labelWeightVal = Label(infoFrameTop, text=pokeWeight, bg=secondaryColor, fg="white")
labelWeightVal.grid(column=1, row=2)

labelAbilities = Label(infoFrameBot, text="Abilities", bg=secondaryColor, fg="white")
labelAbilities.grid(column=0, row=3, columnspan=2)

labelAV1 = Label(infoFrameBot, text=abilities[0].capitalize(), bg=secondaryColor, fg="white")
labelAV1.grid(column=0, row=4, columnspan=2)

labelAV2 = Label(infoFrameBot, text=abilities[1].capitalize(), bg=secondaryColor, fg="white")
labelAV2.grid(column=0, row=5, columnspan=2)


#Some pokemon don't have a 3rd ability, this will try to print the third ability
#If there is no third ability, it will print ---

try:
    if len(abilities) < 3:
        labelAV3 = Label(infoFrameBot, text="", bg=secondaryColor, fg="white")
        labelAV3.grid(column=0, row=6, columnspan=2)  
    else:
        labelAV3 = Label(infoFrameBot, text=abilities[2].capitalize(), bg=secondaryColor, fg="white")
        labelAV3.grid(column=0, row=6, columnspan=2) 
except:
    labelAV3 = Label(infoFrameBot, text="", bg=secondaryColor, fg="white")
    labelAV3.grid(column=0, row=6, columnspan=2)    

#------------------------------------------------------------------------------

#Stats Labels------------------------------------------------------------------
statsFrame = Frame (root, bg=secondaryColor, highlightthickness=8, highlightbackground=primaryColor)
statsFrame.grid(column=1, row=1, padx=(5, 15), pady=10)

labelStatHP = Label(statsFrame, text="HP", bg=secondaryColor, fg="white")
labelStatHP.grid(column=0, row=0, padx=15)
labelStatHPVal = Label(statsFrame, text=pokeStats[0], bg=secondaryColor, fg="white")
labelStatHPVal.grid(column=1, row=0, padx=15)

labelStatAtk = Label(statsFrame, text="Atk", bg=secondaryColor, fg="white")
labelStatAtk.grid(column=0, row=1)
labelStatAtkVal = Label(statsFrame, text=pokeStats[1], bg=secondaryColor, fg="white")
labelStatAtkVal.grid(column=1, row=1)

labelStatDef = Label(statsFrame, text="Def", bg=secondaryColor, fg="white")
labelStatDef.grid(column=0, row=2)
labelStatDefVal = Label(statsFrame, text=pokeStats[2], bg=secondaryColor, fg="white")
labelStatDefVal.grid(column=1, row=2)

labelStatSpA = Label(statsFrame, text="SpA", bg=secondaryColor, fg="white")
labelStatSpA.grid(column=0, row=3)
labelStatSpAVal = Label(statsFrame, text=pokeStats[2], bg=secondaryColor, fg="white")
labelStatSpAVal.grid(column=1, row=3)

labelStatSpD = Label(statsFrame, text="SpD", bg=secondaryColor, fg="white")
labelStatSpD.grid(column=0, row=4)
labelStatSpDVal = Label(statsFrame, text=pokeStats[2], bg=secondaryColor, fg="white")
labelStatSpDVal.grid(column=1, row=4)

labelStatSpe = Label(statsFrame, text="Spe", bg=secondaryColor, fg="white")
labelStatSpe.grid(column=0, row=5)
labelStatSpeVal = Label(statsFrame, text=pokeStats[2], bg=secondaryColor, fg="white")
labelStatSpeVal.grid(column=1, row=5)
#-------------------------------------------------------------------------------


#Pokemon Selector-------------------------------------------------------------

#redefines the variables
def varUpdate():
    global pokemon_info, pokemon_info, abilities, typing, weightKG, heightCM, pokeName, pokeHeight, pokeWeight, spriteImg, spriteURL
    global pokeImage, imageData, photo, pokeID, pokeStats
    pokemon_info = getInfo(pokemon_name)
    abilities = [ability_info["ability"]["name"] for ability_info in pokemon_info["abilities"]]
    typing = [type_info["type"]["name"] for type_info in pokemon_info["types"]]
    pokeID = pokemon_info["id"]
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
    pokeStats = [stat["base_stat"]for stat in pokemon_info["stats"]]

#selects a new pokemon, and configures the labels
def changeInfo():
    global pokemon_name
    newPoke = listbox.get(ANCHOR).lower()
    pokemon_name = newPoke
    varUpdate()
    labelImage.configure(image=photo)
    changeColor()
    if len(typing) == 2:
        labelTyping1.configure(text=typing[0])
        labelTyping2.configure(text=typing[1])
    else:
        labelTyping1.configure(text=typing[0])
        labelTyping2.configure(text="")
    labelID.configure(text=pokeID)
    labelName.configure(text=pokeName)
    labelHeightVal.configure(text=pokeHeight)
    labelWeightVal.configure(text=pokeWeight)
    labelAV1.configure(text=abilities[0].capitalize())
    labelAV2.configure(text=abilities[1].capitalize())
    try:
        labelAV3.configure(text=abilities[2].capitalize())
    except:
        labelAV3.configure(text="".capitalize())
    labelStatHPVal.configure(text=pokeStats[0])
    labelStatAtkValVal.configure(text=pokeStats[1])
    labelStatDefValVal.configure(text=pokeStats[2])
    labelStatSpAValVal.configure(text=pokeStats[3])
    labelStatSpDValVal.configure(text=pokeStats[4])
    labelStatSpeVal.configure(text=pokeStats[5])


#Search box that filters out items based on the typed info---------------------

#Updates the list with the pokemon's names by deleting everything in it
#And appending what is inside a temporary list made with items that contain
#the value in the searchbox

def update(names):
    listbox.delete(0,END)
    for items in names:
        listbox.insert(END, items)

#Checks the searchbox and adds items to the search list for appending with the
#update function
def check(e):
    searched = searchBox.get()
    if searched == "":
        search = nameList
    else: 
        search = []
        for names in nameList:
            if searched.lower() in names.lower():
                search.append(names)
    update(search)
    
searchBox = Entry(root)
searchBox.grid(column=0, row=2, pady=15, padx=15)  

#executes the check function everytime we type in the searchbox
searchBox.bind("<KeyRelease>", check)
#------------------------------------------------------------------------------


#Button selects the Anchor and executes the functions above to update the stats
buttonFrame = LabelFrame(root, highlightthickness=8, highlightbackground=primaryColor)
buttonFrame.grid(column=1, row=2, pady=15, padx=15)        
selectButton = Button (buttonFrame, text = "Select Pokemon", command=changeInfo, bg=secondaryColor, fg="white")
selectButton.pack()
#------------------------------------------------------------------------------

update(nameList)
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
    
