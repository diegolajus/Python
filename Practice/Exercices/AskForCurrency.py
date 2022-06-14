divisas = {
    "Bitcoin":"Btc",
    "Euro":"€",
    "Dollar":"$",
    "Ethereum":"Eth",
}

# get() en un diccionario el argumento será la clave, y devuelve el valor
ask = input("Busca una divisa: ")

if divisas.get(ask): #Devuelve True or False
    print(divisas.get(ask))
else: 
   print("This Currency is not in the Data Base")