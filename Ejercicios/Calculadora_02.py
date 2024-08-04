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

def tema_oscuro(*args):
    estilo.configure('mainframe.TFrame', background='#010924')
    estilo_label1.configure('Label1.TLabel', background='#010924', foreground='white')
    estilo_label2.configure('Label2.TLabel', background='#010924', foreground='white')

    estilo_botones_numeros.configure('Botones_numeros.TButton', background='#00044A', foreground='white')
    estilo_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#020A90')])
    estilo_botones_borrar.configure('Botones_borrar.TButton', background='#010924', foreground='white')
    estilo_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#000AB1')])
    estilo_botones_restantes.configure('Botones_restantes.TButton', background='#010924', foreground='white')
    estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#000AB1')])

def tema_claro(*args):
    estilo.configure('mainframe.TFrame', background='#DBDBDB', foreground='black')
    estilo_label1.configure('Label1.TLabel', background='#DBDBDB', foreground='black')
    estilo_label2.configure('Label2.TLabel', background='#DBDBDB', foreground='black')

    estilo_botones_numeros.configure('Botones_numeros.TButton', background='#FFFFFF', foreground='black')
    estilo_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])
    estilo_botones_borrar.configure('Botones_borrar.TButton', background='#CECECE', foreground='black')
    estilo_botones_borrar.map('Botones_borrar.TButton', background= [('active', '#858585')])
    estilo_botones_restantes.configure('Botones_restantes.TButton', background='#CECECE', foreground='black')
    estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('mainframe.TFrame', background='#DBDBDB')

mainframe = ttk.Frame(ventana, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
# Ajustando la calculadora para que sea responsive
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

estilo_label1 = ttk.Style()
estilo_label1.configure('Label1.TLabel', font="arial 15", anchor="e")
estilo_label2 = ttk.Style()
estilo_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

# -------------------------------------
# Estilos para los botones
# -------------------------------------
estilo_botones_numeros = ttk.Style()
estilo_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilo_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

estilo_botones_borrar = ttk.Style()
estilo_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilo_botones_borrar.map('Botones_borrar.TButton', foreground= [('active', '#FF0000')], background= [('active', '#858585')])

estilo_botones_restantes = ttk.Style()
estilo_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilo_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#858585')])

# -------------------------------------
# Creando los botones
# -------------------------------------
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

# -------------------------------------
# Colocando los botones en el mainframe
# -------------------------------------
button_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_divison.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, columnspan=2, row=6, sticky=(W, N, E, S)) # sticky : Sirve para completar el espacio que sobra por ocupar más de una columna
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))

button_igual.grid(column=0, columnspan=3, row=7, sticky=(W, N, E, S))
button_raiz.grid(column=3, row=7, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

ventana.bind('<KeyPress-o>', tema_oscuro)
ventana.bind('<KeyPress-c>', tema_claro)

ventana.mainloop()