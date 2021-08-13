"""
With a given integral number n, write a program to generate a 
dictionary that contains (i, i x i) such that is an integral 
number between 1 and n (both included). and then the program 
should print the dictionary.Suppose the following input is supplied 
to the program: 8
"""
# El usuario nos dará un int
n = int(input())
# Diccionario vacío
ans = {}
# se recorre un rango entre 1 y el numero del usuario +1
for i in range (1,n+1):
    # la clave del dicc. sera ans[1,2,3...] y el valor será i*i, 1*1, 2*2, 3*3 ...
    ans[i] = i * i
print(ans)