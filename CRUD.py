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

# ----------------------------- Función salir


def salir_beber_el_rollo_de_siempre():
    valor_salir = messagebox.askquestion(
        "Salir", "Deseas salir de la aplicación?")
    # si yes/no según el botón pulsado

    if valor_salir == "yes":
        root.destroy()


def borrar_campos():
    # no le puedo asignar directamente una cadena vacía (mi_id="") porque son variables de control
    mi_id.set("")
    mi_nombre.set("")
    mi_pass.set("")
    mi_apellido.set("")
    mi_direccion.set("")
    # para el texto, desde el principio 1.0, hasta el final END
    textoComentario.delete(1.0, END)


def crear():
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute(
        f"INSERT INTO datos_usuarios VALUES(NULL,'{mi_nombre.get()}', '{mi_pass.get()}', '{mi_apellido.get()}', '{mi_direccion.get()}', '{textoComentario.get(1.0, END)}')")
    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con éxito")


# ---------------------- Variables de control

mi_id = StringVar()
mi_nombre = StringVar()
mi_pass = StringVar()
mi_apellido = StringVar()
mi_direccion = StringVar()


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
# -------------------------------------- Creación del menu
# Creamos cada elemento del menu con las opciones de los desplegables
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectarBBDD)
bbddMenu.add_command(label="Salir", command=salir_beber_el_rollo_de_siempre)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrar_campos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Create", command=crear)
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

cuadroID = Entry(miFrame, textvariable=mi_id)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=mi_nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

labelPass = Label(miFrame, text="Contraseña:")
labelPass.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=mi_pass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

labelApellido = Label(miFrame, text="Apellido:")
labelApellido.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroApellido = Entry(miFrame, textvariable=mi_apellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=mi_direccion)
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

botonCreate = Button(frameBotones, text="Create", command=crear)
botonCreate.grid(row=0, column=0, padx=10, pady=10)

botonRead = Button(frameBotones, text="Read")
botonRead.grid(row=0, column=1, padx=10, pady=10)

botonUpdate = Button(frameBotones, text="Update")
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonDelete = Button(frameBotones, text="Delete")
botonDelete.grid(row=0, column=3, padx=10, pady=10)


root.mainloop()
