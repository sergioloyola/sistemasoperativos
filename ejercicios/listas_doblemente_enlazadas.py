############################################################################
#Autor: Loyola Sergio
#Materia: Sistemas operativos 1 Cuatrimestre 2016
#Fecha: 30/03/2016
############################################################################
class Node:
  def __init__(self, valor=None):
    self.valor = valor
    self.prev  = None
    self.next  = None

  #def __str__(self):
  def getValor(self):   
     return str(self.valor) 

class List:
    def __init__(self):
        self.firstNode =  None
        self.lastNode = None

    def esVacio(self):
        if self.firstNode == None:
            return True 

    def agregarInicio(self, valor):
        nodo_nuevo = Node(valor)
	if self.esVacio() == True:
            self.firstNode = self.lastNode = nodo_nuevo
        else:
            nodo_nuevo.next = self.firstNode
            self.firstNode.next = nodo_nuevo
            self.firstNode = nodo_nuevo	 	
    
    def agregarFinal(self, valor):
        node_nuevo = Node(valor)
	if self.esVacio() == True:
            self.firstNode = self.lastNode = nodo_nuevo
        else:
            self.lastNode.next = node_nuevo
            node_nuevo.prev = self.lastNode
            self.lastNode = node_nuevo           
    
    def eliminarPrimero(self):
         if self.esVacio() == True:
            print("La lista esta Vacia, funcion inapropiada")
         elif self.firstNode == self.lastNode:
            self.firstNode = None
            self.lastNode = None
            print("El Valor fue eliminado, Lista vacia!!!")
         else:
            aux = self.firstNode
            self.firstNode = self.firstNode.next
            self.firstNode.prev = None
            aux = None
            print("Valor Eliminado")

    def eliminarUltimo(self):
         if self.esVacio() == True:
            print("La lista esta Vacia, funcion inapropiada")
         elif self.firstNode == self.lastNode:
            self.firstNode = None
            self.lastNode = None
            print("El Valor fue eliminado, Lista vacia!!!")
         else:
            aux = self.lastNode
            self.lastNode = self.lastNode.prev
            self.lastNode.next = None
            aux = None
            print("Valor Eliminado")

    def imprimirListaPrimeroUltimo(self):
         if self.esVacio() == True:
            print ("Lista Vacia")
         else:
            validar = True
            aux = self.firstNode
            while (validar):
               print (aux.getValor())
               if aux == self.lastNode:
                  validar = False
               else:
                  aux = aux.next

    def imprimirListaUltimoPrimero(self):
         if self.esVacio() == True:
            print ("Lista Vacia")
         else:
            validar = True
            aux = self.lastNode
            print (aux.getValor())
            while (validar):
               aux = aux.prev
#               if aux != self.firstNode:
               if aux != None:
                  print (aux.getValor())
               else:
                  validar = False
	

    def imprimir(self):
        nodo = self.firstNode
        while nodo != None:
            print nodo.valor
            nodo=nodo.next

lista = List()
lista.agregarInicio(1)
lista.agregarInicio(8)
#lista.agregarSiguiente(2)
lista.agregarFinal(3)
lista.agregarFinal(5)
#lista.eliminarPrimero()
#lista.eliminarUltimo()
#lista.imprimirListaPrimeroUltimo()
lista.imprimirListaUltimoPrimero()
#lista.imprimir()


