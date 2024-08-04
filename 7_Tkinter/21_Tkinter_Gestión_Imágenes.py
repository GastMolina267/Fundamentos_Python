### TKINTER ###
## Gestión de imágenes
import tkinter as tk
# Nos permite trabajar con imágenes más allá de la función que viene integrada con Python
# PIL permite manipular mejor las imágenes y trabajar con archivos jpg
from PIL import Image, ImageTk
'''
pip install Pillow
'''
import os

# Verifica si el archivo de imagen existe en el directorio actual
if not os.path.exists("./Media/apple.png"):
    raise FileNotFoundError("No se encuentra el archivo 'apple.png' en el directorio actual.")

ventana = tk.Tk()
ventana.title("Gestión de Imágenes con Tkinter")
ventana.geometry("400x300")

# Cargar la imagen
imagen = Image.open("./Media/apple.png")
imagen_redimensionada = imagen.resize((50,50)) # Redimensionar la imágen en px
imagen_rotada = imagen_redimensionada.rotate(90) # Rotar la imágen
imagen_tk = ImageTk.PhotoImage(imagen_rotada) # Establecer la imágen

# Crear y mostrar el botón con la imagen
boton = tk.Button(ventana, image=imagen_tk, padx=10, pady=10)
boton.pack()

# Ejecutar la ventana principal de la aplicación
ventana.mainloop()