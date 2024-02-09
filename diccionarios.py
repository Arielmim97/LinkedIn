#Creando diccionario con dict

diccionario = dict(nombre="Ariel", apellido="Mendez")

#Las listas no pueden ser mutables
diccionario = {frozenset(["Ariel", "Si soy"]): "jajajaja"}
#Creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")

print(diccionario)