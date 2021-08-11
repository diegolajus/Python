nombre = input("Escribe tu nombre ")
edad = input("Escribe tu edad ")
email = input("Escribe tu email ")
fruta = input("Escribe tu fruta favorito ")

personal_data = {
    "nombre":nombre,
    "edad":edad,
    "email":email,
    "fruta":fruta,
}

print (f"Mr./Ms.{personal_data['nombre']} tiene {personal_data['edad']} años , su email es {personal_data['email']} y su fruta favorito es {personal_data['fruta']}")

