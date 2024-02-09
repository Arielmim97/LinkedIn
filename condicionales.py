ingreso_mensual = 7200
gasto_mensual = 80000

#If anidado y elif
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien, estas bien")
    else: 
        print("Estas gastando demasiado a ver si te alcanza")
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("Estas bien en el salvador")

else: 
    print("Sos pobre")
    
