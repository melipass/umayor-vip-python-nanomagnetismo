# -*- coding: utf-8 -*-
# Ejercicio 2 Semana 7
"""
Construir una función que convierta kilómetros en millas y otra que
convierta euros en dólares.
"""
import requests

def ConvertirEURaUSD(valorEnEuro):
    #API key en https://www.alphavantage.co/support/#api-key
	#Para leer desde archivo local:
    #api_file = open("D:\\Universidad\\S08 - 2020\\VIP\\api_key_alphavantage_co.txt", 'r')
    #api_key = str(api_file.read()) #obtener del link arriba
    #api_file.close()
    api_key = ""
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


print("Bienvenido. Debe elegir un tipo de conversión."
      "\nPara convertir de kilómetros a millas, ingrese 1."
      "\nPara convertir de euros a dólares, ingrese 2.")
try:
    tipoDeConversion = input("Tipo de conversión: ")
    if tipoDeConversion == "1":
        kilometros = float(input("Ingrese el número de kilómetros: "))
        millas = ConvertirKMaMillas(kilometros)
        print("Al convertir, son " + f"{millas:.2f}"  + " millas.")
    elif tipoDeConversion == "2":
        euros = float(input("Ingrese el valor en euros: "))
        dolares = ConvertirEURaUSD(euros)
        print("El valor en dólares es USD$" + f"{dolares:.2f}")
    else:
        raise Exception
except:
    print("El valor ingresado es incorrecto. Vuelva a intentarlo.")