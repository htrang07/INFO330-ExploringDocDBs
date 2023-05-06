import sqlite3
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

conn = sqlite3.connect('pokemon.sqlite')
cur = conn.cursor()

for row in cur.execute("SELECT name, pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense FROM pokemon").fetchall():
    types = cur.execute("SELECT type1, type2 FROM pokemon_types_view WHERE name=?", (row[0],)).fetchone()
    abi = [ability[0].strip("',") for ability in cur.execute("SELECT name FROM ability AS a LEFT JOIN pokemon_abilities ON id = ability_id WHERE pokemon_id=?", (row[1],)).fetchall()]
    poke = {
        "name": row[0],
        "pokedex_number": row[1],
        "types": [types[0], types[1]],
        "hp": row[2],
        "attack": row[3],
        "defense": row[4],
        "speed": row[5],
        "sp_attack": row[6],
        "sp_defense": row[7],
        "abilities": abi
    }
    pokemonColl.insert_one(poke)

for doc in pokemonColl.find({}):
    print(doc)