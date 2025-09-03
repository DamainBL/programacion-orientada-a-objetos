#Damian Bermudez Lara
#suma de numeros hasta el 15000

print ("bienvenido a numeros del 5 al 15000 \n")

#declarar variables

menu = 5

numero = 0

while (menu!=0):

    #esperar a order del usuario
    
    menu = int(input("mini menu--- escribe 1 para realizar el conteo --- escribe 0 para salir --- \n"))
    
    if(menu==1):

    #bucle de suma hasta completar los 15000
        
        for i in range(1, 3001):

            numero = numero + 5
        
            print (numero)
    elif(menu==0):

        print("adios")

    else:
             
        print("opcion no encontrada")


