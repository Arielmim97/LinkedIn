animales = {"perro", "gato", "loro", "cocodrilo"}
numeros = {10,62,12,72}

#Recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a : {animal}")
#Recorriendo la lista numero y multiplicandola por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)
    
#Iterando dos conjunto al mismo tiempo con la misma cantidad de elementos
for numero_animal in zip(animales, numeros):
    print(f"recorriendo la lista 1: {numero}")
    print(f"recorriendo la lista 2: {animal}")
#No funciona en conjuntos
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}" )
    
#usando el else dentro del for
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
    
#todo lo anterior funciona igual para tuplas y conjuntos