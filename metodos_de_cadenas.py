cadena1 = "Hola soy Ariel"
cadena2 = "Soy grande"
#Mayusculas y minusculas
mayus = cadena1.upper()
minus = cadena1.lower()

#Primer letra mayuscula
primer_letra_mayuscula = cadena1.capitalize()

#Buscar una cadena en otra cadena si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("o")
#buscamos una cadena en otra cadena, si no hay coincidencias devuelve una excepcion
busqueda_index = cadena1.index("a")

#si es numerico devuelve true
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("Hola")

#contamos cuantos caracteres tiene
contar_caracteres = len(cadena1)

#verificacmos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con  = cadena1.startswith("hola")

#verificacmos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("l")

#reemplaza un pedazo de la cadena dada con otra dada
cadena_nueva = cadena1.replace("la", "lu")

print(cadena_nueva)
