### TKINTER ###
## Gestión de archivos
import tkinter as tk
from tkinter import filedialog # Nos permite trabajar y manejar archivos

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[('Archivos de texto' , '*.txt'),('Todos los archivos' , '*.*')])
    if file_path:
        with open(file_path, 'r') as file_obj: # --> Abrir el archivo en modo de lectura
            contenido = file_obj.read() 
            text_widget.delete(1.0, tk.END) # --> Que vaya palabra por palabra, hasta llegar al final
            text_widget.insert(tk.INSERT, contenido) # --> Que vaya insertando, lo que venga guardado en el contenido

ventana = tk.Tk()
ventana.geometry("500x450")
ventana.title("Gestión de archivos")
ventana.minsize(500,450)

text_widget = tk.Text(ventana, wrap='word')
text_widget.pack(expand=True, fill='both')

boton = tk.Button(ventana, text="Abrir Archivo", command=abrir_archivo)
boton.pack()

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