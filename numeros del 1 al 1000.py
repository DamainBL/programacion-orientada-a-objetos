#Damian Bermudez Lara
#numeros dell 1 al mil

print ("bienvenido a numeros del 1 al 10000 \n")

#declarar variables

menu = 5

numero = 0

while (menu!=0):

    #esperar a que el usuario de la orden de empezar a contar

    menu = int(input("mini menu--- escribe 1 para realizar el conteo --- escribe 0 para salir --- \n"))
    
    if(menu==1):

    #bucle de suma hasta completar  10000
    
        for i in range(1, 10001):

            numero = numero + 1
        
            print (numero)
            
    elif(menu==0):

        print("adios")

    else:
             
        print("opcion no encontrada")






