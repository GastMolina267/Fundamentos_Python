### Variables ###

variable_string = "Mi variable de string"
print(variable_string)

variable_int = 5
print(variable_int)

variableInt_a_variableStr = str(variable_int)
print(variableInt_a_variableStr)
print(type(variableInt_a_variableStr))

variable_bool = False
print(variable_bool)

# Concatenación de variables en un print
print(variable_string, variableInt_a_variableStr, variable_bool)
print("Este es el valor de:", variable_bool)

# Algunas funciones del sistema
print(len(variable_string))

bienvenida = "Hola, bienvenido a Python"
print("ola" in bienvenida)

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Oscar", "Meladio", 'Lalo', 35
print("\nMe llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('\n\n¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print("->",(name))
print("->",(age))

print("Una vez mostramos el valor almacenado en las variables 'name' y 'age'",
      "podemos volver a alterar su valor.")

# Cambiamos su tipo
name = 35
age = "Lalo"
print("=>",(name))
print("=>",(age))