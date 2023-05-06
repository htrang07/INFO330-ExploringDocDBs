import sqlite3   
import sys 
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


pika = pokemonColl.find({"name": "Pikachu"})
for p in pika:
    print(p)
