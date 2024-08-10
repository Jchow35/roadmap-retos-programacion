'''

Funciones definidas por el usuario
'''

# Función Simple


def greet():

    print("Hola, Python!")


greet()

greet()

def saludo():
    print("Hola juan")

def suma():
    print(20 + 10) 

saludo()
saludo()
suma()

# Con retorno

'''
Definición de la función
def return_greet():

La palabra clave def se usa para definir una función.
return_greet es el nombre de la función.
() indica que la función no toma argumentos (parámetros).

return "Hola, Python!":

Dentro de la función, se usa la palabra clave return para especificar el valor que la función devolverá cuando sea llamada.
En este caso, la función devuelve la cadena "Hola, Python!".

Llamada e impresión de la función

greet = return_greet():

Esta línea llama a la función return_greet().
La función se ejecuta y devuelve la cadena "Hola, Python!".
Este valor se asigna a la variable greet.
print(greet):

Esta línea imprime el valor de la variable greet en la consola.
Como greet contiene la cadena "Hola, Python!", eso es lo que se imprimirá.
'''

def return_greet():
    return "Hola, Python!"

greet = return_greet()
print(greet)

def devolver_nombre():
    return "Juan Carlo Molina"

nombre = devolver_nombre()
print(nombre)

def devolver_suma():
    return 5 + 32

suma = devolver_suma()
print(suma)    

# Función con un argumento

def arg_greet(name):
    print(f"hola; {name}!")

arg_greet("Juan")

# Función con argumentos
def arg_welcome(name, lastname):
    print(f"Bienvenido, {name} {lastname}!")

arg_welcome("Juan", "Molina")

def arg_datos_demograficos(sexo, edad, nacionalidad):
    print(f"Datos demograficos: Sexo: {sexo}, Edad: {edad}, nacionalidad: {nacionalidad}")

arg_datos_demograficos("Masculino", 37, "Nicaraguense")

# Con un argumento predeterminado

# Ejemplo 1
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Juan")
default_arg_greet()

# Ejemplo 2

def arg_welcome(name, lastname):
    print(f"Bienvenido, {name} {lastname}!") 

arg_welcome(lastname="Molina", name="Juan")

# Función con argumento y retorno 

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Juan"))

print(return_args_greet(name= "juan", greet= "Hi"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

print(f"{greet}, {name}!")

# Con un número variable de argumentos 

'''
El código define una función llamada variable_arg_greet 
que acepta un número variable de argumentos y luego los usa
en un bucle para imprimir un saludo personalizado para cada uno de ellos.
'''
# Ejemplo 1
def variable_arg_greet(*names):
        for name in names:
            print(f"Hola, {name}!")
    
variable_arg_greet("Python", "Juan", "Carlos", "Comunidad")

# Ejemplo 2
def variable_arg_numbers(*numbers):
    for number in numbers:
        print(number + 1)

variable_arg_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Ejemplo 3 

def variable_arg_animales(*animales):
    for animal in animales:
        print(animal)

variable_arg_animales("cerdo", "perro", "vaca", "gallina", "gato", "pollo")

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f" {value} ({key})")

variable_key_arg_greet(
    language="Python",
    name="Juan",
    lastname="Molina",
    alias="jchow",
    age=37
)

# Función dentro de funciones

def outer_funtion():
    def inner_funtion():
        print("Funcion interna: Hola, Python!")
    inner_funtion()

outer_funtion()

# Funciones del lenguaje (built-in)

print(len("MouDerev")) # len muestra el número de espacios
print(type("Juan Carlos")) # type muestra el tipo de dato
print(type(37)) # type muestra el tipo de dato
print("Juan Carlos".upper()) # Muestra una copia del texto en mayuscula

'''
Variables locales y globales
'''














