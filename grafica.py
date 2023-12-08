from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from itertools import product
import random
import json

uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["prototipico_401"]
coleccion_usuarios = db["padron"]

votos_xg = coleccion_usuarios.count_documents({'candidato': 'Xóchitl Gálvez"})
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               