# ejercicio de herencia y uso de super
# sistema para un escuela En el sistema vamos a tener 2 clases principales : personba y estudiante 
# la clase persona tendra los atributos de nombre y la edad  y un metodo que imprima el nombre y la edad 
# de la persona la clase estudiante heredarra de  la clase persona y tendfra un atributo adicional : grado y un metodo que imprima
# el grado del estudiante deberas utilizar super en el metodo de inizializacion (init) para reutilizar el codigo de la clase padre (persona)
#luego crea una instancia de la clase Estudiante e imprima sus atributos y utiliza sus metodods para asegurarte de que todo funciona
# Correctamente
class Personas:  # crear la clase Persona inicialisamos 
    def __init__(self,nombre,edad): # el self __init__ entre parentesis (el metodo que se refiere a si mismo el self , los parametros que tendra en este caso nombre , edad)
        self.nombre = nombre  # recordar iniciar el self.nombre sera el metodo como vamos a acceder a los parametros que iremos a pasar , parametros son lo que definimos en el def init que serian nombre , y la edad 
        self.edad = edad
    def nombre_edad(self):  # creamos una funcion de nombre_edad con el (self) , referirse asi mismo : que cuando accedamos a ella
        return f"El nombre es {self.nombre} y su edad es de : {self.edad}"  # nos dara el valor que estamos retornando
class Estudiante(Personas):  # creamos una clase Estudiante e inicialisamos
    def __init__(self,nombre,edad,grado):  # en este def__init ponemos los parametros de nombre,edad que vendria heredando de la clase "Personas" y aparte un parametro mas de grado
        super().__init__(nombre,edad)  # el super().init es para traer los parametros al que accedemos de la clase Personas ya que en la linea 15 : donde especificamos el estra de grado solo lo estamos definiendo y aqui con el super()__init__ lo estamos traendo  : no tenemos que pasar el self ya que : self no se pasa como parametro cuando usamos la funcion super() : si no usamos la funcion super() ay si pasamos self 
        self.grado = grado  

    def llamar_grado(self):  # funcion de llamar_grado la inicialisamos con el self : es metodo de referirse asimismo 
        return f'El grado del estudiante {self.grado}'  # y lo que tendra el llamar_grado es : retornar lo que pongamos en este mensajo del grado del estudiante es tal

omar = Personas("Omar",19)
print(omar.nombre_edad())
luis = Estudiante("Omar",34,"2")
print(luis.llamar_grado())

