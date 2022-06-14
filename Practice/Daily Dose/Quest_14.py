"""
Question: Write a program that accepts a sentence and calculate the
 number of upper case letters and lower case letters. Suppose the 
 following input is supplied to the program: Hello world! Then, the 
 output should be: UPPER CASE 1 LOWER CASE 9
"""

#definimos variables
x = input()
y = {"Upper Case":0,"Lower Case":0} #Diccionario con dos claves:valor (contador)
#recorremos el input y tras saber si isupper() o islower()...
for item in x:
    if item.isupper():
        y["Upper Case"] = y["Upper Case"]+1 # ...añadimos 1 al contador
    elif item.islower():
        y["Lower Case"] = y["Lower Case"]+1 #...añadimos 1 al contador
    else:
        pass# si no pasa nada salimos del loop
#Mostramos por consola los dos contadores, con titulos para saber cual es cual
print("Upper Case", y["Upper Case"] )
print("Lower Case", y["Lower Case"] )

    