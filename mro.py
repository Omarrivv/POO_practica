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
class Z(Y):  # y La Z es la siguiente parametro que estaria como una ultima opcion pero no esta la funcion de hablar asi que no ejecuta nada y seguira buscando en el orden jerarquico
    pass  # no hacer nada una forma mas simple de decirlo 
class F:
    pass
class B():  # ahora como en esta clase de B no hace nada ya que esta con pass vamos devuelta al orden que la otra clase seria la C
    pass
class C(F): # Y C tampoco no hace nada ya que no tiene ninguna funcion de hablar y a esa funcion nosotros estamos intentando llamar a hora como no hay nada seguiremos con el orden jerarquico
    pass  # correccion ejemplo si en la jerarquia de B ejemplo tiene : B(A) seguira al 2a no da una segunda vuelta correccion hara lo que dije en los demas comentarios , siempre  y cuando hereden de uno mismo ejemplo si de D(hay B,Z) y esos 2 heredan de A si daran solo a la clase A espero q se haya entendido .
class D(B,C,Z):  # este caso es a esta clase a la que llamamos que es la clase D(con sus parametros de B , C , Z) el orden seria irse primero a B 
    pass  # hay algo que no explice como no encontro nada En B,C,Z se va a dar una segunda vuelta si alguna de esas clase "hereda" de otras clases y seguiran ese orden jerarquico hasta encontrar la funcion de hablar y si no lo encuentra esa funcion no nos imprimira nada 
d = D()  # en este caso estamos definiendo que vamos a la clase : class D() que Tienen dentro de ellos 3 clases : metoddos que deben hacer la funcion de hablar lo que se define debajo de esta linea :
d.hablar()  # como en la linea que definimos "d = D()" llamamos esta clase "metodo" que debe tener la funcion de hablar y si no tiene nada en este caso va a seguir la jerarquia : en este caso estamos definiendo class D(B,C,Z):
#pass
print(D.mro())  # todo lo que dije el comentario resumida en este codigo te da el orden jerarquiqua
# y como se observa va en este orden : si no tiene la funcion hablar dentro de esa clase D seguira el orden de los parametros (1 ira a ser =B,2 ira a ser =C,3 ira a ser =Z) y en ese orden si le quieres agregar mas clases , si te preguntas a que me refiero con el metodo de hablar es : 
# def hablar(self):
#         print("HOLA desde X")  <----  me refiero a eso con el metodo de hablar y self como lo vuelvo a decir nos sirve de una forma para referirse a si mismo





