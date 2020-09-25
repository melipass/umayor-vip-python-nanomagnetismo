#Ejercicio 2:
"""
Escriba un código que pida un número del 1 al 10 y lo imprima en pantalla como cadena
(’uno’,’dos’,etc).
"""
#Idea: Buscar en un arreglo con el texto correspondiente a cada número.

numeros = ['uno','dos','tres','cuatro','cinco',
           'seis','siete','ocho','nueve','diez']

try:
    numero = int(input('Escriba un número entre 1 y 10: '))
    assert numero <=10
    assert numero >=1
    print(numeros[numero-1])
except AssertionError:
    print('Error: El número debe estar entre 1 y 10.')
except:
    print('Error: Entrada incorrecta.')
    
#Ejercicio 3:
"""
Modifique el ejercicio anterior para que imprima un mensaje de error si el número no esta entre
1 y 10.
"""
#Hice esto en el desarrollo del 2, por lo tanto mantendré un mismo archivo para ambos.