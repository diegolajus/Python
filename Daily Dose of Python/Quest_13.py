"""
Question: Write a program that accepts a sentence
 and calculate the number of letters and digits.
  Suppose the following input is supplied to the 
  program: hello world! 123 Then, 
  the output should be: LETTERS 10 DIGITS 3
"""

#definimos variables
x = input()
y = {"Digits":0,"Letters":0} #Diccionario con dos claves:valor (contador)
#recorremos el input y tras saber si isdigit() o isalpha()...
for item in x:
    if item.isdigit():
        y["Digits"] = y["Digits"]+1 # ...añadimos 1 al contador
    elif item.isalpha():
        y["Letters"] = y["Letters"]+1 #...añadimos 1 al contador
    else:
        pass# si no pasa nada salimos del loop
#Mostramos por consola los dos contadores, con titulos para saber cual es cual
print("Digits", y["Digits"] )
print("Letters", y["Letters"] )

 
    