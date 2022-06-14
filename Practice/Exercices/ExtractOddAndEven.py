#separar una lista de numeros entre pares e inmpares


ejemplo = [3,7,9,5,3,7,12,20,25,48,78,45,12,64,97,53,48,78,52,1,5,8,7,4,5,2,3,6,9,8,9,8,56,235,458,785,123,568,452,125,785,458,785,325]

def separar (lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

pares, impares = separar(ejemplo)

print (pares)
print(impares)


