"""
Question: Use a list comprehension to square each odd number 
in a list. The list is input by a sequence of comma-separated
 numbers. Suppose the following input is supplied to the 
 program: 1,2,3,4,5,6,7,8,9 
 Then, the output should be: 1,3,5,7,9
"""

user_list = input()
# variable que reune todos los nums de user_list que cuyo resto al dividirlo entre 2 no sea 0
odds = [x for x in user_list.split(",") if int(x)%2!=0] # "!=" porque x es 0 en la primera iteración
# mostramos por pantalla unas comas a las cuales les añadimos los items de la lista odds
print(",".join(odds))
