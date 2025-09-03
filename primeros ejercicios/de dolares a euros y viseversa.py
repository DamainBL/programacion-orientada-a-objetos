#Damian Bermudez Lara
#conversion de dolares a euros

print ("bienvenido a coversor de euros a dolares \n")

#declarar los valores de conversion(segun lunes primero de septiembre del 2025)

menu = 5

euro = 0.85

dolar1 = 1.17

while (menu!=0):

#dar opciones al usuario segun la conversion que desee realizar
    
    menu = int(input("mini menu--- escribe 1 para realizar de dolares a euros --\n-- escribe 2 para realizar de euros a dolares --- escribe 0 para salir--- \n"))
    
    if(menu==1):

    #tomar el valor que desea convertir

        dolar = float(input("ingrese la cantidad de dolares que desee convertir: "))

    #realizar operacion e imprimir
        
        dolar = dolar * euro

        print(dolar)

    elif(menu==2):

    #tomar el valor que desea convertir
        
        euro1 = float(input("ingrese la cantidad de dolares que desee convertir: "))

    #realizar operacion e imprimir
        
        euro1 = euro1 * dolar1

        print(euro1)

    
    elif(menu==0):

        print("adios")

    else:
             
        print("opcion no encontrada")


