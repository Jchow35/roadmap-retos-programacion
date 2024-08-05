"""
Operadores
"""

# Operadores Aritméticos

# Se usa f para interpolar texto y luego se usa {} para realizar la operación aritmética
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 //3 = {10 // 3}")

# Interpolación con una cadena de texto y una variable
sum = 10 + 3
print(f"Suma 10 + 3 = {sum}")

# Operadores de comparación
print(f"Igualdad 10 == 3 {10 == 3}")
print(f"Desigualdad 10 != 3 {10 != 3}")
print(f"Mayor que 10 > 3 {10 > 3}")
print(f"Menor que 10 < 3 {10 < 3}")
print(f"Mayor o igual que 10 >= 3 {10 >= 10}")
print(f"Menor o igual que 10 <= 3 {10 <= 3}")

# Operadores Lógicos
print(f"AND && : 10 + 3 = 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 = 13 and 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 11 # Asignación
print(my_number)
my_number += 1 # Suma y asignación
print(my_number) 
my_number -= 1 # Resta y asignación
print(my_number) 
my_number *= 2 # Multiplicación y asignación
print(my_number) 
my_number /= 2 # División y asignación
print(my_number) 
my_number %= 2 # Módulo y asignación
print(my_number) 
my_number **= 2 # Exponente y asignación
print(my_number)
my_number //= 1 # División entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_new_number is my_number es {my_new_number is my_number}")
print(f"my_new_number is not my_number es {my_new_number is not my_number}")

# Operadores de pertenencia
print(f"'u' in 'Juan' = {'u' in 'juan'}")
print(f"'b' not in 'Carlos' = {'b' not in 'Carlos'}")

# Operadores con bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3  {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

'''
Operadores de control
'''

# Condicionales

# Ejemplo 1
my_string = "MoureDev"

if my_string == "MoureDev":
    print("my_string es 'MoureDev'")
else:
        print("my_string no es 'MoureDev")

# Ejemplo 2
my_string = "Brais"

if my_string == "MoureDev":
    print("my_string es 'MoureDev'")
elif my_string == "Brais":
    print("my_string es 'Brais")
else:
        print("my_string no es 'MoureDev")

# Iterativas
'''
for: es para crear bucles o ciclo en programación,
es una secuencia de instrucciones de código que se ejecuta 
repetidas veces

range : rango es una secuencia inmutable de números enteros. 
Puede ser especificado por un inicio, un final y un paso.
'''

for i in range(11):
    print(i)

# Uso del while para crear bucles

i = 0

while i <= 10:
    print (i)
    i += 1

# Manejo de excepciones

# Ejemplo 1
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

# Ejemplo 2
try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

# Ejercicio extra

'''
Imprime los números del 10 al 56 siempre y cuando 
sean números pares y que no sean ni el 16 ni
múltiplos de 3.
'''


for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)