#promedio de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5
#Duraciond de crudos
crudo_promedio = 5
crudo_dalto = 3.5
#Diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el tiempo vacio promedio
tiempo_vacio_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto/ 10
#mostrando la diferencia de durancion
print("--------------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el mas que el promedio")
print("--------------------")

#Ejecricio B
print("--------------------")

print(f"Un curso promedio elmina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")

#mostrando diferencia si los cursos duraran 10 horas
print("--------------------")
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos")