"""
Question 6
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24


"""
import math #para math.sqrt()
#Variables 
c=50
h=30
#resultado final 
result = []
#Recorremos los números que el user introduce en el input separados por comas (split())
user_numbers=[x for x in input().split(",")] 
#Recorremos user_numbers para poder aplicar la fórmula (aún no creada) a cada uno de los user_numbers
for y in user_numbers:
    #Fórmula que se añade (append()) a la variable result. round para 
    result.append(round(math.sqrt(2*c*float(y)/h))) 
    # 'y' es un string, convertir en float.

    # Si convertimos 'y' en un integer, el usuario no podría introducir numeros con decimales en el input..
    # ValueError: invalid literal for int() with base 10
print(result)