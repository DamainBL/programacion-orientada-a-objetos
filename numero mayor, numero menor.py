#Damian Bermudez Lara
#numero mayor, numero menor

print("programa para saber que numero es mayor y cual es menor")

#tomar datos del usuario

numero_1 = float(input("escriba un numero arabigo: "))
numero_2 = float(input("escriba otro numero arabigo: "))

#realizar una conparacion de mayor o menor para determinar cual es el mayor y el menor

if(numero_1>numero_2):

    print("el numero ",numero_1,"es mayor que ", numero_2)

elif(numero_1==numero_2):

    print("el numero ",numero_1,"es igual que ", numero_2)

else:

    print("el numero ",numero_2,"es mayor que ", numero_1)
