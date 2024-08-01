### TKINTER ###
## TextBox
import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

def text():
    new_tex = textBox.get() # Queremos capturar lo escrito en la caja de texto y al momento de clickar el botón, lo mostramos
    etiqueta["text"] = new_tex

textBox = tkinter.Entry(ventana, font="Helvetica 30") # Creando entrada de texto
textBox.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack()

boton = tkinter.Button(ventana, text="Click", command=text)
boton.pack()

ventana.mainloop()