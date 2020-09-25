# Ejercicio 1
"""
Modifique el código para que los elementos de la lista se muestren en
una linea, separados por comas.
"""

#Código original:
"""
ingredientes_hechizero=['patas de araña','anca de rana','ojo de salamandra',
                        'ala de murcielago','baba de caracol','piel de serpiente']
for i in ingredientes_hechizero:
    print(i)
"""

print("**** Probando la versión for: ****")
ingredientes_hechizero=['patas de araña','anca de rana','ojo de salamandra',
                        'ala de murcielago','baba de caracol','piel de serpiente']
for i in ingredientes_hechizero:
    if i == ingredientes_hechizero[-1]:
        print(i + ".")
    else:
        print(i + ", ", end="")

print("\n**** Probando la versión while: ****")        
x=0        
while x != len(ingredientes_hechizero):
    if ingredientes_hechizero[x] == ingredientes_hechizero[-1]:
        print(ingredientes_hechizero[x] + ".")
    else:
        print(ingredientes_hechizero[x] + ", ", end="")
    x += 1