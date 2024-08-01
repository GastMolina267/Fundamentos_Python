### TKINTER ###
## Es un módulo integrado que nos permite crear interfaces gráficas
import tkinter # <--- Módulo a importar para utilizar TKinter

ventana = tkinter.Tk() # Nuevo elemento de ventana 
ventana.geometry("400x300") # Redimensionar la ventana a un tamaño predeterminado

etiqueta = tkinter.Label(ventana, text="Hello World", bg="red") # Integrar una etiqueta en la ventana
etiqueta.pack() # Establecerla de manera predeterminada

'etiqueta.pack(side=tkinter.RIGTH)' # Es una forma de establecer el lugar en donde vo la etiqueta
# Dependiendo de en dónde la querramos, declaramos RIGTH, BOTTOM, TOP, LEFT
'etiqueta.pack(fill=tkinter.X, bg="blue")' # Es una forma en la que podemos rellenar el espacio que ocupa la etiqueta
# Dependiendo de en dónde la querramos, declaramos X ó Y

ventana.mainloop() # El método mainloop sirve para mantener abierta la ventana