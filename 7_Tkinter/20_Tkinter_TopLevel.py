### TKINTER ###
## Ventanas TopLevel
from tkinter import *
# TopLevel permite crear una ventana independiente/nueva en el programa

ventana = Tk()
ventana.geometry("500x400")
ventana.title("Ventana Principal")
ventana.minsize(500,400)

# Las declaramos, pero no instanciamos para utilizarlas en otro momentos
ventana_toplevel = None
boton_mostrar = None
boton_eliminar = None

def destruirTopLevel():
    global ventana_toplevel, boton_mostrar, boton_eliminar
    # Declaramos variables globales para poder instanciarse en cualquier contexto
    if ventana_toplevel: # Si existe
        ventana_toplevel.destroy()
        ventana_toplevel = None
    boton_eliminar.grid_remove()
    boton_mostrar.grid()

def mostrarTopLevel():
    global ventana_toplevel, boton_mostrar, boton_eliminar
    # Si no las declaramos en global, no podríamos instanciarlas en este contexto
    if not ventana_toplevel: # Si no existe
        ventana_toplevel = Toplevel(ventana)
        ventana_toplevel.geometry("300x200")
        ventana_toplevel.title("Ventana Secundaria")
        label = Label(ventana_toplevel, text="Ventana_TopLevel")
        label.pack()
        boton_mostrar.grid_remove()
        boton_eliminar.grid()

boton_mostrar = Button(ventana, text="Mostrar", width=10, height=5, command=mostrarTopLevel)
boton_mostrar.grid(row=3, column=1)

boton_eliminar = Button(ventana, text="Eliminar", width=10, height=5, command=destruirTopLevel)
boton_eliminar.grid(row=3, column=2)
boton_eliminar.grid_remove()  # Inicialmente oculto

ventana.mainloop()