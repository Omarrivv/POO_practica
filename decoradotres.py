def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamatr a la funcion ")
        funcion()
        # print("Despues de llamar a la funcion ")
    return funcion_modificada()
# def saludo():
#     print("Hola Omar")

# saludo_modificado = decorador(saludo)

@decorador
def saludo():
    print("Hola omar como andas")

saludo()

