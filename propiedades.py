class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre  # del  hace que : un operador que elimina valores

omar = Persona("Omar",17)

nombre = omar.nombre
print(nombre)

omar.nombre = "RIhack"

nombre = omar.nombre
print(nombre)

del omar.nombre

print("heozdgnispgs iiilm9sf9hkas omay roks omf9ekne9 contrs = paword quwe jacer tu como siempre que miersa tu aras ")

