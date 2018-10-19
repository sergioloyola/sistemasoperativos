class PCB:
  def __init__(self, pid=None, state=None, date=None, priority=None, burst_time=None, pc=None, basedir=None, inst=None):
    self.pid = pid
    self.state  = state
    self.date = date
    self.priority = priority
    self.burst_time = burst_time
    self.pc = pc
    self.basedir = basedir
    self.inst = inst

  def set_state(self, state):
    self.state = state
 
  def set_burst_time(self, state):
    self.burst_time = state

  def get_burst_time(self):
    return self.burst_time

  def set_pid(self, pid):
    self.pid = pid

  def get_pid(self):
    return self.pid

  def get_basedir(self):
    return self.basedir

  def get_inst(self):
    return self.inst

  def __str__(self):
    return "%s - %s - %s - %s - %s - %s - %s - %s" % (self.pid, self.state, self.date, self.priority, self.burst_time, self.pc, self.basedir, self.inst)

class Node:
  def __init__(self, PCB):
    self.valor = PCB
    self.prev  = None
    self.next  = None

  def getValor(self):
     return self.valor

  def __str__(self):
     return str(self.valor)

class queue:
    def __init__(self):
        self.firstNode =  None
        self.lastNode = None

    def esVacio(self):
        if self.firstNode == None:
            return True

    def put_ready(self, valor):
        node_nuevo = Node(valor)
	if self.esVacio() == True:
            self.firstNode = self.lastNode = node_nuevo
        else:
            self.lastNode.next = node_nuevo
            node_nuevo.prev = self.lastNode
            self.lastNode = node_nuevo

    def agregarFinal(self, valor):
        node_nuevo = Node(valor)
        if self.esVacio() == True:
            self.firstNode = self.lastNode = nodo_nuevo
        else:
            self.lastNode.next = node_nuevo
            node_nuevo.prev = self.lastNode
            self.lastNode = node_nuevo



    def get_next(self):
         if self.firstNode == self.lastNode:
            if self.firstNode == None and self.lastNode == None:
		#print ("Feo")
		return None

            aux = self.firstNode
            self.firstNode = None
            self.lastNode = None
            return aux.getValor()
         else:
            aux = self.firstNode
            self.firstNode = self.firstNode.next
            self.firstNode.prev = None
            return aux.getValor()
            aux = None

    def get_prev(self):
	if self.firstNode == self.lastNode:
            if self.firstNode == None and self.lastNode == None:
                return None

            aux = self.firstNode
            self.firstNode = None
            self.lastNode = None
            return aux.getValor()
        else:
            aux = self.firstNode
            self.firstNode = self.firstNode.prev
#            self.firstNode.prev = None
            return aux.getValor()
            aux = None


    def get_pcb(self):
         if self.firstNode == self.lastNode:
            if self.firstNode == None and self.lastNode == None:
		#print ("Feo")
		return None

            aux = self.firstNode
            self.firstNode = None
            self.lastNode = None
            return aux.getValor()
         else:
            aux = self.firstNode
            #self.firstNode = self.firstNode.next
            #self.firstNode.prev = None
            return aux.getValor()
            aux = None

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

    def get_ultimo(self):
	if self.esVacio() == True:
		return None
	else:
		return self.lastNode

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
               if aux != None:
                  print (aux.getValor())
               else:
                  validar = False

    def imprimirOrdenado_pid(self):
         listita = []
	 print "PID" +"  STATE  " +"  DATE" +"   PRIORITY" + " BURST_TIME"
	 print "-----------------------------------------"
         if self.esVacio() == True:
            print ("Lista Vacia")
         else:
            validar = True
            aux = self.firstNode
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastNode:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.pid, reverse=False)
         for v in vv2:
           print (v)
    def queue_ordenada(self):
         listita = []
         if self.esVacio() == True:
            print ("Lista Vacia")
         else:
            validar = True
            aux = self.firstNode
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastNode:
                  validar = False
               else:
                  aux = aux.next
	 return listita

    def imprimirOrdenado_burst(self):
         listita = []
	 print "PID" +"  STATE  " +"  DATE" +"   PRIORITY" + " BURST_TIME"
	 print "-----------------------------------------"
         if self.esVacio() == True:
            print ("Lista Vacia")
         else:
            validar = True
            aux = self.firstNode
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastNode:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.burst_time, reverse=False)
         for v in vv2:
           print (v)

    def imprimirOrdenado_priority(self):
         listita = []
	 print "PID" +"  STATE  " +"  DATE" +"   PRIORITY" + " BURST_TIME"
	 print "-----------------------------------------"
         if self.esVacio() == True:
            print ("Lista Vacia")
         else:
            validar = True
            aux = self.firstNode
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastNode:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.priority, reverse=False)
         for v in vv2:
           print (v)

