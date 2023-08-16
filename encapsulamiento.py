# # tema de encapsulamiento d en python nos sirve para proteger metodoss , variables ejemplo: que alguien no deba acceder a un metodo variable , etc 
# # SEETERS Y GEETERS son 2 metodos que se utilizan para acceder a las propiedades privadas que tienen las clases y no solo accederlas si no tambien modificarlas : formas de acceder y modificar o establecer los valores de un atributo 
# class MiClase:
#     def __init__(self):
#         self._atributo_privado= "Valor"  # este es un atributo privado y tambien tenemos a tributos muy muy privados con solo poner __ 2 guiones bajos
#         self.__atributo_muy_muy_privado = "Yo soy omar RoHack"  # este es un atributo muy muy privado


#     def __hablar():  # metodos privados  podemos decirle que sea un metodo privado con solo _ un guion o le odemos decir que va hacer un metodo muy muy privado con __ 2 guiones 
#         print("Hola que tal yo soy Omar ")

# objeto = MiClase()
# privacidad = MiClase()
# print(objeto._atributo_privado)

# # print(privacidad.__atributo_muy_muy_privado)

# print(privacidad.__hablar())

# class Persona:
#     def __init__(self,nombre,edad):
#         self._nombre = nombre
#         self._edad = edad

#     def get_nombre(self):
#         return self._nombre
    
#     def set_nombre(self, new_nombre):
#         self._nombre = new_nombre

# omar = Persona("Omar",17)

# nombre = omar.get_nombre()

# print(nombre)

# omar.set_nombre("rivera")
# # omar._nombre = "Rosas"

# nombre = omar.get_nombre()

# print(nombre)

# decoradores .py

