import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def pantalla_inicial():
    global pantalla 
    pantalla=tk.Tk()
    pantalla.attributes('-fullscreen', True)
    pantalla.title("Sistema Electrónico de Votación URC")
    pantalla.iconbitmap("urc_icono_small.ico")

    image=PhotoImage(file="urc_logo.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()
    Label(text="").pack()
    Label(text="").pack()

    Label (text="   Sistema electrónico de votación 2023-2", bg="#9F2241", fg="white", width="300", height="5", font=("Calibri_bold", 25)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(text="Iniciar Proceso de Votación", height="3", width="25", font=("Calibri_bold", 20), command=pantalla_qr).pack()
    Label(text="").pack()

    Label(text="Campero Raúl Isaac   ", font=("Calibri_bold", 17)).pack(anchor=tk.SE)
    Label(text="de la Cruz Hernández Andrea   ", font=("Calibri_bold", 17)).pack(anchor=tk.SE)
    Label(text="Miranda Hernández José Rafael   ", font=("Calibri_bold", 17)).pack(anchor=tk.SE)
    Label(text="Nápoles Romero Manuel   ", font=("Calibri_bold", 17)).pack(anchor=tk.SE)

    pantalla.mainloop()

def validar_usuario(matricula):
    global usuario
    # Conectar a la base de datos de MongoDB
    uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["prototipico_401"]
    coleccion_usuarios = db["padron"]

    matricula = int(matricula)

    # Buscar el usuario en la colección
    usuario = coleccion_usuarios.find_one({"user_id": matricula})
  
    if usuario:
        ha_votado = bool(usuario.get('ha_votado', False))
       
        if ha_votado:
            # Usuario ya ha votado, enviar alerta
            messagebox.showerror(title="Alerta", message="El usuario ya ha votado")
            pantalla_qr.destroy()

        else:
            # Usuario puede votar, mostrar pantalla de datos
            messagebox.showinfo(title="Validación Exitosa", message="Usuario puede votar")
            pantalla_datos()
   
    else:
        return False

def procesar_ingreso(matricula):

    if validar_usuario(matricula):
        messagebox.showinfo(title="Validación Exitosa", message="Usuario registrado en el sistema. Puede votar")
        pantalla_datos()

    else:
        messagebox.showerror(title="Validación errónea", message="Usuario no registrado en el sistema\n---------\nAclarar datos con monitor de casilla")

def pantalla_qr():
    
    global pantalla2 
    pantalla2 = Toplevel(pantalla)
    pantalla2.attributes('-fullscreen', True)
    pantalla2.title("Sistema Electrónico de Votación URC")
    pantalla2.iconbitmap("urc_icono_small.ico")

    Label(pantalla2, text="Escanea tu codigo QR o ingresa mediante matricula", bg="#9F2241", fg="white", width="300", height="5", font=("Calibri_bold", 25)).pack()
    Label(pantalla2, text="").pack()

    qr_image = PhotoImage(file='qr_scan.png')
    img_label = Label(image=qr_image)

    Label(pantalla2, text="Ingresa matrícula", font=("Calibri_bold", 20)).pack()
    texto_var = StringVar()
    entrada_matricula = Entry(pantalla2, textvariable=texto_var, font=("Calibri", 18))
    entrada_matricula.pack(pady=80, padx=75)
    

    Label(pantalla2, text="Escanear QR", font=("Calibri_bold", 20)).pack(padx=30, anchor=tk.N)
    qr_button = Button(pantalla2, image=qr_image)
    qr_button.pack(padx=300)
    
    img_label = Label(pantalla2, text='')
    img_label.pack(padx=200)

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

    Label(pdatos, text="Valida que tus datos sean correctos", bg="#9F2241", fg="white", width="300", height="5", font=("Calibri_bold", 25)).pack()
    Label(pdatos, text="").pack(pady=30)

    tk.Label(pdatos, text=f"Matrícula: {usuario['user_id']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Primer nombre: {usuario['nombre_1']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w') 
    tk.Label(pdatos, text=f"Segundo nombre: {usuario['nombre_2']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Apellido paterno: {usuario['apellido_1']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Apellido materno: {usuario['apellido_2']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Edad: {usuario['edad']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Estado: {usuario['estado']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')
    tk.Label(pdatos, text=f"Sexo: {usuario['sexo']}", font=("Calibri_bold", 20)).pack(padx=500, anchor='w')

    boton_ir = Button(pdatos, text="Ir a votación", height="2", width="25", font=("Calibri_bold", 20), command=pantalla_candidatos)
    boton_ir.place(x=500, y=650)
  
    #Botón e imagen de regresar a home
    #Button(pdatos, text="Regresar a inicio", command=pantalla_inicial, font=("Calibri_bold", 10)).place(x=30, y=720)

    pdatos.mainloop()

def pantalla_candidatos():

    #Pantalla que enseña a los candidatos de la elección    
    global pcandidatos 
    pcandidatos = Toplevel(pantalla)
    #pcandidatos = tk.Tk()
    pcandidatos.attributes('-fullscreen', True)
    pcandidatos.title("Sistema Electrónico de Votación URC")
    pcandidatos.iconbitmap("urc_icono_small.ico")

    #Cintillo de título de pantalla
    Label(pcandidatos, text="Vota por un candidato", bg="#9F2241", fg="white", width="300", height="5", font=("Calibri_bold", 25)).pack()
    Label(pcandidatos, text="").pack()

    #Logo alianza va x méxico
    vxmx_image = PhotoImage(file='vaxmexico.png')
    vxmx_label = tk.Label(pcandidatos, image=vxmx_image)
    vxmx_label.place(x=103, y=220)

    #Logo mc
    mc_image = PhotoImage(file='mc.png')
    mc_label = tk.Label(pcandidatos, image=mc_image)
    mc_label.place(x=553, y=220)

    #Logo mc
    morena_image = PhotoImage(file='morena.png')
    morena_label = tk.Label(pcandidatos, image=morena_image)
    morena_label.place(x=1003, y=220)

    #Botón e imagen de botón para Xóchitl Gálvez
    xg_image = PhotoImage(file='xg.png')
    xg_label = Label(image=xg_image)
    Label(pcandidatos, text="Bertha Xóchitl\nGálvez Ruíz", font=("Calibri_bold", 20)).place(x=140, y=625)
    xg_button = Button(pcandidatos, image=xg_image, command=voto_xg)
    xg_button.place(x=100, y=360)
    xg_label = Label(pcandidatos, text='')
    xg_label.pack()

    #Botón e imagen de botón para Samuel García
    sg_image = PhotoImage(file='sg.png')
    sg_label = Label(image=sg_image)
    Label(pcandidatos, text="Samuel Alejandro\nGarcía Sepúlveda", font=("Calibri_bold", 20)).place(x=570, y=625)
    sg_button = Button(pcandidatos, image=sg_image, command=voto_sg)
    sg_button.place(x=550, y=360)
    sg_label = Label(pcandidatos, text='')
    sg_label.pack()

    #Botón e imagen de botón para Claudia Sheinbaum   
    cs_image = PhotoImage(file='claudia_sheinbaum.png')
    cs_label = Label(image=cs_image)
    Label(pcandidatos, text="Claudia Sheinbaum\nPardo", font=("Calibri_bold", 20)).place(x=1010, y=625)
    cs_button = Button(pcandidatos, image=cs_image, command=voto_cs)
    cs_button.place(x=1000, y=360)
    cs_label = Label(pcandidatos, text='')
    cs_label.pack()

    #Entrada de texto y botón de registro para otra opción   
    Label(pcandidatos, text="Otro: ", font=("Calibri_bold", 20)).place(x=495, y=755)
    texto_var = StringVar()
    otro_candidato = Entry(pcandidatos, textvariable=texto_var, font=("Calibri", 18))
    otro_candidato.place(x=565, y=760)

    def registrar_otro():
        global otro_cand
        otro_cand = texto_var.get()
        voto_otro(otro_cand)

    enviar_otro_button = Button(pcandidatos, text="Enviar", font=("Calibri_bold", 15), command=registrar_otro)
    enviar_otro_button.place(x=827, y=753)

    pcandidatos.mainloop()

def voto_otro(otro_cand):

    # Obtén el nombre del candidato para el voto
    otro_cand = str(otro_cand)

    # Conéctate a la base de datos de MongoDB
    uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["prototipico_401"]
    coleccion_usuarios = db["padron"]

    # Actualiza el campo 'candidato' para el usuario actual
    filtro = {"user_id": usuario["user_id"]}
    actualizacion = {"$set": {"candidato": otro_cand, "ha_votado": True}}

    # Ejecuta la actualización
    resultado = coleccion_usuarios.update_one(filtro, actualizacion)

    # Verifica si la actualización fue exitosa
    if resultado.modified_count > 0:
        messagebox.showinfo(title="Voto registrado", message=f"Voto registrado con código:\n {usuario['_id']}")
    else:
        messagebox.showinfo(title="", message="Error en el registro de voto")

def voto_xg():

    # Obtén el nombre del candidato para el voto
    candidato = "Xóchitl Gálvez"

    # Conéctate a la base de datos de MongoDB
    uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["prototipico_401"]
    coleccion_usuarios = db["padron"]

    # Actualiza el campo 'candidato' para el usuario actual
    filtro = {"user_id": usuario["user_id"]}
    actualizacion = {"$set": {"candidato": candidato, "ha_votado": True}}

    # Ejecuta la actualización
    resultado = coleccion_usuarios.update_one(filtro, actualizacion)

    # Verifica si la actualización fue exitosa
    if resultado.modified_count > 0:
        messagebox.showinfo(title="", message=f"Voto registrado con código:\n {usuario['_id']}")
    else:
        messagebox.showinfo(title="", message="Error en el registro de voto")

def voto_sg():

    # Obtén el nombre del candidato para el voto
    candidato = "Samuel García"

    # Conéctate a la base de datos de MongoDB
    uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["prototipico_401"]
    coleccion_usuarios = db["padron"]

    # Actualiza el campo 'candidato' para el usuario actual
    filtro = {"user_id": usuario["user_id"]}
    actualizacion = {"$set": {"candidato": candidato, "ha_votado": True}}

    # Ejecuta la actualización
    resultado = coleccion_usuarios.update_one(filtro, actualizacion)

    # Verifica si la actualización fue exitosa
    if resultado.modified_count > 0:
        messagebox.showinfo(title="", message=f"Voto registrado con código:\n {usuario['_id']}")
    else:
        messagebox.showinfo(title="", message="Error en el registro de voto")

def voto_cs():

    # Obtén el nombre del candidato para el voto
    candidato = "Claudia Sheinbaum"

    # Conéctate a la base de datos de MongoDB
    uri = "mongodb+srv://mongo:Antwort5.@cluster0.bluuccs.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["prototipico_401"]
    coleccion_usuarios = db["padron"]

    # Actualiza el campo 'candidato' para el usuario actual
    filtro = {"user_id": usuario["user_id"]}
    actualizacion = {"$set": {"candidato": candidato, "ha_votado": True}}

    # Ejecuta la actualización
    resultado = coleccion_usuarios.update_one(filtro, actualizacion)

    # Verifica si la actualización fue exitosa
    if resultado.modified_count > 0:
        messagebox.showinfo(title="", message=f"Voto registrado con código:\n {usuario['_id']}")
    else:
        messagebox.showinfo(title="", message="Error en el registro de voto")


                                                              
pantalla_inicial()
#pantalla_candidatos()






