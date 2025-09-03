#Damian Bermudez Lara

x1 = 5
x2 = 10
x3 = 15
prcio = 50000
precio = 100000
precio1 = 150000
total = 0
descuento = 0
xd = 0

producto = int(input("ingrese el precio del producto que desea comprar: "))


def descuento(producto)


if(precio>producto>=prcio):

    descuento = (producto*x1)/100
    total = producto-descuento
    xd = x1

elif(precio1>producto>=precio):

    descuento = (producto*x2)/100
    total = producto-descuento
    xd = x2

elif(producto>=precio1):

    descuento = (producto*x3)/100
    total = producto-descuento
    xd = x3

print("----el subtotal de su producto es ",producto, "---- has !!!ganado¡¡¡ un descuento de: ",xd, "%----")
print("\n el total de lo que debes pagar son: ", total)

