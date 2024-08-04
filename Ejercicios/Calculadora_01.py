'''
Desarrollar una aplicación de calculadora que permita realizar operaciones aritméticas básicas 
(suma, resta, multiplicación y división) con números enteros y decimales. 
La interfaz debe ser intuitiva y fácil de usar. Incluye funcionalidades adicionales 
como borrar limpiar toda la pantalla y manejar errores comunes como la división por cero.
'''

from tkinter import *

i = 0

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")
ventana.minsize(300,300)
ventana.maxsize(300,300)

# Creando la entrada de la calculadora
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

# Creando botones de la calculadora
boton1 = Button(ventana, text="1", width=5, height=2, command= lambda: click_boton(1))
boton2 = Button(ventana, text="2", width=5, height=2, command= lambda: click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command= lambda: click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command= lambda: click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2, command= lambda: click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2, command= lambda: click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2, command= lambda: click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command= lambda: click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2, command= lambda: click_boton(9))
boton0 = Button(ventana, text="0", width=13, height=2, command= lambda: click_boton(0))  # Cambiado el ancho a 13

boton_borrar = Button(ventana, text="AC", width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(ventana, text="(", width=5, height=2, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=")", width=5, height=2, command= lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width=5, height=2, command= lambda: click_boton("."))

boton_div = Button(ventana, text="/", width=5, height=2, command= lambda: click_boton("/"))
boton_mult = Button(ventana, text="*", width=5, height=2, command= lambda: click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2, command= lambda: click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, command= lambda: click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, command= lambda: operacion())

# Agregando botones en pantalla
# Fila 1
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)
# Fila 2
boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)
# Fila 3
boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_resta.grid(row=3, column=3, padx=5, pady=5)
# Fila 4
boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_suma.grid(row=4, column=3, padx=5, pady=5)
# Fila 5
boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)  # Cambiado para abarcar 2 columnas
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()