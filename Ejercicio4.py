# Crear un programa que valide si una constraseña ingresada por el usuario es segura.
# Una contraseña segura:
#   1 - Tiene más de 8 caracteres.
#   2 - Tiene al menos una letra mayúscula.
#   3 -Tiene al menos un número.

#"print(len("Hola"))
#print("A".isupper())
#print("1".isnumeric())
#cadena = "Hola"
#for i in range (len(cadena)):
#    print(i)
    
#for i in range (len(cadena)):
#    print(cadena[i])

def comprobarContraseña (password):
    largo = False
    mayus = False
    numer = False

    if len(password) > 8:
        largo = True
    for i in range (len(password)):
        if password[i] .isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True 

    if largo and mayus and numer:
        return True
    else:
        return False

password = input("Ingrese una contraseña: ")

verificacion = comprobarContraseña(password)
if verificacion:
    print("La contraseña es segura")
else:
    print("Su contraseña no es segura")
