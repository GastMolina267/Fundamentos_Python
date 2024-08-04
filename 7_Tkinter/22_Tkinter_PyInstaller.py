### TKINTER ###
## Empaquetado - PyInstaller

'''
pip install pyinstaller
'''
## Instalar el módulo de PyInstaller


'''
pyinstaller --onefile nombre_del_archivo.py
'''
## Seleccionar el archivo a empaquetar

'''
pyinstaller --onefile --name nombre_del archivo_a_empaquetar nombre_del_archivo.py
'''
## Podemos seleccionar un archivo a empaquetar y cambiarle el nombre

# --onefile significa que lo que vayamos a empaquetar, lo vamos a guardar cómo un único archivo
# --name es para cambiar el nombre una vez se empaqueta
# Podemos usar un archivo main.py principal que importe el verdadero archivo del proyecto

'''
# project.py
import tkinter as tk

class Proyecto():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mi aplicación")

        self.etiqueta = tk.Label(self.ventana, text="Presionar el botón para mostrar msj")
        self.etiqueta.pack(pady=20)

        self.boton = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_mensaje())
        self.boton.pack()
    
    def mostrar_mensaje(self):
        mensaje = "Hello, world!"
        self.etiqueta.config(text=mensaje)

    def iniciar_aplicacion(self):
        self.ventana.mainloop()
'''

'''
# main.py
from 'project' import 'Proyecto'

app = Proyecto()
app.iniciar_aplication()
'''