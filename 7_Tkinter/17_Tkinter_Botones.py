### TKINTER ###
## Botones

import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

def saludo(nombre): # Función que va a ejecutar el botón
    print("Hola " + nombre)

boton = tkinter.Button(ventana, text="Click", padx="50", pady="20", command= lambda : saludo("Observador")) # Creando un nuevo botón y redimensionándolo
# Para que al momento de clickear el botón, responda con alguna función, se emplea el campo de command
# El lambda nos sirve para utilizar funciones que requieran un parámetro
# Aunque también, el lamba sirve para declarar la acción en una misma línea de código si de un simple print se tratase
boton.pack()

ventana.mainloop()