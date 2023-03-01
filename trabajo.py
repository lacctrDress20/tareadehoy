#Interfaz Gráfica con Tkinter para cumplir con las exigencias del usuario
from tkinter import *
raiz=Tk()
miFrame=Frame(raiz, width="600", height="400")
miFrame.pack()
#------------------------------------
cuadroDNI=Entry(miFrame)
cuadroDNI.grid(row=0, column=1, padx=10, pady=10)
#------------------------------------
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
#------------------------------------
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=3, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)

cuadroTelefono=Entry(miFrame)
cuadroTelefono.grid(row=2, column=3, padx=10, pady=10)


DNILabel=Label(miFrame, text="DNI:")
DNILabel.grid(row=0, column=0, padx=10, pady=10)
#----------------------------
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx=10, pady=10)
#-----------------------------
ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=2, padx=10, pady=10)

DireccLabel=Label(miFrame, text="Dirección:")
DireccLabel.grid(row=2, column=0, padx=10, pady=10)

TelefLabel=Label(miFrame, text="Telefono:")
TelefLabel.grid(row=2, column=2, padx=10, pady=10)

BotonEnvio=Button(raiz, text="total")
BotonEnvio.pack()

raiz.mainloop()