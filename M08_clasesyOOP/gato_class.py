class Gato:
    def __init__(self, nombre, edad,raza, sexo):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
   #Creamos el método presentar
    def presentar(self):
        print("Mi Nombre: ", self.nombre)
        print("Edad: ", self.edad,"años")
        print("Raza: ", self.raza)
        print("Sexo: ", self.sexo)

gato1 = Gato('Pompon',2,'Siames','Macho')

gato1.presentar()

gato2 = Gato('Nina',3,'Mezcla','Hembra')

gato2.presentar()