class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando ..............")

nombre = input("Su nombre es : ")
edad = input("Digite cuantos años tienes : ")
grado = input("Diga su grado : ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE : \n\n
      NOMBRE : {estudiante.nombre} \n
      EDAD : {estudiante.edad} \n
      GRADO : {estudiante.grado} \n
     """)

while True:
    estudiar = input("estas estudiando : estudiar , algo , todavia no : ")
    if(estudiar.lower() == "estudiar"):
       estudiante.estudiar()
    elif(estudiar.lower() == "algo"):
        print("Aun no estas estudiando ...")
    else:
        print("Y por que no estudias")
    

