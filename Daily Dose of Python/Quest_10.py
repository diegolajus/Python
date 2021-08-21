"""
Question: Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and sorting 
them alphanumerically. Suppose the following input is supplied to the program: 
hello world and practice makes perfect and hello world again 
Then, the output should be: 
again and hello makes perfect practice world

"""

# Pedimos input para que introduzca texto
x = input()
# Recorre el input anterior y separa cada palabra introducida
y = [i for i in x.split(" ")]
# mostramos en pantalla la lista con:
    # sort() (ordenada alfabeticamente)
    # set() (devuelve elemento iterable sin repetir)
print((sorted(set(y))))
# faltaba volver a juntar los elementos de la 
# lista con espacios para que se vean como un texto.
print(" ".join(y))

