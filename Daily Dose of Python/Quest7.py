"""
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""
# Pedimos dos numeros separados por comas
user_input = input("Enter values for row and column number: ")
rows, cols = user_input.split(",")
# Los convertimos en integers
rows = int(rows)
cols = int(cols) 
# resultado final (grid)
result = []
# Recorremos un rango igual al primer numero (las filas del usuario)
for x in range(rows):
    # Fila vacía
    row = []
    # Recorremos un rango igual al segundo numero (las columnas del usuario)
    for y in range(cols):
        # Por cada una de ellas, añadimos el producto a la fila
        row.append(x * y)
        # Finalmente cada una de las filas es añadida ala grid vacía "result"
    result.append(row)
    # Vemos en consola todas las filas creadas
    print(row)
# Vemos en consola todas las filas añadidas a la variable resultado (grid)
print(result)