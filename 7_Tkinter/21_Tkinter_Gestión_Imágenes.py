### TKINTER ###
## Gestión de archivos
import tkinter as tk
# Nos permite trabajar con imágenes
from PIL import Image, ImageTk

ventana = tk.Tk()
etiqueta = tk.Label(ventana)

imagen = Image.open("apple.png")
imagen_tk = ImageTk.PhotoImage(imagen)

boton = tk.Button(ventana, image=imagen_tk)
boton.pack()

ventana.mainloop()