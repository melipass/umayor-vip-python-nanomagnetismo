#Ejercicio 1:
"""
De que otra forma se puede escribir el código
if edad<30:
    print('Aún es joven')
elif edad>50:
    print('Es de la tercera edad')
else:
    print('No es tan viejo')
    para obtener el mismo resultado?
"""
#Idea: Rotar las variables.

edad = int(input('Ingrese su edad: '))

if edad>50:
    print('Es de la tercera edad')
elif edad>30: #Llego a esta condicional solo si la anterior es False
    print('No es tan viejo')
else:
    print('Aún es joven')