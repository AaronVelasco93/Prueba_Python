print ("Calculo del Iva de una cantidad")


print("1.- Digita el iva")
print("2.- Digita la catidad")

##definir la entrada de datos
print("Dame el iva: ")
ivacli=float(input())
cantidad=float(input("Dame una catidad: $"))

#imprime la cantidad
print("La catidad es: $",cantidad)
#Saca el iva (iva*'cantidad definida por el usuario')
print("El Iva es: ",ivacli*cantidad)

input("Preciona cualquier tecla para continuar....")
