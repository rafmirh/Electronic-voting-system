import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


def validar_usuario(matricula):
    global usuario
    # Conectar a la base de datos de MongoDB
    uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    """try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)"""

    db = client["prototipico_401"]
    coleccion_usuarios = db["padron"]

    global consulta_id

    consulta_id = ObjectId(matricula)

    # Buscar el usuario en la colección
    usuario = coleccion_usuarios.find_one({"_id": consulta_id})
    
    if usuario:
        return True
   
    else:
        return False

def procesar_ingreso(consulta_id):

    if validar_usuario(consulta_id):
        messagebox.showinfo(title="Validación Exitosa", message="Registro encontrado en el sistema")
        pantalla_datos()

    else:
        messagebox.showerror(title="Validación errónea", message="Registro no encontrado en el sistema")

def pantalla_consulta():
    
    global pantalla2 
    pantalla2=tk.Tk()
    #pantalla2 = Toplevel(pantalla)
    pantalla2.attributes('-fullscreen', True)
    pantalla2.title("Sistema Electrónico de Votación URC")
    pantalla2.iconbitmap("urc_icono_small.ico")

    Label(pantalla2, text="Consulta tu registro de voto", bg="#9F2241", fg="white", width="300", height="5", font=("Calibri_bold", 25)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Ingresa tu código de votación", font=("Calibri_bold", 20)).pack()
    texto_var = StringVar()
    entrada_matricula = Entry(pantalla2, textvariable=texto_var, font=("Calibri", 18))
    entrada_matricula.pack(pady=80, padx=75)
    
    def procesar():
        global matricula
        matricula = texto_var.get()
        procesar_ingreso(matricula)
    
    Button(pantalla2, text="Validar", command=procesar, font=("Calibri_bold", 20)).place(x=820, y=320)

    pantalla2.mainloop()

def pantalla_datos():
    global pdatos
    pdatos=tk.Tk()
    pdatos.attributes('-fullscreen', True)
    pdatos.title("Sistema Electrónico de Votación URC")
    pdatos.iconbitmap("urc_icono_small.ico")

    Label(pdatos, text="Registro de votación", bg="#9F2241", fg="white", width="300", height="5", font=("Calibri_bold", 25)).pack()
    Label(pdatos, text="").pack(pady=30)

    tk.Label(pdatos, text=f"Registro de voto: {usuario['_id']}", font=("Calibri_bold", 20)).pack(padx=150, anchor='n')

    Label(pdatos, text="").pack()
    Label(pdatos, text="").pack()

    tk.Label(pdatos, text=f"Código de estatus: {usuario['user_id']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Primer nombre: {usuario['nombre_1']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w') 
    tk.Label(pdatos, text=f"Segundo nombre: {usuario['nombre_2']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Apellido paterno: {usuario['apellido_1']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Apellido materno: {usuario['apellido_2']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Edad: {usuario['edad']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Estado: {usuario['estado']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Sexo: {usuario['sexo']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    Label(pdatos, text="").pack()
    Label(pdatos, text="").pack()

    tk.Label(pdatos, text=f"Registro de voto: {usuario['ha_votado']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Elección: {usuario['candidato']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')

    pdatos.mainloop()

pantalla_consulta()
