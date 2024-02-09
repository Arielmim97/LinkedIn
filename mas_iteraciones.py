#Creando las listas
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno" ]

cadena = "Hola Ariel"

numeros = [2,5,8,10]
#Evitando que se coma una granada con la sentencia continue
for fruta in frutas:
   if fruta == "granada":
       continue
   print(f"Me voy a comer una: {fruta}")
   
#Evitando que el bucle siga ejecutandose el else no se ejecuta tampoco
for fruta in frutas:
    if fruta == "perra":
        break
else: 
    print("terminado")
    
#Iterando(recorriendo) una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo(duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

