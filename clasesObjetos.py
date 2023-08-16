# clases y objetos 
from psutil import win_service_iter
class Celular: # self es una forma de hacer referencia asi mismo a un objeto ,  por ejemplo si yo digo self.marca es como decir celular.marca si yo digo self.modelo es como decir celular.modelo es una forma de hacer referencia asi mismo 
    def __init__(self , marca, modelo , camara):  # crear un metodo llamado int es un metodo especial cada vez que  instanciamos una clase este metodo se ejecuta automaticamente
        self.marca = marca  # accediendo a un parametro el igualar alm valor de marca que seria el parametro que esta despues de las  comas de self sse entiende xd .. ? 
        self.modelo = modelo
        self.camara = camara
# el metodo def __init__ es un metodo especial es un metodo constructor (self es una forma de referirse a si mismo ) pasarle lo que queremos que tenga
# self.marca = marca  y los demas : es como decir celular.marca y el igual a marca es el parametro que iremos a pasar depsues : creando la propiedad de self y luego accediendo a un parametro 
    def llamar(self):  # sin el self te dara error : por que si no das el parametro que hace referncia al objeto , para que el objeto pueda utilizar ambas metodos como de llamar y cortar
        print(f'Estas llamando desde un : {self.modelo}') # y en este caso el self.modelo es como indicar a si mismo con el self y accediendo al modelo que seria ese celular que nosotros mismos lo hemos creado 

    def colgar(self):
        print(f'Estas colgando con : {self.modelo}')

celulares_omar = Celular("smafung", "nonvosd", "57MP")
print(celulares_omar.camara)
celular1 = Celular("Sansung", "S23", "48MP")
celular2 = Celular("IphoneOmar", "PRO  MAX", "60MP")
celular1.llamar()
celular2.colgar()


# que es una clase , que es un constructor y como funciona , los atributos y propiedades : como funciona los metodsos como funciona self como crear objetos 