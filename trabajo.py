#Interfaz Gráfica con Tkinter para cumplir con las exigencias del usuario
from tkinter import *
raiz=Tk()
raiz.title("Ferreteria el manco")
miFrame=Frame(raiz, width="600", height="400")
miFrame.config(bg="PaleTurquoise1")
miFrame.pack()

cuadroTexto=Label(miFrame, text="Ingrese sus datos").grid(row=0, column=2, padx=10, pady=10)

cuadroDNI=Entry(miFrame).grid(row=1, column=1, padx=10, pady=10)
DNILabel=Label(miFrame, text="DNI:").grid(row=1, column=0, padx=10, pady=10)

cuadroNombre=Entry(miFrame).grid(row=2, column=1, padx=10, pady=10)
nombreLabel=Label(miFrame, text="Nombre:").grid(row=2, column=0, padx=10, pady=10)

cuadroApellido=Entry(miFrame).grid(row=2, column=3, padx=10, pady=10)
ApellidoLabel=Label(miFrame, text="Apellido:").grid(row=2, column=2, padx=10, pady=10)

cuadroDireccion=Entry(miFrame).grid(row=3, column=1, padx=10, pady=10)
DireccLabel=Label(miFrame, text="Dirección:").grid(row=3, column=0, padx=10, pady=10)

cuadroTelefono=Entry(miFrame).grid(row=4, column=1, padx=10, pady=10)
TelefLabel=Label(miFrame, text="Telefono:").grid(row=4, column=0, padx=10, pady=10)

CodigProd=Entry(miFrame).grid(row=7, column=0, padx=10, pady=10)
CodigProd=Entry(miFrame).grid(row=8, column=0, padx=10, pady=10)
CodigProd=Entry(miFrame).grid(row=9, column=0, padx=10, pady=10)
CodigProd=Label(miFrame, text="Cod_Prod").grid(row=5, column=0, padx=10, pady=10)

Descripcion=Label(miFrame, text="Descripción").grid(row=5, column=1, padx=10, pady=10)

Unidad=Label(miFrame, text="Unidad").grid(row=5, column=2, padx=10, pady=10)
Cantidad=Entry(miFrame).grid(row=7, column=3, padx=10, pady=10)
Cantidad=Entry(miFrame).grid(row=8, column=3, padx=10, pady=10)
Cantidad=Entry(miFrame).grid(row=9, column=3, padx=10, pady=10)
Cantidad=Label(miFrame, text="Cantidad").grid(row=5, column=3, padx=10, pady=10)

Precio=Label(miFrame, text="Precio").grid(row=5, column=4, padx=10, pady=10)

Subtotal=Label(miFrame, text="Subtotal").grid(row=5, column=5, padx=10, pady=10)

BotonEnvio=Button(miFrame, text="total")
BotonEnvio.grid(row=9, column=6, padx=10, pady=10)

raiz.mainloop()