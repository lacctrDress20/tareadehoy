#Interfaz Gráfica con Tkinter para cumplir con las exigencias del usuario
from tkinter import *
raiz=Tk()
miFrame=Frame(raiz, width="700", height="400")
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.place(x=100, y=100)

raiz.mainloop()