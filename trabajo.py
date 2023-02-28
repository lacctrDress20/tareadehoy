#Interfaz Gráfica con Tkinter para cumplir con las exigencias del usuario
from tkinter import *
raiz=Tk()
raiz.config(bg="PaleTurquoise1")
miFrame=Frame(raiz, width="600", height="400")
miFrame.pack()
miFrame.config(bg="PaleTurquoise1")
cuadroDNI=Entry(miFrame)
cuadroDNI.grid(row=0, column=1, padx=10, pady=10)
cuadroDNI.config(bg="red")
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)


DNILabel=Label(miFrame, text="DNI:")
DNILabel.grid(row=0, column=0, padx=10, pady=10)
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx=10, pady=10)
ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2, column=0, padx=10, pady=10)

raiz.mainloop()