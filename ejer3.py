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


class EmpleadoArtista(Persona, Artista):
    def __init__(self,nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa


    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
    

omar = EmpleadoArtista("Omar",17,"Peruano","Experto en tecnologias de programacion",30000,"AmazonGoogleCORP_OMAR")
omar.hablar()
print(f'Mi habilidad es {omar.habilidad}')

instancia = isinstance(omar, EmpleadoArtista)

# herencia = issubclass(EmpleadoArtista,Persona)

print(instancia)
