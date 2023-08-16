class A:
    pass
class BASE:
    def hablar(self):
        print("Hola desde el canal pro")
class X:
    def hablar(self):
        print("HOLA desde X")
class Y(X):
    pass
class Z(Y):
    pass
class F:
    pass
class B():
    pass
class C(F):
    pass
class D(B,C,Z):
    pass
d = D()
d.hablar()
# print(D.mro())

