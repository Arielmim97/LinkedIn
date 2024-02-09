#Listas se pueden modificar
lista = ["Ariel Mendez", "Medicina", True, 1.85]
#Tuplas no se pueden modificar
tupla = {"Ariel Mendez", "Medicina", True, 1.85}

#Creando un conjunto (set)no se puedeacceder a elementos por inidice,  no almacena datos duplicados
conjunto = {"Ariel Mendez", "Medicina", True, 1.85, "soy ariel"}

print(conjunto)
#Key : value y separado en comas
diccionario = {
    "nombre" : "Ariel",
    "Estuido" : "medicina",
    "altura" : 1.86,
    "dato_duplicado": "soy ariel"
}

print(diccionario["altura"] + 2)


