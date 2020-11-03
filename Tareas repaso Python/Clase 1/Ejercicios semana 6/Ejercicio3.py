# Ejercicio 3
"""
 Considere el siguiente algoritmo: se inicia con un número entero n. Si n es par, se divide entre 2.
Si n es impar, se multiplica por 3 y se le suma 1. Al número que resulta, se le aplica nuevamente
el proceso hasta que se llega al número 1. Escriba un programa que aplique este proceso a un
número entero, y que muestre cuantos pasos se necesitaron para llegar al 1.
"""



n = float(input("Ingrese número: "))
pasosWhile = 0
while int(n) != 1:
    if n%2 == 0:
        n /= 2
        print(str(n))
        pasosWhile += 1
    else:
        n = (n*3)+1
        print(str(n))
        pasosWhile += 1
print("Los pasos necesarios para esto fueron " + str(pasosWhile))

#Por ahora no se me ocurre la lógica para hacerlo con un for.