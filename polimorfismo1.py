# multiples formas de hacer cosas pero dde diferentes maneras

class Gato():
    def sonido(self):
        return f'Miau'
    
class Perro():
    def sonido(self):
        return f'Guau'
    
class Vaca():
    def sonido(self):
        return f'muuuuuu'

def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()
vaca = Vaca()

print(gato.sonido())
print(perro.sonido())
print(vaca.sonido())

hacer_sonido(vaca)

