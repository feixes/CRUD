import sqlite3
from tkinter import *
from tkinter import messagebox
from sqlite3 import *

root = Tk()

# ------------------------------------ Conexión, creación base de datos


def conectarBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE datos_usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50),
                password VARCHAR(50),
                apellido VARCHAR(50),
                direccion VARCHAR(50),
                comentarios VARCHAR(120)
            )
        ''')

        messagebox.showinfo("BBDD", "Base de datos creado con éxito")
    except:
        messagebox.showwarning("Ojo!", "La base de datos ya existe")


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
# -------------------------------------- Creación del menu
# Creamos cada elemento del menu con las opciones de los desplegables
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectarBBDD)
bbddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Create")
crudMenu.add_command(label="Read")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

# Creamos las etiquetas de cada manu
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------------------------------------- Construcción de campos grid
miFrame = Frame(root)
miFrame.pack()

labelID = Label(miFrame, text="ID:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)

cuadroID = Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

labelPass = Label(miFrame, text="Contraseña:")
labelPass.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

labelApellido = Label(miFrame, text="Apellido:")
labelApellido.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

labelComentario = Label(miFrame, text="Comentarios:")
labelComentario.grid(row=5, column=0, sticky="ne", padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand="scrollVert")

# ---------------------------------- Botones CRUD

# nuevo frame para los botones
frameBotones = Frame(root)
frameBotones.pack()

botonCreate = Button(frameBotones, text="Create")
botonCreate.grid(row=0, column=0, padx=10, pady=10)

botonRead = Button(frameBotones, text="Read")
botonRead.grid(row=0, column=1, padx=10, pady=10)

botonUpdate = Button(frameBotones, text="Update")
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonDelete = Button(frameBotones, text="Delete")
botonDelete.grid(row=0, column=3, padx=10, pady=10)


root.mainloop()
