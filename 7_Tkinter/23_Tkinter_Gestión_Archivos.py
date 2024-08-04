### TKINTER ###
## Gestión de archivos
import os
import tkinter as tk
from tkinter import filedialog # Nos permite trabajar y manejar archivos

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[('Archivos de texto' , '*.txt'),('Todos los archivos' , '*.*')])
    if file_path:
        with open(file_path, 'r') as file_obj: # --> Abrir el archivo en modo de lectura
            contenido = file_obj.read() 
            text_widget.delete(1.0, tk.END) # --> Que vaya palabra por palabra, hasta llegar al final
            text_widget.insert(tk.INSERT, contenido) # --> Que vaya insertando, lo que venga guardado en el contenido

def guardar_archivo():
    file_path = filedialog.asksaveasfilename(filetypes=[('Archivos de texto' , '*.txt'),('Todos los archivos' , '*.*')])
    if file_path:
        with open(file_path, 'w') as file_obj: # --> Abrir el archivo en modo de escritura
            contenido = text_widget.get(1.0, tk.END) # --> Que vaya palabra por palabra, hasta llegar al final
            file_obj.write(contenido) # --> Que vaya escribiendo, lo que vaya guardando en el contenido

def crear_archivo():
    file_create = filedialog.asksaveasfile(mode='w', defaultextension='.txt') # --> Crear un archivo nuevo, y que se escriba
    if file_create:
        file_create.write("Hello, world")
        file_create.close()

def seleccionar_directorio():
    dir_path = filedialog.askdirectory()
    if dir_path:
        list_box.delete(0, tk.END)
        for file in os.listdir(dir_path):
            list_box.insert(tk.END, file)

ventana = tk.Tk()
ventana.title("Gestión de archivos")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

# Frame para los botones superiores
frame_botones_sup = tk.Frame(ventana)
frame_botones_sup.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
frame_botones_sup.columnconfigure((0, 1), weight=1)

boton3 = tk.Button(frame_botones_sup, text="Seleccionar Directorio", command=seleccionar_directorio)
boton3.grid(row=0, column=0, sticky="ew", padx=2)

boton = tk.Button(frame_botones_sup, text="Abrir Archivo", command=abrir_archivo)
boton.grid(row=0, column=1, sticky="ew", padx=2)

# Frame principal para la lista y el texto
frame_principal = tk.Frame(ventana)
frame_principal.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
frame_principal.columnconfigure(0, weight=1)
frame_principal.rowconfigure(1, weight=1)

list_box = tk.Listbox(frame_principal)
list_box.grid(row=0, column=0, sticky="nsew")

text_widget = tk.Text(frame_principal, wrap='word')
text_widget.grid(row=1, column=0, sticky="nsew")

# Frame para los botones inferiores
frame_botones_inf = tk.Frame(ventana)
frame_botones_inf.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
frame_botones_inf.columnconfigure((0, 1, 2), weight=1)

boton1 = tk.Button(frame_botones_inf, text="Guardar Archivo", command=guardar_archivo)
boton1.grid(row=0, column=0, sticky="ew", padx=2)

boton2 = tk.Button(frame_botones_inf, text="Crear Archivo", command=crear_archivo)
boton2.grid(row=0, column=2, sticky="ew", padx=2)

'''
file_paths = filedialog.askopenfilename() --> Permite seleccionar un archivo y nos devuelve la dirección
print(file_paths)

file_paths = filedialog.askopenfilenames() --> Permite seleccionar varios archivos y nos devuelve la dirección
print(file_paths)

file_object = filedialog.askopenfile(mode='r') --> Permite abrir, en modo lectuar, un archivo e imprimir
if file_object:
    print(file_object.read())
    file_object.close()
'''

ventana.mainloop()