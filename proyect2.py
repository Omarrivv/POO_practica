class Aniimal:
    def comer(self):
        print("El animal esta comiendo ")

class Ave(Aniimal):
    def volar(self):
        print("El animal esta volando ")

class Mamifero(Aniimal):
    def amamantar(self):
        print("El animal esta amamantandose ")


class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()

print(Murcielago.mro())

