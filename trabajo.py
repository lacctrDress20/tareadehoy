#Interfaz Gráfica con Tkinter para cumplir con las exigencias del usuario
from tkinter import *
raiz=Tk()
miFrame=Frame(raiz, width="700", height="400")
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=0, column=1, padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, padx=10, pady=10)

raiz.mainloop()