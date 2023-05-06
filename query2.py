import sqlite3   
import sys 
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


greater_150 = pokemonColl.find({"attack": {"$gt": 150}})
for i in greater_150:
    print(i)
