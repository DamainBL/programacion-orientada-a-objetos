#Damian Bermudez Lara
#calcular area de rectangulo 

print("programa para calcular area y perimetro de rectangulo")

Largo = float(input("escriba el largo de su figura en numeros arabigos: "))
ancho = float(input("escriba la base de su figura en numeros arabigos: "))

perimetro = (Largo*2)+(ancho*2)
area = Largo*ancho 



print("menu--------1:perimetro-----------2:area----------0:salir")

menu = int(input("ingrese el numero de la accion que desea realizar: "))

while(menu!=0):

    if(menu==1):

        print(perimetro)

    elif(menu==2):

        print(area)
    
    else:
             
        print("opcion no encontrada")

    menu = int(input("ingrese el numero de la accion que desea realizar"))



