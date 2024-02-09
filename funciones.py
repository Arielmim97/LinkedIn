#Creando una funcion simple
#def saludar():
#    print("Hola Ariela como andas?")
#ejecutando una funcion simple
#saludar()

#Funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else :
        adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo} como andas?")
    
saludar("Gabriela", "Mujer")

#Crear funciones que retornen valores
def crear_contraseñas_andom(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}"
    return contraseña   

 
password = crear_contraseñas_andom(98)
frase = f"Tu contrase;a nueva es {password}"
print(frase)