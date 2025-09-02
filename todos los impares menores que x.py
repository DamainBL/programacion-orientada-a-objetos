#Damian Bermudez Lara
#numeros menores impares

print("programa para saber los numeros impares menores que tu numero")

#recopilar datos

numero_1 = int(input("escriba un numero arabigo entero: "))

print("\nsu numero es ", numero_1, "y los menores impares que el son: ")

#bucle segun el numero dicho por el usuario

for i in range(1, numero_1):

    numero_1 = numero_1 - 1

#verificar si el numero es impar e imprimirlo

    if(numero_1%2!=0):

        print(numero_1)

        

    


    
