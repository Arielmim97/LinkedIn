#Creando un conjunto con set
conjunto = set({"Dato1", "Dato2"})


#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"Dato1", "Dato2"})
conjunto2 = {conjunto1, "Dato3"}


print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto2

#Verificando si es un superconjunto

resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)