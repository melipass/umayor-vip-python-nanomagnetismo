#Ejercicio 2
"""
Escriba un programa que detecte si una letra es una vocal.
"""

vocales = 'aeiou'
print("Ingrese una letra para identificar si es vocal.")
try:
    letra = str(input("Letra: ")).lower()
    assert len(letra) == 1
    if letra in vocales:
        print("Es vocal.")
    else:
        print("No es vocal")
except AssertionError:
    if len(letra) == 0:
        print('No ingresó la letra. Vuelva a intentarlo.')
    else:
        print("Debe ingresar una sola letra. Vuelva a intentarlo.")
except:
    print("Error en el valor ingresado.")