lista_precios_kg = {
    "Platano":0.95,
    "Manzana":0.8,
    "Pera":0.79,
    "Sandia":1.7,
}




#Mostrar al usuario qué fruta hay disponible (Se muestra como una lista)
# Funcion para devolver la lista en string (Visualmente mejor en la consola después)     
def listToString(fruta_disponible): 
    str1 = " " 

    return (str1.join(fruta_disponible))
           
fruta_disponible = [key for key in lista_precios_kg.keys()]


print(f"Hoy nos queda esta fruta: ", listToString(fruta_disponible)) 




# Pedimos al usuario qué fruta quiere comprar
fruta = input ("¿Qé fruta quieres? ")

if fruta in lista_precios_kg:
    kilos = float(input(f"¿Cuantos kilos de {fruta} quieres?"))
    print(f"{kilos}Kg de {fruta} valen a {lista_precios_kg[fruta]*kilos} $ ")
else:
    print(f"{fruta} no se encuentra disponible")