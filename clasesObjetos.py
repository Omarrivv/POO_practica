# clases y objetos 
from psutil import win_service_iter
class Celular: # self es una forma de hacer referencia asi mismo a un objeto ,  por ejemplo si yo digo self.marca es como decir celular.marca si yo digo self.modelo es como decir celular.modelo es una forma de hacer referencia asi mismo 
    def __init__(self , marca, modelo , camara):  # crear un metodo llamado int es un metodo especial cada vez que  instanciamos una clase este metodo se ejecuta automaticamente
        self.marca = marca  # accediendo a un parametro el igualar alm valor de marca que seria el parametro que esta despues de las  comas de self sse entiende xd .. ? 
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f'Estas llamando desde un : {self.modelo}')

    def colgar(self):
        print(f'Estas colgando con : {self.modelo}')


celular1 = Celular("Sansung", "S23", "48MP")
celular2 = Celular("IphoneOmar", "PRO  MAX", "60MP")
celular1.llamar()
celular2.colgar()


