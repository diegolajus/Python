"""

Question£º Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
 Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: 
 HELLO WORLD 
 PRACTICE MAKES PERFECT

"""

lines = []
# Loop en el que se abre un input para escribir, cuando se escribe + "PRESS ENTER",
# Pasaremos al siguiente input y así consecutivamente.
while True:
    s = input()
    if s:
        #Cada input introducido se guarda en la variable lines=[] con el string method .upper()
        lines.append(s.upper())
    # la siguiente acción, que no sea introducir otro input, nos hará salir del loop
    else:
        break;
# recorremos y mostramos cada una de las "lines" 
for s in lines:
    print (s)