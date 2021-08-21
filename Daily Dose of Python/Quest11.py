"""
Question: Write a program which accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not. The numbers 
that are divisible by 5 are to be printed in a comma separated sequence. 
Example: 0100,0011,1010,1001 Then the output should be: 1010 
"""


# Pedimos numeros en binario
binaries = [x for x in input("Instert binary numbers").split(",")]

# recorremos el input
for i in binaries:
    #Si el contenido del recorrido no contiene ni 1 ni 0...
    if "0" not in i and "1" not in i:
        #...Pedimos un número en binario
        print(f"{i} is not a binary number")
    else:
        # si el contenido recorrido se divide entre 5 y el resto es 0 muéstralo por consola
        if int(i,2) %5 == 0:
            print(i)
        

        

