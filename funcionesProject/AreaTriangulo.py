#Ejemplo para calcular el area de un triangulo

#Variables e entrada
base= int(input("Ingrese la base: "))
altura= int(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area= (b * a) / 2
    return area

#Invocar la funcion
resultado= calcularAreaTriangulo(base,altura)
#Salida
print(f"El area del triangulo cuya base es {base} y su altura de {altura} es {resultado}" )

#funcion con argumentos predederminados

def my_functio(country= "Colombia"):
    print("I am from " + country)

my_functio()
my_functio("Sweden")

#Argumentos Arbitarion

def mostrarEstudiantes (*args):
    print("El estudiante: "+ args[2])
mostrarEstudiantes ("Emil", "Tobias", "Linus")

#Argumentos palabras clave
def mostrarCarros (carrol, carro2, carro3):
    print("El carro es:" +carro2)

mostrarCarros(carro1 = "BMW", carro3 = "Ferrari", carro2 = "Ford")

#Argumentos Kwargs
def mostrarCliente (**kwargs):
    print("Su apellido es: "+ kwargs["apellido"])
mostrarCliente (nombre = "Tobias", apellido = "Refsnes")

def miFuncion():
    pass

#Ejemplo de uso de la funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

#Ejemolo de pow
num1 = pow(7, 4)
print(num1)

#Modulo de matematicas
import math
num3= math.ceil(7.8)
num4= math.floor(7.8)

print(num3) #returns 8
print(num4) #returns 7