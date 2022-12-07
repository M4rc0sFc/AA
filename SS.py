#Importas módulo random y collections
import random 
import collections 
from collections import deque

def main():
    #Declaras la secuencia ciclica como una lista
    secuenciaCiclic = []

    #Preguntas por la longitud de la lista, es necesario hacer un casting a enteros
    longitud = int(input("Inserta un número entero positivo para la longitud de la secuencia cíclica:"))

    #Anexamos los valores a la lista secuenciaCiclic desde el 0 hasta la longitud
    for i in range(0,longitud):
        secuenciaCiclic.append(random.randint(0,100));

    #Ordenamos la lista
    secuenciaCiclic.sort()

    #Declaramos el objeto item de tipo deque
    item = deque(secuenciaCiclic)
    item.rotate(random.randint(0,longitud))  #Rota la lista a la derecha para resolver la secuencia ciclica, en este momento item contiene una secuencia ciclica ordenada

    print(item)
    print(min(item))

    resultado = BusquedaIM(item, longitud-1)
    print(resultado)


def BusquedaIM(listaSCO, longitud):
    p = busquedaIndice(1, longitud, listaSCO)
    return p
    
def busquedaIndice(indiceIzq, indiceDer, listaSCO):
    if(indiceIzq == indiceDer): return indiceIzq;
    else:
        mitad = (indiceIzq + indiceDer) // 2
        if(listaSCO[mitad] < listaSCO[indiceDer]):
            return busquedaIndice(indiceIzq, mitad, listaSCO)
        else:
            return busquedaIndice(mitad + 1, indiceDer, listaSCO)


main()
