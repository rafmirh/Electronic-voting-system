from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from itertools import product
import random
import json

nombre = ["Roberto", "José", "Maximiliano", "Raúl", "Karla", "Manuel", "Carlos", "Jared", "Enrique", "Jesús", "Ariana", "Andrea", "América", "Víctor", "Daniel", "Adán", "Rafael", "Isaac", "Sofía", "Ricardo", "Jocelyn", "Monserrath", "Daniela", "Francisco"]
apellido = ["Rodríguez", "Quintero", "Miranda", "Martínez", "Campero", "Casas", "Nápoles", "López", "Guerra", "Valdés", "González", "Pérez", "Hernández", "Flores", "Rincón", "Carmona", "Sánchez", "Hernández", "García", "Espinosa", "Morales", "Romero", "Gordillo", "Rojas", "Ramírez", "de la Cruz", "Espinosa"]
sexo = ["Hombre", "Mujer"]
estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro","Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]
candidatos = ["Caludia Sheinbaum", "Xóchitl Gálvez", "Samuel García", "Ninguno"]
pesos_candidatos = [0.48, 0.24, 0.08, 0.2]
padron = []

# Combinaciones de 4 nombres (2 nombres y 2 apellidos)
for nombre_combinado in product(nombre, repeat=2):
    for apellido_combinado in product(apellido, repeat=2):
        nombre_combinado_1 = {
            'nombre_1': nombre_combinado[0],
            'nombre_2': nombre_combinado[1],
            'apellido_1': apellido_combinado[0],
            'apellido_2': apellido_combinado[1]
        }
        padron.append(nombre_combinado_1)

# Combinaciones de 3 nombres (1 nombre y 2 apellidos)
for n1 in nombre:
    for apellido_comb in product(apellido, repeat=2):
        nombre_combinado_2 = {
            'nombre_1': n1,
            'nombre_2': "",
            'apellido_1': apellido_comb[0],
            'apellido_2': apellido_comb[1]
        }
        padron.append(nombre_combinado_2)

# Se agregan valores aleatorios de sexo, estado y edad para las personas dentro del padron

for matricula, persona in enumerate(padron, start=1):
    persona['user_id'] = matricula

for persona in padron:
    persona['ha_votado'] = False
    persona['sexo'] = random.choice(sexo)
    persona['estado'] = random.choice(estados)
    persona['edad'] = round(random.uniform(18, 80))
    persona['candidato'] = random.choices(candidatos, weights=pesos_candidatos, k=1)[0]


# Imprimir tamaño del padrón
#print(len(padron))

# Imprimir ejemplos
#print(padron[750:755])

#Test de conexión a MongoDB

uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#client.list_database_names()
mydb = client["prototipico_401"]

#print(mydb.list_collection_names())
mycollections = mydb["padron"]

json_string = json.dumps(padron)
#print(json_string)

with open("padron.json", "w") as outfile:
    outfile.write(json_string)

#Leemos el archivo json y lo guardamos en la base de datos de Mongo
# Opening JSON file
with open('padron.json', 'r') as openfile:
     # Reading from json file
    json_object = json.load(openfile)
# print(type(json_object))
json_object

mycollections.insert_many(json_object)

print("Database deployed!!")
