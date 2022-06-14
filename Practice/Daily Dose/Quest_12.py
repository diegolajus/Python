"""
Question: Write a program, which will find all such 
numbers between 1000 and 3000 (both included) such 
that each digit of the number is an even number. 
The numbers obtained should be printed in a 
comma-separated sequence on a single line.
"""

# Lista vacía donde almacenamos los numeros
# del rango que solo contienen numeros pares
only_even = []
#Recorremos el rango
for item in range(1000,3001):
    # Convertimos los numeros del rango recorrido en str
    # para evitar 'int' object is not subscriptable (no se puede acceder a un numero como si fuera un diccionario,lista, string...)
    e = str(item)
    # al convertir cada caracter de nuevo en integer
    # y ver que son pares...
    if (int(e[0]) %2 == 0) and (int(e[1]) %2 == 0) and (int(e[2]) %2 == 0) and (int(e[3]) %2 == 0):
        only_even.append(e)# ... los añadimos a la lista vacía
print(",".join(only_even)) # mostramos por consolas unas comas a las
                 # cuales les añadimos los numeros de la lista
