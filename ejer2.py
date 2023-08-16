class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola mi funcion es hablar ... soy {self.nombre}")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.motas = notas
        self.universidad = universidad

class Jefe(Persona):
    def __init__(self,nombre,edad,nacionalidad,empresa,ganancias):
        super().__init__(nombre,edad,nacionalidad)
        self.empresa = empresa
        self.ganancias = ganancias


roberto = Empleado("Marcos",17,"Peruano","Ingeniero de Sistemas",9000)
# roberto.hablar()

jorge = Estudiante("Jorge",34,"USA",20,"Valle grande")

omar = Jefe("Omar",20,"Peruano","TWPOOY",20000)

# print(f'El empleado {roberto.nombre} trabaja en {roberto.trabajo} y su salario es de {roberto.salario}')

# print(f'El estudiante {jorge.nombre} esta estudiando en {jorge.universidad} sus notas son de {jorge.motas} el es hijo de {omar.nombre} que a la vez {omar.nombre} es el jefe de {roberto.nombre} en la empresa {omar.empresa}')

# print(omar.nombre)

