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

i = 0

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

def ingresarValores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get()+tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarValoresTeclado(event):
    tecla = event.char

    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get()+tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')
    if tecla == '\r':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
    elif event.keysym == 'BackSpace' or event.keysym == 'Delete':
        borrar(event)

def raizCuadrada():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(event=None):
    valor_actual = entrada2.get()
    if valor_actual:
        nuevo_valor = valor_actual[:-1]
        entrada2.set(nuevo_valor)

def borrarTodo(*args):
    entrada1.set('')
    entrada2.set('')

def calcular_resultado():
    entrada1.set(entrada1.get() + entrada2.get())
    try:
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
    except ZeroDivisionError:
        entrada2.set("Error: División por cero")
    except:
        entrada2.set("Error")
    entrada1.set('')

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('mainframe.TFrame', background='#DBDBDB')

mainframe = ttk.Frame(ventana, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
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
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, anchor="e", style="Label1.TLabel", justify="right")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(N, E, S, W))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, anchor="e",style="Label2.TLabel", justify="right")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(N, E, S, W))

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
button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda:ingresarValores('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda:ingresarValores('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda:ingresarValores('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda:ingresarValores('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda:ingresarValores('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda:ingresarValores('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda:ingresarValores('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda:ingresarValores('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda:ingresarValores('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda:ingresarValores('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrarTodo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda:ingresarValores("("))
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda:ingresarValores(")"))
button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda:ingresarValores("."))

button_divison= ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda:ingresarValores("/"))
button_multiplicacion= ttk.Button(mainframe, text="*", style="Botones_restantes.TButton", command=lambda:ingresarValores("*"))
button_suma= ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda:ingresarValores("+"))
button_resta= ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda:ingresarValores("-"))

button_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda:ingresarValores('='))
button_raiz = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda:raizCuadrada())

# -------------------------------------
# Colocando los botones en el mainframe
# -------------------------------------
button_parentesis1.grid(column=0, row=2, sticky=(N, E, S, W))
button_parentesis2.grid(column=1, row=2, sticky=(N, E, S, W))
button_borrar_todo.grid(column=2, row=2, sticky=(N, E, S, W))
button_borrar.grid(column=3, row=2, sticky=(N, E, S, W))

button7.grid(column=0, row=3, sticky=(N, E, S, W))
button8.grid(column=1, row=3, sticky=(N, E, S, W))
button9.grid(column=2, row=3, sticky=(N, E, S, W))
button_divison.grid(column=3, row=3, sticky=(N, E, S, W))

button4.grid(column=0, row=4, sticky=(N, E, S, W))
button5.grid(column=1, row=4, sticky=(N, E, S, W))
button6.grid(column=2, row=4, sticky=(N, E, S, W))
button_multiplicacion.grid(column=3, row=4, sticky=(N, E, S, W))

button1.grid(column=0, row=5, sticky=(N, E, S, W))
button2.grid(column=1, row=5, sticky=(N, E, S, W))
button3.grid(column=2, row=5, sticky=(N, E, S, W))
button_suma.grid(column=3, row=5, sticky=(N, E, S, W))

button0.grid(column=0, columnspan=2, row=6, sticky=(N, E, S, W)) # sticky : Sirve para completar el espacio que sobra por ocupar más de una columna
button_punto.grid(column=2, row=6, sticky=(N, E, S, W))
button_resta.grid(column=3, row=6, sticky=(N, E, S, W))

button_igual.grid(column=0, columnspan=3, row=7, sticky=(N, E, S, W))
button_raiz.grid(column=3, row=7, sticky=(N, E, S, W))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

ventana.bind('<KeyPress-o>', tema_oscuro)
ventana.bind('<KeyPress-c>', tema_claro)
ventana.bind('<Key>', ingresarValoresTeclado)
ventana.bind('<KeyPress-b>', borrar)
ventana.bind('<KeyPress-c>', borrarTodo)
ventana.bind('<Return>', lambda event: calcular_resultado())
ventana.bind('<BackSpace>', borrar)
ventana.bind('<Delete>', borrar)

ventana.mainloop()