def Menu():
    print ("Menu de calculadora")

    print ("1.- Suma")
    print ("2.- Resta")
    print ("3.- Multiplicacion")
    print ("4.- Divicion")
    print ("5.- Salir")


def Calculadora():
    print ("Funciones Aritmeticas")

    Menu()

    opc= int (input("Seleccion la opcion\n"))

    while (opc>0 and opc<5):
        x= int (input("Ingresa un numero: "))
        y= int (input("Ingresa otro numero: "))

        if (opc==1):
            print ("Suma es:",x+y)
            opc= int (input("Secciona opcion: "))

        elif(opc==2):
            print ("Resta es:",x-y)
            opc= int (input("Secciona opcion: "))

        elif(opc==3):
            print ("Multiplicacion es: ",x*y)
            opc= int (input ("Seleccion opcion: "))

        elif(opc==4):
            print("Divicion es: ",x/y)
            opc= int (input ("Seleccion opcion: "))

##############









        

Calculadora()

print ("Fin del programa")
input(".....")
