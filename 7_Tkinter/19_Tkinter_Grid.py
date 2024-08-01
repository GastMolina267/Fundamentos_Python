### TKINTER ###
## Grid
import tkinter
# El grid es la forma de disposición de los diversos widgets en la ventana

ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.minsize(400,300)

boton = tkinter.Button(ventana, text="Boton", width=10, height=5)
boton1 = tkinter.Button(ventana, text="Boton1", width=10, height=5)
boton2 = tkinter.Button(ventana, text="Boton2", width=10, height=5)
boton3 = tkinter.Button(ventana, text="Boton3", width=10, height=5)
boton4 = tkinter.Button(ventana, text="Boton4", width=10, height=5)
# El posicionamiento de los widgets en la ventana va por filas y columnas
# Como si se tratase de Batalla Naval o del Ajedrez
boton.grid(row=0, column=0) 
boton1.grid(row=1, column=1)
boton2.grid(row=2, column=2)
boton3.grid(row=0, column=2)
boton4.grid(row=2, column=0)

ventana.mainloop()