#PROCESAMIENTO DE MANTENIMIENTO DE FLOTILLAS VEHICULARES
print ("Servicio de apoyo para el mantenimiendo de unidades")
#Para iniciar el proceso del programa se pedira una contraseña, si no es la correcta el programa no se ejecutará
llave = str(input("Ingresa la contraseña "))
if llave == "gerente2026":
    print ("Acceso permitido, Bienvenido. ")
else:
    print ("Contraseña incorrecta, intente nuevamente. ")
    exit()

# Solicitar datos y kilometrajes del vehiculo al empleado 
ncoche = str(input("Ingresa el nombre del auto:"))
kmactual = int(input("Ingresa el kilometraje actual:"))
kmserv = int(input("Ingresa el kilometraje del próximo servicio:"))

if ncoche == "mazda 3":
    print ("Auto utilitario")
elif ncoche == "toyota hilux":
    print ("Vehiculo Utilitario de carga")
elif ncoche == "chevrolet suburban":
    print ("Auto ejecutivo")
else:
    print ("Auto no registrado verifique el nombre de la unidad")
    exit()

#Asignación de los costos de servicio 
#Se consideran los 3 tipos de vehiculos que la empresa solicita,
#Los costos de mantenimiento respectivos para Mazda 3 (Mt1) , Toyota Hilux (Mt2) y Chevrolet suburban (Mt3)
mtmenor1 = 3050
mtmayor1 = 5650

mtmenor2 = 4705
mtmayor2 = 9550

mtmenor3 = 3600
mtmayor3 = 7559

# Lista de vehículos registrados en la flotilla 
vehiculos = ["mazda 3", "toyota hilux", "chevrolet suburban"]
 

#Condicionales de acuerdo al km ingresado y por realizar servivio 
if kmactual >= kmserv:
    print("La unidad requiere mantenimiento.")
    print("1. Mantenimiento menor")
    print("2. Mantenimiento mayor")

    tipo = int(input("Selecciona el tipo de mantenimiento: "))

    if ncoche == "mazda 3":
        if tipo == 1:
            print("Costo del mantenimiento:", mtmenor1)
        elif tipo == 2:
            print("Costo del mantenimiento:", mtmayor1)
        else:
            print("Tipo de mantenimiento no válido.")

    elif ncoche == "toyota hilux":
        if tipo == 1:
            print("Costo del mantenimiento:", mtmenor2)
        elif tipo == 2:
            print("Costo del mantenimiento:", mtmayor2)
        else:
            print("Tipo de mantenimiento no válido.")

    elif ncoche == "chevrolet suburban":
        if tipo == 1:
            print("Costo del mantenimiento:", mtmenor3)
        elif tipo == 2:
            print("Costo del mantenimiento:", mtmayor3)
        else:
            print("Tipo de mantenimiento no válido.")

else:
    faltan = kmserv - kmactual
    print("La unidad no requiere mantenimiento.")
    print("Faltan", faltan, "km para el próximo servicio.")