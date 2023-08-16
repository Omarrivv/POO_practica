class Persona:
    def __init__(self,nombre, edad, nacionalidad): # el self va aser referncia asi mismo y con parametros que nosotros le iremos a pasar
        self.nombre = nombre  # definiendo que el self.nombre va aser como yo voy a acceder a el nombre y asi con cada uno de los demas
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola mi funcion es hablar ... yo soy {self.nombre}")


class Empleado(Persona):  # creamos una clase empleado heredara de Persona que seria Persona la clase padre -> Empleado hereda de la clase Persona
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.motas = notas
        self.universidad = universidad

omar = Empleado("Omar",17,"Peruano","Experto en tecnologias de programacion",30000)
omar.hablar()
