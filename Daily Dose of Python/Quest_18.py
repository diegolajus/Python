"""
Question: A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

"""
import re # importamos expresiones regulares

passwords = input("Type in: ") # pedimos las contraseñas
passwords = passwords.split(",")# las separamos

accepted_pass = [] # introduciremos las válidas
for i in passwords:# recorremos el input del usuario
    
    # Aqui empieza el proceso de aceptacion de caracteres
    # si no cumplen los requisitos no seran añadidas al "accepted_pass"
    if len(i) < 6 or len(i) > 12: 
        continue # próxima iteracion
    # expresiones regulares (detecta caracteres de a - z en minusculas)
    elif not re.search("([a-z])+", i):
        continue
    # expresiones regulares (detecta caracteres de A - Z en mayúsculas)
    elif not re.search("([A-Z])+", i):
        continue
    # expresiones regulares (detecta caracteres de 0 - 9)
    elif not re.search("([0-9])+", i):
        continue
    # expresiones regulares (detecta caracteres especiales)
    elif not re.search("([!@$%^&])+", i):
        continue
        # si en ningun momento se ha passado a la próxima iteración
        # es que la contraseña es valida
    else:
        accepted_pass.append(i) # la añadimos a la lista

print((" ").join(accepted_pass)) # mostramos espacios unidos por el resultado de la lista