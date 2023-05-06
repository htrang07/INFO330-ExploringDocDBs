from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


pika = pokemonColl.find({"name": "Pikachu"})
for p in pika:
    print(p)

greater_150 = pokemonColl.find({"attack": {"$gt": 150}})
for i in greater_150:
    print(i)

overgrow_abi = pokemonColl.find({"abilities": "Overgrow"})
for o in overgrow_abi:
    print(o)