'''
Desarrollar una aplicación de calculadora que permita realizar operaciones aritméticas básicas 
(suma, resta, multiplicación y división) con números enteros y decimales. 
La interfaz debe ser intuitiva y fácil de usar. Incluye funcionalidades adicionales 
como borrar limpiar toda la pantalla, manejar errores comunes como la división por cero, cálculo de la raíz cuadrada
y, cómo añadido, un modo claro/oscuro
'''
from tkinter import *
from tkinter import ttk
import math

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('mainframe.TFrame', background='#DBDBDB')

mainframe = ttk.Frame(ventana, style="mainframe.TFrame")
mainframe.grid(column=0, row=0)

estilo_label1 = ttk.Style()
estilo_label1.configure('Label1.TLabel', font="arial 15", anchor="e")
estilo_label2 = ttk.Style()
estilo_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

# Estilos para los botones
estilo_botones_numeros = ttk.Style()
estilo_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")

estilo_botones_borrar = ttk.Style()
estilo_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilo_botones_borrar.map('Botones_borrar.TButton', foreground= [('active', '#FF0000')], background= [('active', '#858585')])

estilo_botones_restantes = ttk.Style()
estilo_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")

# Creando los botones
button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton")
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton")
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton")
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton")
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton")
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton")
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton")
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton")
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton")
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton")

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton")
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton")
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton")
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton")
button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton")

button_divison= ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton")
button_multiplicacion= ttk.Button(mainframe, text="*", style="Botones_restantes.TButton")
button_suma= ttk.Button(mainframe, text="+", style="Botones_restantes.TButton")
button_resta= ttk.Button(mainframe, text="-", style="Botones_restantes.TButton")

button_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton")
button_raiz = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton")

# Colocando los botones en el mainframe
button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_divison.grid(column=3, row=3)

button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid(column=0, columnspan=2, row=6, sticky=(W, E)) # sticky : Sirve para completar el espacio que sobra por ocupar más de una columna
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, columnspan=3, row=7, sticky=(W, E))
button_raiz.grid(column=3, row=7)

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

ventana.mainloop()