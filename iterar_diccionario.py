diccionario = {
    "nombre" : "Ariel",
    "apellido" : "Mendez",
    "subs" : "1000"
}
#Recorriendo un diccionario para obtener las claves
for key in diccionario:
    key 
    print(f"La clave es: {key}")

#Recorriendo un diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")
