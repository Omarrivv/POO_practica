# ejercicio de herencia y uso de super
# sistema para un escuela En el sistema vamos a tener 2 clases principales : personba y estudiante 
# la clase persona tendra los atributos de nombre y la edad  y un metodo que imprima el nombre y la edad 
# de la persona la clase estudiante heredarra de  la clase persona y tendfra un atributo adicional : grado y un metodo que imprima
# el grado del estudiante deberas utilizar super en el metodo de inizializacion (init) para reutilizar el codigo de la clase padre (persona)
#luego crea una instancia de la clase Estudiante e imprima sus atributos y utiliza sus metodods para asegurarte de que todo funciona
# Correctamente
class Personas:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def nombre_edad(self):
        return f"El nombre es {self.nombre} y su edad es de : {self.edad}"
class Estudiante(Personas):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def llamar_grado(self):
        return f'El grado del estudiante {self.grado}'

omar = Personas("Omar",19)
print(omar.nombre_edad())
luis = Estudiante("Omar",34,"2")
print(luis.llamar_grado())

