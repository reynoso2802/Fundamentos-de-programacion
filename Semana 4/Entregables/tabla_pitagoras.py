#Se le piden los datos al usaurio
renglon = int(input("Ingresa el primer factor: "))
columna = int(input("Ingresa el segundo factor: "))

cant = 10
#Creación de la matriz
tabla = []
for f in range (1, cant + 1):
    fila = []
    for c in range (1, cant + 1):
        fila.append (f*c)
    tabla.append (fila)


#Creación de la tabla de pitagoras 

print("\t", end="")
for c in range ( 1, cant + 1):
    print (c,end="\t")
print ()

for f in range (1, cant + 1):
    print (f , end="\t")
    for c in range (1, cant+ 1): 
        print(f*c, end="\t") 
    print ()


# Validar los factores

while renglon < 1 or renglon > 10:
    print("Ingresa un número entre 1 y 10")
    renglon = int(input("Ingresa el primer factor: "))

while columna < 1 or columna > 10:
    print("Ingresa un número entre 1 y 10")
    columna = int(input("Ingresa el segundo factor: "))
# Función para consultar el producto

def consultar_producto(tabla, renglon, columna):

    resultado = tabla[renglon - 1][columna - 1]

    return resultado

# Consultar el resultado
resultado = consultar_producto(tabla, renglon, columna)
print("El resultado de", renglon , ("*") , "es:", resultado)