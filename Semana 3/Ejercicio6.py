#Ejercicio 6:
"""
 Escriba un programa que cumpla con los siguientes requisitos:
 Tome una variable costo por teclado.
 Imprima la cadena ’Eso esta barato’ cuando costo sea menor a 1000.
 Imprima la cadena ’Eso esta a buen precio’ cuando costo sea mayor o igual a 1000,
pero menor o igual a 3000.
 Imprima la cadena ’Eso esta caro’ cuando costo sea mayor a 3000.
 La parte de la cadena ’Eso esta’ solo puede aparecer una vez de manera expl´ıcita dentro
del código.
"""
def ImprimirMensaje(costo):
    if costo > 3000:
        cualidad = "caro."
    elif costo < 1000:
        cualidad = "barato."
    else:
        cualidad = "a buen precio."
    print("Eso está",cualidad)

try:
    costo = int(input("Ingrese el costo: "))
    assert costo > 0
    ImprimirMensaje(costo)
except AssertionError:
    print("El costo debe ser positivo. Vuelva a ejecutar el programa.")
except:
    print("Valor ingresado no es un número entero.")