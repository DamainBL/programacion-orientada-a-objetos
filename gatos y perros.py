#damian bermudez lara
#clases

print("programa gatos y perros \n")

class gato:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color

class perro:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color

el_gato = gato(input("el gato es de raza: "), input("el gato es de color: "))
el_perro = gato(input("el gato es de raza: "), input("el gato es de color: "))


print(f"el gato es un {el_gato.raza} de color {el_gato.color} y dice MIAU!")
print(f"el perro es un {el_perro.raza} de color {el_perro.color} Y DICE GUAU!")




