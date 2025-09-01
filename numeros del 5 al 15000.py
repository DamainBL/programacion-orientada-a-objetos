#Damian Bermudez Lara
#calcular area de rectangulo 

print ("bienvenido a numeros del 5 al 15000 \n")

menu = 5

numero = 0

while (menu!=0):

    menu = int(input("mini menu--- escribe 1 para realizar el conteo --- escribe 0 para salir --- \n"))
    
    if(menu==1):

        for i in range(1, 3001):

            numero = numero + 5
        
            print (numero)
    elif(menu==0):

        print("adios")

    else:
             
        print("opcion no encontrada")

