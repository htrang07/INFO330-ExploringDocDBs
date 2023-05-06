import sqlite3   
import sys 
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


overgrow_abi = pokemonColl.find({"abilities": "Overgrow"})
for o in overgrow_abi:
    print(o)