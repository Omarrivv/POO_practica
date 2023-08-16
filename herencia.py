class Persona:  # superconjunto 
    def __init__(self,nombre, edad, nacionalidad): # el self va aser referncia asi mismo y con parametros que nosotros le iremos a pasar
        self.nombre = nombre  # definiendo que el self.nombre va aser como yo voy a acceder a el nombre y asi con cada uno de los demas
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):  # creamos un metodo de def hablar  y siempre con el self para referirse asi mismo 
        print(f"Hola mi funcion es hablar ... yo soy {self.nombre}")

#subconjunto Empleado
class Empleado(Persona):  # creamos una clase empleado heredara de Persona que seria Persona la clase padre -> Empleado hereda de la clase Persona
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):  # aqa va a tener lo mismos que tenemos de la clase padre : persona y lo que nosotros queremos agregar a esta clase espesifica ejmplo trabajpo y salrio
        super().__init__(nombre,edad,nacionalidad) # con el metodo super().__init__(dentro de este parentesiosi ira que queremos agregar de la clase Persona ) para que sean propiedades epesificas para el empleado 
        self.trabajo = trabajo # creamos devuelta con el metodo cel en este caso el trabajo y salrio que nos servira solamente pra esta clase de empleado 
        self.salario = salario
#subconjunto Estudiante
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.motas = notas
        self.universidad = universidad

omar = Empleado("Omar",17,"Peruano","Experto en tecnologias de programacion",30000)
omar.hablar()


#TIPO DE HERENCIA SIMPLE SIEMPRE Y CUANDO SOLO SEA PERSONA DE SUPERCONJUNTO Y EMPLEADO O ESTUDIANTE QUE SEA SUBCONJUNTO 
# TAMBIEN TENEMOS LA HERENCIA GERARQUIQUA : SE LE LLAMA CUANDO HAY UNA CKLASE QUE DEPENDEN DE TODAS LAS DEMAS 
# TAMBIEN TENEMOS LA HERENCIA MULTIPLE 
