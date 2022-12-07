#Creamos la clase Gráfica 
class Grafica:

    #Constructor de la clase
    def _init_(self, numero_de_nodos):
        self.numero_nodos = numero_de_nodos     #número de nodos que tendrá la clase 
        self.grafica = []                       #lista para almacenar las aristas ?

    #Método para añadir aristas 
    def anade_arista(self, primer_nodo, segundo_nodo, peso):
        self.grafica.append([primer_nodo, segundo_nodo, peso]) #añadimos aristas a nuestro arreglo que representa la gráfica


    #Método recursivo para encontrar la raíz del subárbol al que pertenece un nodo i dado 
    # @returns raiz del nodo i 
    def encuentra_raiz(self, padre, i):
        if padre[i] == i:
            return i
        return self.encuentra_raiz(padre, padre[i])

    #Conecta a los subárboles que contienen a los nodos x e y, conecta el subárbol más chico al subárbol más grande
    def conecta_subarboles(self, padre, tamano_subarboles, x, y):
        raiz_x = self.encuentra_raiz(padre, x)
        raiz_y = self.encuentra_raiz(padre, y)
        if tamano_subarboles[raiz_x] < tamano_subarboles[raiz_y]:
            padre[raiz_x] = raiz_y
        elif tamano_subarboles[raiz_y] > tamano_subarboles[raiz_x]:
            padre[raiz_y] = raiz_x 
        else:
            padre[raiz_y] = raiz_x 
            tamano_subarboles[raiz_x] += 1             
        

