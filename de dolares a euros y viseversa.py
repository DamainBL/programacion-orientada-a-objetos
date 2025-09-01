#Damian Bermudez Lara
#calcular area de rectangulo 

print ("bienvenido a coversor de auros a dolares \n")

menu = 5

euro = 0.85

dolar1 = 1.17

while (menu!=0):

    menu = int(input("mini menu--- escribe 1 para realizar de dolares a euros --\n-- escribe 2 para realizar de euros a dolares --- escribe 0 para salir--- \n"))
    
    if(menu==1):

        dolar = float(input("ingrese la cantidad de dolares que desee convertir: "))

        dolar = dolar * euro

        print(dolar)

    elif(menu==2):

        
        euro1 = float(input("ingrese la cantidad de dolares que desee convertir: "))

        euro1 = euro1 * dolar1

        print(euro1)

    
    elif(menu==0):

        print("adios")

    else:
             
        print("opcion no encontrada")

