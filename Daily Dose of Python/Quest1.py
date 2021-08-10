"""
Write a program which will find all such numbers which are 
divisible by 7 but are not a multiple of 5, between 2000 and 3200 
(both included).The numbers obtained should be printed in a 
comma-separated sequence on a single line.
 
"""

# RANGO 2000 3200
# DIVISIBLE POR 7
# MULTIPLE OF 5

l = []

for i in range (2000,3200):   # recorro todo el rango
    if  i % 7 == 0 and i % 5 != 0: 
        print(i, end=",")        

# i % 7 == 0 (todos los numeros que dividos por 7 daran de resto 0)
# i % 5 != 0 (todos los numeros que dividios por 5 daran de resto algo que no es 0)
# print(i, end=",") para que se imprima todoe n una linea
