#UTF-8
# Ejercicio 1 
"""
Escriba un programa que pida las calificaciones de 5 alumnos,
3 calificaciones por alumno.
"""
listaAlumnos = []
cantidadDeNotas = 5

class AlumnoFor:
    def __init__(self):
        self.nombre = ""
        self.__notas = []
    def agregarNota(self, nota):
        self.__notas.append(nota)
    def mostrarNotas(self):
        i=1
        for x in self.__notas:
            print("La nota",str(i),"de",self.nombre,"es",str(x))
            i += 1

class AlumnoWhile:
    def __init__(self):
        self.nombre = ""
        self.__notas = []
    def agregarNota(self, nota):
        self.__notas.append(nota)
    def mostrarNotas(self):
        i=0
        while i != len(self.__notas):
            print("La nota",str(i+1),"de",self.nombre,"es",str(self.__notas[i]))
            i += 1

def PedirNotasFor(cantidadDeAlumnos):
    for x in range(1, int(cantidadDeAlumnos) + 1):
        globals()["Alumno"+str(x)] = AlumnoFor()
        globals()["Alumno"+str(x)].nombre = "Alumno " + str(x)
        listaAlumnos.append(globals()["Alumno"+str(x)])
    for alumno in listaAlumnos:
        print("\n***** " + alumno.nombre + " *****")
        for nota in range(0,cantidadDeNotas):
            alumno.agregarNota(float(input("Ingresar nota " + str(nota+1) +
                                         " para el " + alumno.nombre + ": ")))

def PedirNotasWhile(cantidadDeAlumnos):
    x = 0
    while x != (int(cantidadDeAlumnos) + 1):
        globals()["Alumno"+str(x+1)] = AlumnoWhile()
        globals()["Alumno"+str(x+1)].nombre = "Alumno " + str(x+1)
        listaAlumnos.append(globals()["Alumno"+str(x+1)])
        x += 1
    alumnoActual = 0
    while alumnoActual != (len(listaAlumnos)-1):
        notaActual = 0
        while notaActual != cantidadDeNotas:
            listaAlumnos[alumnoActual].agregarNota(float(input("Ingresar nota "
                                                               + str(notaActual+1) +
                                                               " para el "
                                                               + listaAlumnos[alumnoActual].nombre + ": ")))
            notaActual += 1
        alumnoActual += 1
        
metodo = input("¿Desea ingresar notas usando For (1) o usando While (2)?"
               + "\nIngrese el nombre o número correspondiente: ").lower()
if metodo == "for" or metodo == "1":
    PedirNotasFor(input("Ingrese la cantidad de alumnos: "))
elif metodo == "while" or metodo == "2":
    PedirNotasWhile(input("Ingrese la cantidad de alumnos: "))
else:
    print("Vuelva a intentarlo.")