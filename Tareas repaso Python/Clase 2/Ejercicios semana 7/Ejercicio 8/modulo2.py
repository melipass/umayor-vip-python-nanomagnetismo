# -*- coding: utf-8 -*-
# Ejercicio 8 módulo 2
"""
 Separe las funciones creadas en tareas anteriores en tr´ es módulos diferentes. Escriba un progra-
ma que incluya los tres módulos, cada uno utilizando una forma de import diferente (normal,
abreviado, importar función directamente), y haga uso de las funciones de cada módulo.
"""
import sys
import requests
from random import randint

def NumeroMenor(num1, num2):
    try:
        assert num1 < num2
        return num1
    except AssertionError:
        return num2
    except:
        print("Error de cálculo. Revisar valores.")
        return -1
    
def ConvertirEURaUSD(valorEnEuro):
    #API key en https://www.alphavantage.co/support/#api-key
    api_file = open("D:\\Universidad\\S08 - 2020\\VIP\\api_key_alphavantage_co.txt", 'r')
    api_key = str(api_file.read()) #obtener del link arriba
    api_file.close()
    url = (r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        "&from_currency=EUR&to_currency=USD&apikey=" + api_key)
    solicitud = requests.get(url)
    datosSolicitud = solicitud.json()
    tasaDeCambio = float(datosSolicitud["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    valorEnDolar = valorEnEuro * tasaDeCambio
    return valorEnDolar
def ConvertirKMaMillas(km):
    valorEnMillas = km * 0.621371
    return valorEnMillas

def Factorial(lista):
    for x in lista:
        factorial = x
        while x != 1:
            x -= 1
            factorial *= x
        yield factorial

def GenerarSerieImpares(n):
    try:
        assert n % 2 == 1
    except AssertionError:
        sys.exit("Error: El número no es par")
    i = 1
    yield i
    while i != n:
        i += 2
        yield i
 
def ImprimirSerieImpares(n, operador):
    valores = list(GenerarSerieImpares(n))
    for x in valores[:-1]:
        print(str(x) + " " + operador + " ", end="")
    print(valores[-1])
    return
            
def CalcularSuma(n):
    valores = list(GenerarSerieImpares(n))
    i = 0
    for x in valores:
        i += x
    return i

def CalcularMultiplicacion(n):
    valores = list(GenerarSerieImpares(n))
    i = 1
    for x in valores:
        i *= x
    return i

def TransformarANumerosRomanos(numero):
    centenas = numero // 100
    centenasRomanas = ["C", "D", "M"]
    decenas = (numero - centenas*100) // 10
    decenasRomanas = ["X", "L", "C"]
    unidades = numero - centenas*100 - decenas*10
    unidadesRomanas = ["I", "V", "X"]
    numeroADevolver = (ArmarNumero(centenas, centenasRomanas)
                       + ArmarNumero(decenas, decenasRomanas)
                       + ArmarNumero(unidades, unidadesRomanas))
    return numeroADevolver
        
def ArmarNumero(numero, letras):
    if numero == 9:
        return letras[0] + letras[2]
    elif numero == 4:
        return letras[0] + letras[1]
    elif numero == 5:
        return letras[1]
    elif numero < 4:
        return letras[0] * numero
    else:
        numero -= 5
        return letras[1] + letras [0] * numero
    
def GenerarTresNumeros():
    uno = randint(0,100)
    dos = randint(0,100)
    tres = randint(0,100)
    return [str(uno), str(dos), str(tres)]