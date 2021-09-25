from tkinter import *
from tkinter import messagebox
from sqlite3 import *

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
# -------------------------------------- Creación del menu
# Creamos cada elemento del menu con las opciones de los desplegables
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar")

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

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

labelID = Label(miFrame, text="ID", width=10, anchor="e")
labelID.grid(row=0, column=0, padx=10, pady=10)

cuadroID = Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

labelNombre = Label(miFrame, text="Nombre", width=10, anchor="e")
labelNombre.grid(row=1, column=0, padx=10, pady=10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

labelPass = Label(miFrame, text="Contraseña", width=10, anchor="e")
labelPass.grid(row=2, column=0, padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

labelApellido = Label(miFrame, text="Apellido", width=10, anchor="e")
labelApellido.grid(row=3, column=0, padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

labelDireccion = Label(miFrame, text="Dirección", width=10, anchor="e")
labelDireccion.grid(row=4, column=0, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

labelComentario = Label(miFrame, text="Comentarios",
                        width=10, height=5, anchor="ne")
labelComentario.grid(row=5, column=0, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand="scrollVert")


root.mainloop()
