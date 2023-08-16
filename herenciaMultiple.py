class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola mi funcion es hablar ... soy {self.nombre}")


class Artista:
    def __init__(self,habilidad):
        self.habilidad =habilidad

    def mostrar_habilidad(self):
        print(f'Mi habilidad es {self.habilidad}')


class EmpleadoArtista(Persona, Artista):  # en este caso hereda de dos clases como de Persoona y Artista 
    def __init__(self,nombre, edad, nacionalidad,habilidad,salario,empresa):  #definir todo lo que va a tener y aparte creare 2 propiedades apartes como salario y empresa 
        Persona.__init__(self,nombre, edad, nacionalidad)  # que vamos a heredar directa a la clase , y en el parenteis (lo que vamos a heredar de persona y asi con lo de Artista pero cada uno en diferentes init )
        Artista.__init__(self,habilidad)
        self.salario = salario  # el self es un metodo para acceder asi mismo y luego rl .salrio es como nosotros va,mos a aceder a ese valor
        self.empresa = empresa


    def presentarse(self):
        return f'{super().mostrar_habilidad()}'  # al usra super estamos terminando de decirle al programa que mostrarhabilidad es un metodo que se crae desde arriba 
    

omar = EmpleadoArtista("Omar",17,"Peruano","Experto en tecnologias de programacion",30000,"AmazonGoogleCORP_OMAR")
omar.hablar()
print(f'Mi habilidad es {omar.habilidad}')

instancia = isinstance(omar, EmpleadoArtista)                                                          

herencia = issubclass(EmpleadoArtista,Persona)                                                          
                                                          
print(instancia)                                                          
# metodo de resolucion de orden MRO cual es el orden en que python va a llamar primero 
# alt + click -> seleccionar varias lineas : Insertar cursor
#Ctrl+Alt+ ↑ / ↓   :  Insertar cursor arriba/abajo
# Ctrl+u :  Deshacer la última operación del cursor
#Shift+Alt+I   : Insertar cursor al final de cada línea seleccionada
# Ctrl+I  : Seleccione la línea actual
# Ctrl+Shift+L   : Seleccionar todas las apariciones de la selección actual
#Ctrl+F2   : Seleccionar todas las apariciones de la palabra actual
# Shift+Alt+→  : Ampliar selección
# Shift+Alt+←   : Reducir selección
# Shift+Alt +  :  Selección de columna (caja)
# (drag mouse)   :  
#  Ctrl+Shift+Alt   : Column (box) selection
#  + (arrow key)  : 
#  Ctrl+Shift+Alt  : Column (box) selection page up/down
#  +PgUp/PgDn  : 


