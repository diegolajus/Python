"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to prinololt the string in upper case.
Also please include simple test function to test the class methods.

"""

# Construimos los parametros con metodo init
class GetAndPrint(object):
    def __init__(self):
        self.s = ""
# Definimos la primera funcion que guardará el input
    def getString(self):
        self.s = input()
# Definimos la segunda funcion que nso devolvera el input en UpperCase
    def printString(self):
            print(self.s.upper())

str = GetAndPrint()
str.getString()
str.printString()
