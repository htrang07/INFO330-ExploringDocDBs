import random
from pymongo import MongoClient
#ALLOW USERS TO PICK ANY TWO POKEMON RATHER THAN TWO RANDOM POKEMON

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")

    winner = random.randrange(2)
    if winner == 0: print("Battle results: " + pokemon1['name'])
    if winner == 1: print("Battle results: " + pokemon2['name'])

#IMPROVED CODE
def main():
    pokemon_names = []
    for pokemon in pokemonColl.find({}, {"name": 1, "pokedex_number": 1}):
        pokemon_names.append(pokemon['name'] + " (" + str(pokemon['pokedex_number']) + ")")

    print("Choose two Pokemon to battle:")
    for i, name in enumerate(pokemon_names):
        print(str(i+1) + ". " + name)
    choice1 = int(input("Choose Pokemon 1: "))
    choice2 = int(input("Choose Pokemon 2: "))

    pokemon1 = fetch(int(pokemon_names[choice1-1].split("(")[1].split(")")[0]))
    pokemon2 = fetch(int(pokemon_names[choice2-1].split("(")[1].split(")")[0]))

    battle(pokemon1, pokemon2)

main()