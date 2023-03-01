#Interfaz Gráfica con Tkinter para cumplir con las exigencias del usuario
from tkinter import *
raiz=Tk()
miFrame=Frame(raiz, width="600", height="400")
miFrame.pack()

cuadrolabel=Label(miFrame, text="Ferreteria el coloso").grid(row=0, column=2, padx=10, pady=10)
cuadroDNI=Entry(miFrame).grid(row=1, column=1, padx=10, pady=10)
cuadroNombre=Entry(miFrame).grid(row=2, column=1, padx=10, pady=10)
cuadroApellido=Entry(miFrame).grid(row=2, column=3, padx=10, pady=10)
cuadroDireccion=Entry(miFrame).grid(row=3, column=1, padx=10, pady=10)
cuadroTelefono=Entry(miFrame).grid(row=4, column=1, padx=10, pady=10)

DNILabel=Label(miFrame, text="DNI:").grid(row=1, column=0, padx=10, pady=10)
nombreLabel=Label(miFrame, text="Nombre:").grid(row=2, column=0, padx=10, pady=10)
ApellidoLabel=Label(miFrame, text="Apellido:").grid(row=2, column=2, padx=10, pady=10)
DireccLabel=Label(miFrame, text="Dirección:").grid(row=3, column=0, padx=10, pady=10)
TelefLabel=Label(miFrame, text="Telefono:").grid(row=4, column=0, padx=10, pady=10)
BotonEnvio=Button(raiz, text="total").pack()


raiz.mainloop()