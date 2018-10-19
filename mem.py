#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Simulacion de la memoria del sistema operativo con todos sus vericuetos (Asignacion continua, paginacion,
#	      ajustes y algoritmo de eleccion de victima.
#########################################################################################################################

from irqmanager import *
from kernell import *
from page_table import *
from cpu import *

reg_mem= {1000: None, 1001: None, 1002: None, 1003: None, 1004: None, 1005: None, 1006: None, 1007: None, 1008: None, 1009: None, 1010: None, 1011: None}
memory_available = {}

class Memory:
	def __init__(self):
        	self.firstMem =  None
        	self.lastMem = None

    	def esVacio(self):
        	if self.firstMem == None:
            		return True
	
        def set_cpu(self, procesador):
                self.procesador = procesador

        def set_page_table(self, pagina):
                self.pagetable = pagina

	def memory_table(self, address, inst):
#		print get_type_memory()
		global reg_mem
       		self.address = address - 1
		self.inst = inst
		for x in self.inst:
			self.address = self.address +1
			reg_mem[self.address] = x

	def memory_table_paginacion(self, address, inst, pid):
		if cpu_state():
			self.cpu = self.procesador.get_cpu()
			if self.cpu.get_pid() == pid:				
        	                self.address = address - 1
                	        self.inst = inst
                        	cont= 0
				cont_frame=0
				for x in self.inst:
					if cont <= 3:
                               			self.address = self.address +1
                               			reg_mem[self.address] = x
						cont= cont+1
		                for id in memory_available:
					if memory_available[id] == False and cont_frame == 0:
						self.elemento_tabla = PAGETABLE_ELEM(self.cpu.get_pid(), self.cpu.get_pc()/4, id, None, True)
						self.pagetable.put(self.elemento_tabla)
						memory_available[id] = True
						cont_frame = 1

	def get_memory_table(self):
        	for id in reg_mem:
	        	print id, ":" , reg_mem[id]

        def crear_tabla_libre(self):
#		set_type_memory(0)
		set_type_memory(1)
		global memory_available
		memory_available = {}
		id=1000
		cont = 0
		while id <= 1011:
			if reg_mem[id] == None:
				cont =0
				while id+cont <=1011 and reg_mem[id+cont] == None:
					cont=cont+1
					memory_available[id] = cont	
			id = id + cont

        def agregar_a_bloque(self, valor): #paginacion
       		bloque_nuevo = Memlist(valor)
        	if self.esVacio() == True:
            		self.firstMem = self.lastMem = bloque_nuevo
        	else:
            		self.lastMem.next = bloque_nuevo
            		bloque_nuevo.prev = self.lastMem
            		self.lastMem = bloque_nuevo

	def frame_memory(self):
                valor_1 = MEMFISICA(0, True, 1000)
                valor_2 = MEMFISICA(1, True, 1004)
                valor_3 = MEMFISICA(2, True, 1008)
                self.agregar_a_bloque(valor_1)
                self.agregar_a_bloque(valor_2)
                self.agregar_a_bloque(valor_3)

	def get_memory_page_list(self):
        	listita = []
         	if self.esVacio() == True:
           		 print ("Cola Vacia")
         	else:
            		validar = True
            		aux = self.firstMem
            		while (validar):
               			listita.append(aux.getValor())
               			if aux == self.lastMem:
                  			validar = False
               			else:
                  			aux = aux.next
		return listita

	def search_memoria_fisica_disponible(self):
		        validar = True
                        aux = self.firstMem
                        while (validar):
				var=aux.getValor()
				if var.get_state():
					return True
                                if aux == self.lastMem:
                                        validar = False
                                else:
                                        aux = aux.next
			return False

	def memoria_fisica_cambiar_estado(self, id):
		        validar = True
                        aux = self.firstMem
                        while (validar):
				var=aux.getValor()
				if var.get_n_frame() == id:
					var.set_state(True)
					validar = False
                                if aux == self.lastMem:
                                        validar = False
                                else:
                                        aux = aux.next


        def lista_ordenada(self):
        	listita = []
         	if self.esVacio() == True:
           		 print ("Cola Vacia")
         	else:
            		validar = True
            		aux = self.firstMem
            		while (validar):
               			listita.append(aux.getValor())
               			if aux == self.lastMem:
                  			validar = False
               			else:
                  			aux = aux.next
         	vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         	for v in vv2:
	             print (v)

	def get_memory_libre(self):
#		print "Memoria Libre raton"
        	for id in memory_available:
	        	print id, ":" , memory_available[id]

	def base_dir(self, cant_inst):
		for id in memory_available:
                        if memory_available[id] >= cant_inst:
				return id

	def set_memory_clean_reg(self,reg):
		reg_mem[reg] = None 

class Swap:
	def __init__(self):
        	self.firstSwap =  None
        	self.lastSwap = None

    	def esVacio(self):
        	if self.firstSwap == None:
            		return True

        def agregar_a_bloque(self, valor): #paginacion
       		bloque_nuevo = Memlist(valor)
        	if self.esVacio() == True:
            		self.firstSwap = self.lastSwap = bloque_nuevo
        	else:
            		self.lastSwap.next = bloque_nuevo
            		bloque_nuevo.prev = self.lastSwap
            		self.lastSwap = bloque_nuevo

	def frame_swap(self): # Cuando el swap esta en False, quire decir que esta ocupada
                valor_1 = MEMFISICA(0, True, 1000)
                valor_2 = MEMFISICA(1, True, 1004)
                valor_3 = MEMFISICA(2, True, 1008)
                valor_4 = MEMFISICA(3, True, 1012)
                valor_5 = MEMFISICA(4, True, 1016)
                valor_6 = MEMFISICA(5, True, 1020)
                self.agregar_a_bloque(valor_1)
                self.agregar_a_bloque(valor_2)
                self.agregar_a_bloque(valor_3)
                self.agregar_a_bloque(valor_4)
                self.agregar_a_bloque(valor_5)
                self.agregar_a_bloque(valor_5)

	def search_swap_disponible(self):
		        validar = True
                        aux = self.firstSwap
                        while (validar):
				var=aux.getValor()
				#print var.get_n_frame()
				#print var.get_state()
				if var.get_state():
					return True
                                if aux == self.lastSwap:
                                        validar = False
                                else:
                                        aux = aux.next
			return False

        def swap_ordenada(self):
                listita = []
                if self.esVacio() == True:
                         print ("Cola Vacia")
                else:
                        validar = True
                        aux = self.firstSwap
                        while (validar):
                                listita.append(aux.getValor())
                                if aux == self.lastSwap:
                                        validar = False
                                else:
                                        aux = aux.next
                vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
                for v in vv2:
                     print (v)



class MEMFISICA:
  def __init__(self, n_frame=None, state=None, base_dir=None):
    self.n_frame = n_frame
    self.state  = state #False: bloque ocupado, True: bloque libre
    self.base_dir = base_dir

  def set_n_frame(self, n_frame):
    self.n_frame = n_frame

  def get_n_frame(self):
    return self.n_frame

  def set_state(self, state):
    self.state = state

  def get_state(self):
    return self.state

  def set_base_dir(self, base_dir):
    self.base_dir = base_dir

  def get_base_dir(self):
    return self.base_dir

  def __str__(self):
    return "%s - %s - %s" % (self.n_frame, self.state, self.base_dir)

  
class Memlist:
  def __init__(self, MEMFISICA):
    self.valor = MEMFISICA
    self.prev  = None
    self.next  = None

  def getValor(self):
     return self.valor

  def __str__(self):
     return str(self.valor)


class MEMBLOCK:
  def __init__(self, pid=None, state=None, base_dir=None, size=None):
    self.pid = pid
    self.state  = state #False: bloque ocupado, True: bloque libre
    self.base_dir = base_dir
    self.size = size

  def set_pid(self, pid):
    self.pid = pid

  def get_pid(self):
    return self.pid

  def set_state(self, state):
    self.state = state

  def get_state(self):
    return self.state

  def set_base_dir(self, base_dir):
    self.base_dir = base_dir

  def get_base_dir(self):
    return self.base_dir

  def set_size(self, size):
    self.size = size

  def get_size(self):
    return self.size

  def __str__(self):
    return "%s - %s - %s - %s" % (self.pid, self.state, self.base_dir, self.size)

class PAGETABLE_ELEM:
  def __init__(self, pid=None, page=None, frame=None, swap=None, load=None, flag_r=None, timestamp=None):
    self.pid = pid
    self.page  = page #Numero de Pagina
    self.frame = frame #Numero de Bloque
    self.swap = swap #Posicione la memoria swap si no esta cargado
    self.load = load #True si esta memoria Fisica y false si esta en la swap
    self.flag_r = flag_r
    self.timestamp = timestamp

  def set_pid(self, pid):
    self.pid = pid

  def get_pid(self):
    return self.pid

  def set_page(self, page):
    self.page = page

  def get_page(self):
    return self.page

  def set_frame(self, frame):
    self.frame = frame

  def get_frame(self):
    return self.frame

  def set_swap(self, swap):
    self.swap = swap

  def get_swap(self):
    return self.swap

  def set_load(self, load):
    self.load = load

  def get_load(self):
    return self.load

  def set_flag_r(self, flag_r):
    self.flag_r = flag_r

  def get_flag_r(self):
    return self.flag_r

  def set_timestamp(self, timestamp):
    self.timestamp = timestamp

  def get_timestamp(self):
    return self.timestamp

  def __str__(self):
    return "%s - %s - %s - %s - %s -%s -%s" % (self.pid, self.page, self.frame, self.swap, self.load, self.flag_r, self.timestamp)


class Pagetable:
  def __init__(self, PAGETABLE_ELEM):
    self.valor = PAGETABLE_ELEM
    self.prev  = None
    self.next  = None

  def getValor(self):
     return self.valor

  def __str__(self):
     return str(self.valor)

class Bloques:
  def __init__(self, MEMBLOCK):
    self.valor = MEMBLOCK
    self.prev  = None
    self.next  = None

  def getValor(self):
     return self.valor

  def __str__(self):
     return str(self.valor)

class Paginacion:
    def __init__(self):
        self.firstBlock =  None
        self.lastBlock = None

    def esVacio(self):
        if self.firstBlock == None:
            return True

    def search_base_dir(self, dir):
         if self.esVacio() == True:
            print (" ")
         else:
            validar = True
            aux = self.firstBlock
            mem_block = aux.getValor()
            while (validar):
               if mem_block.get_base_dir() == dir:
                       return True
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

    def agregar_a_bloque(self, valor): #paginacion
        bloque_nuevo = Bloques(valor)
        if self.esVacio() == True:
            self.firstBlock = self.lastBlock = bloque_nuevo
        else:
            self.lastBlock.next = bloque_nuevo
            bloque_nuevo.prev = self.lastBlock
            self.lastBlock = bloque_nuevo

    def crear_block_list(self):
                valor_1 = MEMBLOCK(None, True, None , 4)
                valor_2 = MEMBLOCK(None, True, None , 4)
                valor_3 = MEMBLOCK(None, True, None , 4)
                self.agregar_a_bloque(valor_1)
                self.agregar_a_bloque(valor_2)
                self.agregar_a_bloque(valor_3)

    def change_block(self, size): #paginacion
	print "" #ver si se puede eliminar en paginacion no se utiliza

    def block_list_search(self, size):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
            mem_block = aux.getValor()
            while (validar):
               if mem_block.get_state() == True:
#               if mem_block.get_state() == True and mem_block.get_size() >= size:
                       return mem_block.get_base_dir()
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

    def add_block_list(self, valor): #Paginacion
	if self.esVacio() == True:
           print ("No hay Bloques")
        else:
           validar = True
	   aux = self.firstBlock
	   mem_block = aux.getValor()
           if mem_block.get_pid() != valor.get_pid():
	   	while (validar):
	      		if mem_block.get_state() == True and mem_block.get_size() >= valor.get_size():
	 	 		mem_block.set_pid(valor.get_pid())
	 	 		mem_block.set_state(valor.get_state())
	 	 		mem_block.set_base_dir(valor.get_base_dir())
	 	 		mem_block.set_size(valor.get_size())
		 		validar = False
	      		if mem_block.get_state() == True and mem_block.get_size() < valor.get_size():
	 	 		mem_block.set_pid(valor.get_pid())
	 	  		mem_block.set_state(valor.get_state())
	 	   		mem_block.set_base_dir(valor.get_base_dir())
	 	 		mem_block.set_size(mem_block.get_size())
		 		aux = aux.next
		 		mem_block = aux.getValor()
	 	 		mem_block.set_pid(valor.get_pid())
	 	 		mem_block.set_state(valor.get_state())
	 	 		mem_block.set_size(valor.get_size() - mem_block.get_size())
		 		validar = False
              		if aux == self.lastBlock:
                 		validar = False
	      		else:
	         		aux = aux.next
		 		mem_block = aux.getValor()

    def lista_ordenada(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         for v in vv2:
           if v.get_size() >= 0:
             print (v)

    def search_for_pid(self, pid):#Paginacion
         if self.esVacio() == True:
            print (" ")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_pid() == pid:
		       return mem_block.get_base_dir()
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

	

#El primer espacio disponible donde entre
class First_Fit:
    def __init__(self):
        self.firstBlock =  None
        self.lastBlock = None

    def esVacio(self):
        if self.firstBlock == None:
            return True

    def crear_block_list(self):
	valor = MEMBLOCK(None, True, 1000, len(reg_mem))  
	self.add_block_list(valor)		

    def search_base_dir(self, dir):
         if self.esVacio() == True:
            print (" ")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_base_dir() == dir:
		       return True
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

    def search_for_pid(self, pid):
         if self.esVacio() == True:
            print (" ")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_pid() == pid:
		       return mem_block.get_base_dir()
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()
        

    def add_block_list(self, valor):
        if self.search_base_dir(valor.get_base_dir()):
		print "busqueda TRUE"
		if self.esVacio() == True:
            		print ("No hay Bloques")
         	else:
            		validar = True
            		aux = self.firstBlock
            		mem_block = aux.getValor()
            		while (validar) and mem_block.get_base_dir() != valor.get_base_dir():
               			if aux == self.lastBlock:
                  			validar = False
               			else:
                  			aux = aux.next
                  			mem_block = aux.getValor()

            		if mem_block.get_base_dir() == valor.get_base_dir():
				if mem_block.get_size() == valor.get_size():
					mem_block.set_pid(valor.get_pid())
               				mem_block.set_state(False)
				else:
					print "elsesss"
					bloque = MEMBLOCK(None, True , mem_block.get_base_dir() + valor.get_size(), mem_block.get_size() - valor.get_size())
					mem_block.set_pid(valor.get_pid())
               				mem_block.set_state(False)
               				mem_block.set_size(valor.get_size())
#					bloque = MEMBLOCK(None, True , mem_block.get_base_dir() + valor.get_size(), mem_block.get_size() - valor.get_size())
					bloque_nuevo = Bloques(bloque)
					self.lastBlock.next = bloque_nuevo
					bloque_nuevo.prev = self.lastBlock
					self.lastBlock = bloque_nuevo
        else:
		#print "Busqueda FALSE"
        	new_block = Bloques(valor)
		if self.esVacio() == True:
            		self.firstBlock = self.lastBlock = new_block
        	else:
            		self.lastBlock.next = new_block
            		new_block.prev = self.lastBlock
            		self.lastBlock = new_block

    def get_next(self):
         if self.firstBlock == self.lastBlock:
            if self.firstBlock == None and self.lastBlock == None:
                return None
            aux = self.firstBlock
            self.firstBlock = None
            self.lastBlock = None
            return aux.getValor()
         else:
            aux = self.firstBlock
            self.firstBlock = self.firstBlock.next
            self.firstBlock.prev = None
            return aux.getValor()
            aux = None

    def imprimirListaDeBloques(self):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               print (aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next

    def block_list_search(self, size):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_state() == True and mem_block.get_size() >= size:
		       return mem_block.get_base_dir()
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

    def liberar_bloque(self, pid):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar) and mem_block.get_pid() != pid:
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

            if mem_block.get_pid() == pid:
       	       mem_block.set_state(True)

    def change_block(self, size):
         aux = self.firstBlock
	 mem_block = aux.getValor()
	 mem_block.set_base_dir(mem_block.get_base_dir() + size)
	 mem_block.set_size(mem_block.get_size() - size)	

    def lista_ordenada(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         for v in vv2:
	   if v.get_size() >= 0:
             print (v)

    def ordenar_memoria(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         return vv2
	 #for v in vv2:
	 #  if v.get_size() >= 0:
         #    print (v)

    def eliminarUltimo(self, list):
         if list.esVacio() == True:
            print("La lista esta Vacia, funcion inapropiada")
         elif list.firstBlock == self.lastBlock:
            list.firstBlock = None
            list.lastBlock = None
            print("El Valor fue eliminado, Lista vacia!!!")
         else:
            aux = list.lastBlock
            list.lastBlock = list.lastBlock.prev
            list.lastBlock.next = None
            aux = None
            print("Valor Eliminado")
    
    def borrar_ultimo(self):	 
         if self.firstBlock == self.lastBlock:
            self.firstBlock = None
            self.lastBlock = None
         else:
            aux = self.lastBlock
            self.lastBlock = self.lastBlock.prev
            self.lastBlock.next = None
            aux = None

    def vaciar_cola(self):
	while self.esVacio() != True:
	    self.borrar_ultimo()

    def desfragmentacion(self):
        list_defrag = []
        list_orig = self.ordenar_memoria()
	list_temp = list_orig[:]
	list_temp.pop(0)
	self.bloque = MEMBLOCK(None, False , 9999 , 0)	
	list_temp.append(self.bloque)
	cont = 0
	for x in list_orig:
		temp = list_temp[0 + cont]
		if x.get_state() == temp.get_state() and x.get_state() == True:
                        self.new_block = MEMBLOCK(None, True , x.get_base_dir(), x.get_size() + temp.get_size())
			list_defrag.append(self.new_block)
			cont = cont + 1
			list_orig.pop(cont)
			cont = cont + 1
		else:
			list_defrag.append(x)
			cont =cont + 1
	#print ("Lista resultante:", list_defrag)
	list_orig = list_defrag[:]
	for y in list_orig:
		if y.get_size() >= 0:
			print y
	return list_orig
     
    def compactar(self):
	list_a_compactar = []	
	temporal = self.desfragmentacion()
	for h in temporal:
		if h.get_size() >= 0:
			list_a_compactar.append(h)
	for x in list_a_compactar:
		if x.get_state() == True:
			list_a_compactar.remove(x)
			list_a_compactar.insert(0, x)
	list_a_compactar = self.aux_desfragmentacion(list_a_compactar)
	self.vaciar_cola()
	for y in list_a_compactar:
		self.add_block_list(y)
	
    def aux_desfragmentacion(self, list):
        list_defrag = []
	list_new = []
        list_orig = list
        list_temp = list_orig[:]
        list_temp.pop(0)
        self.bloque = MEMBLOCK(None, False , 9999 , 0)
        list_temp.append(self.bloque)
        cont = 0
	aux = 0
        for x in list_orig:
                temp = list_temp[0 + cont]
                if x.get_state() == temp.get_state() and x.get_state() == True:
			if x.get_base_dir() < temp.get_base_dir():
				self.new_block = MEMBLOCK(None, True , x.get_base_dir(), x.get_size() + temp.get_size())	
			else:
				self.new_block = MEMBLOCK(None, True , temp.get_base_dir(), x.get_size() + temp.get_size())	
                        list_defrag.append(self.new_block)
                        cont = cont + 1
                        list_orig.pop(cont)
                        cont = cont + 1
                else:
                        list_defrag.append(x)
                        cont =cont + 1
	mem = list_defrag[0]
	aux_mem = mem.get_base_dir()
	for h in list_defrag:
		self.nuevo_bloque = MEMBLOCK(h.get_pid(), h.get_state(), aux_mem, h.get_size())
		list_new.append(self.nuevo_bloque)
		aux = h.get_size()
		aux_mem = aux_mem + aux
		
        return list_new
	

#Mejor espacio disponible
class Best_Fit:
    def __init__(self):
        self.firstBlock =  None
        self.lastBlock = None

    def esVacio(self):
        if self.firstBlock == None:
            return True

    def crear_block_list(self):
	valor = MEMBLOCK(None, True, 1000, len(reg_mem))  
	self.add_block_list(valor)		

    def search_base_dir(self, dir):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_base_dir() == dir:
		       return True
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()
        

    def search_for_pid(self, pid):
         if self.esVacio() == True:
            print (" ")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_pid() == pid:
		       return mem_block.get_base_dir()
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()
        

    def add_block_list(self, valor):
        if self.search_base_dir(valor.get_base_dir()):
		print "busqueda TRUE"
		if self.esVacio() == True:
            		print ("No hay Bloques")
         	else:
            		validar = True
            		aux = self.firstBlock
            		mem_block = aux.getValor()
            		while (validar) and mem_block.get_base_dir() != valor.get_base_dir():
               			if aux == self.lastBlock:
                  			validar = False
               			else:
                  			aux = aux.next
                  			mem_block = aux.getValor()

            		if mem_block.get_base_dir() == valor.get_base_dir():
				if mem_block.get_size() == valor.get_size():
					mem_block.set_pid(valor.get_pid())
               				mem_block.set_state(False)
				else:
					bloque = MEMBLOCK(None, True , mem_block.get_base_dir() + valor.get_size(), mem_block.get_size() - valor.get_size())
					mem_block.set_pid(valor.get_pid())
               				mem_block.set_state(False)
               				mem_block.set_size(valor.get_size())
					bloque_nuevo = Bloques(bloque)
					self.lastBlock.next = bloque_nuevo
					bloque_nuevo.prev = self.lastBlock
					self.lastBlock = bloque_nuevo
        else:
		print "Busqueda FALSE"
        	new_block = Bloques(valor)
		if self.esVacio() == True:
            		self.firstBlock = self.lastBlock = new_block
        	else:
            		self.lastBlock.next = new_block
            		new_block.prev = self.lastBlock
            		self.lastBlock = new_block

    def get_next(self):
         if self.firstBlock == self.lastBlock:
            if self.firstBlock == None and self.lastBlock == None:
                return None
            aux = self.firstBlock
            self.firstBlock = None
            self.lastBlock = None
            return aux.getValor()
         else:
            aux = self.firstBlock
            self.firstBlock = self.firstBlock.next
            self.firstBlock.prev = None
            return aux.getValor()
            aux = None

    def imprimirListaDeBloques(self):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               print (aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
    
    #Busqueda de Bloque que se ajuste mejor al tamanio del nuevo proceso	
    def block_list_search(self, size):
	 var_base_dir = {}
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_state() == True and mem_block.get_size() >= size:
		       var_base_dir[mem_block.get_base_dir()] = mem_block.get_size()	
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()
	    list_orig_ord = sorted(var_base_dir.items(), key=lambda var_base_dir: var_base_dir[1])
	    for x in list_orig_ord:
                return x[0]


    def liberar_bloque(self, pid):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar) and mem_block.get_pid() != pid:
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

            if mem_block.get_pid() == pid:
       	       mem_block.set_state(True)

    def change_block(self, size):
         aux = self.firstBlock
	 mem_block = aux.getValor()
	 mem_block.set_base_dir(mem_block.get_base_dir() + size)
	 mem_block.set_size(mem_block.get_size() - size)	

    def lista_ordenada(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         for v in vv2:
	   if v.get_size() >= 0:
             print (v)

    def ordenar_memoria(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         return vv2

    def eliminarUltimo(self, list):
         if list.esVacio() == True:
            print("La lista esta Vacia, funcion inapropiada")
         elif list.firstBlock == self.lastBlock:
            list.firstBlock = None
            list.lastBlock = None
            print("El Valor fue eliminado, Lista vacia!!!")
         else:
            aux = list.lastBlock
            list.lastBlock = list.lastBlock.prev
            list.lastBlock.next = None
            aux = None
            print("Valor Eliminado")

    def borrar_ultimo(self):	 
         if self.firstBlock == self.lastBlock:
            self.firstBlock = None
            self.lastBlock = None
         else:
            aux = self.lastBlock
            self.lastBlock = self.lastBlock.prev
            self.lastBlock.next = None
            aux = None


    def vaciar_cola(self):
	while self.esVacio() != True:
	    self.borrar_ultimo()

    def desfragmentacion(self):
        list_defrag = []
        list_orig = self.ordenar_memoria()
	list_temp = list_orig[:]
	list_temp.pop(0)
	self.bloque = MEMBLOCK(None, False , 9999 , 0)	
	list_temp.append(self.bloque)
	cont = 0
	for x in list_orig:
		temp = list_temp[0 + cont]
		if x.get_state() == temp.get_state() and x.get_state() == True:
                        self.new_block = MEMBLOCK(None, True , x.get_base_dir(), x.get_size() + temp.get_size())
			list_defrag.append(self.new_block)
			cont = cont + 1
			list_orig.pop(cont)
			cont = cont + 1
		else:
			list_defrag.append(x)
			cont =cont + 1
	#print ("Lista resultante:", list_defrag)
	list_orig = list_defrag[:]
	for y in list_orig:
		if y.get_size() >= 0:
			print y
	return list_orig

    def compactar(self):
	list_a_compactar = []	
	temporal = self.desfragmentacion()
	for h in temporal:
		if h.get_size() >= 0:
			list_a_compactar.append(h)
	for x in list_a_compactar:
		if x.get_state() == True:
			list_a_compactar.remove(x)
			list_a_compactar.insert(0, x)
	list_a_compactar = self.aux_desfragmentacion(list_a_compactar)
	self.vaciar_cola()
	for y in list_a_compactar:
		self.add_block_list(y)
	
    def aux_desfragmentacion(self, list):
        list_defrag = []
	list_new = []
        list_orig = list
        list_temp = list_orig[:]
        list_temp.pop(0)
        self.bloque = MEMBLOCK(None, False , 9999 , 0)
        list_temp.append(self.bloque)
        cont = 0
	aux = 0
        for x in list_orig:
                temp = list_temp[0 + cont]
                if x.get_state() == temp.get_state() and x.get_state() == True:
			if x.get_base_dir() < temp.get_base_dir():
				self.new_block = MEMBLOCK(None, True , x.get_base_dir(), x.get_size() + temp.get_size())	
			else:
				self.new_block = MEMBLOCK(None, True , temp.get_base_dir(), x.get_size() + temp.get_size())	
                        list_defrag.append(self.new_block)
                        cont = cont + 1
                        list_orig.pop(cont)
                        cont = cont + 1
                else:
                        list_defrag.append(x)
                        cont =cont + 1
	mem = list_defrag[0]
	aux_mem = mem.get_base_dir()
	for h in list_defrag:
		self.nuevo_bloque = MEMBLOCK(h.get_pid(), h.get_state(), aux_mem, h.get_size())
		list_new.append(self.nuevo_bloque)
		aux = h.get_size()
		aux_mem = aux_mem + aux
		
        return list_new

#Peor espacio disponible
class Worst_Fit:
    def __init__(self):
        self.firstBlock =  None
        self.lastBlock = None

    def esVacio(self):
        if self.firstBlock == None:
            return True

    def crear_block_list(self):
	valor = MEMBLOCK(None, True, 1000, len(reg_mem))  
	self.add_block_list(valor)		

    def search_base_dir(self, dir):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_base_dir() == dir:
		       return True
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

    def search_for_pid(self, pid):
         if self.esVacio() == True:
            print (" ")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_pid() == pid:
		       return mem_block.get_base_dir()
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()
        
        

    def add_block_list(self, valor):
        if self.search_base_dir(valor.get_base_dir()):
		print "busqueda TRUE"
		if self.esVacio() == True:
            		print ("No hay Bloques")
         	else:
            		validar = True
            		aux = self.firstBlock
            		mem_block = aux.getValor()
            		while (validar) and mem_block.get_base_dir() != valor.get_base_dir():
               			if aux == self.lastBlock:
                  			validar = False
               			else:
                  			aux = aux.next
                  			mem_block = aux.getValor()

            		if mem_block.get_base_dir() == valor.get_base_dir():
				if mem_block.get_size() == valor.get_size():
					mem_block.set_pid(valor.get_pid())
               				mem_block.set_state(False)
				else:
					bloque = MEMBLOCK(None, True , mem_block.get_base_dir() + valor.get_size(), mem_block.get_size() - valor.get_size())
					mem_block.set_pid(valor.get_pid())
               				mem_block.set_state(False)
               				mem_block.set_size(valor.get_size())
					bloque_nuevo = Bloques(bloque)
					self.lastBlock.next = bloque_nuevo
					bloque_nuevo.prev = self.lastBlock
					self.lastBlock = bloque_nuevo
        else:
		print "Busqueda FALSE"
        	new_block = Bloques(valor)
		if self.esVacio() == True:
            		self.firstBlock = self.lastBlock = new_block
        	else:
            		self.lastBlock.next = new_block
            		new_block.prev = self.lastBlock
            		self.lastBlock = new_block

    def get_next(self):
         if self.firstBlock == self.lastBlock:
            if self.firstBlock == None and self.lastBlock == None:
                return None
            aux = self.firstBlock
            self.firstBlock = None
            self.lastBlock = None
            return aux.getValor()
         else:
            aux = self.firstBlock
            self.firstBlock = self.firstBlock.next
            self.firstBlock.prev = None
            return aux.getValor()
            aux = None

    def imprimirListaDeBloques(self):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               print (aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
    
    #Busqueda de Bloque que se el mas grande de tamanio que el nuevo proceso	
    def block_list_search(self, size):
	 var_base_dir = {}
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar):
	       if mem_block.get_state() == True and mem_block.get_size() >= size:
		       var_base_dir[mem_block.get_base_dir()] = mem_block.get_size()	
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()
	    list_orig_ord = sorted(var_base_dir.items(), key=lambda var_base_dir: var_base_dir[1], reverse=True)
	    for x in list_orig_ord:
                return x[0]


    def liberar_bloque(self, pid):
         if self.esVacio() == True:
            print ("No hay Bloques")
         else:
            validar = True
            aux = self.firstBlock
	    mem_block = aux.getValor()
            while (validar) and mem_block.get_pid() != pid:
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
                  mem_block = aux.getValor()

            if mem_block.get_pid() == pid:
       	       mem_block.set_state(True)

    def change_block(self, size):
         aux = self.firstBlock
	 mem_block = aux.getValor()
	 mem_block.set_base_dir(mem_block.get_base_dir() + size)
	 mem_block.set_size(mem_block.get_size() - size)	

    def lista_ordenada(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         for v in vv2:
	   if v.get_size() >= 0:
             print (v)

    def ordenar_memoria(self):
         listita = []
         if self.esVacio() == True:
            print ("Cola Vacia")
         else:
            validar = True
            aux = self.firstBlock
            while (validar):
               listita.append(aux.getValor())
               if aux == self.lastBlock:
                  validar = False
               else:
                  aux = aux.next
         vv2 = sorted(listita, key=lambda objeto: objeto.base_dir, reverse=False)
         return vv2

    def eliminarUltimo(self, list):
         if list.esVacio() == True:
            print("La lista esta Vacia, funcion inapropiada")
         elif list.firstBlock == self.lastBlock:
            list.firstBlock = None
            list.lastBlock = None
            print("El Valor fue eliminado, Lista vacia!!!")
         else:
            aux = list.lastBlock
            list.lastBlock = list.lastBlock.prev
            list.lastBlock.next = None
            aux = None
            print("Valor Eliminado")

    def borrar_ultimo(self):	 
         if self.firstBlock == self.lastBlock:
            self.firstBlock = None
            self.lastBlock = None
         else:
            aux = self.lastBlock
            self.lastBlock = self.lastBlock.prev
            self.lastBlock.next = None
            aux = None

    def vaciar_cola(self):
	while self.esVacio() != True:
	    self.borrar_ultimo()


    def desfragmentacion(self):
        list_defrag = []
        list_orig = self.ordenar_memoria()
	list_temp = list_orig[:]
	list_temp.pop(0)
	self.bloque = MEMBLOCK(None, False , 9999 , 0)	
	list_temp.append(self.bloque)
	cont = 0
	for x in list_orig:
		temp = list_temp[0 + cont]
		if x.get_state() == temp.get_state() and x.get_state() == True:
                        self.new_block = MEMBLOCK(None, True , x.get_base_dir(), x.get_size() + temp.get_size())
			list_defrag.append(self.new_block)
			cont = cont + 1
			list_orig.pop(cont)
			cont = cont + 1
		else:
			list_defrag.append(x)
			cont =cont + 1
	#print ("Lista resultante:", list_defrag)
	list_orig = list_defrag[:]
	for y in list_orig:
		if y.get_size() >= 0:
			print y
	return list_orig


    def compactar(self):
	list_a_compactar = []	
	temporal = self.desfragmentacion()
	for h in temporal:
		if h.get_size() >= 0:
			list_a_compactar.append(h)
	for x in list_a_compactar:
		if x.get_state() == True:
			list_a_compactar.remove(x)
			list_a_compactar.insert(0, x)
	list_a_compactar = self.aux_desfragmentacion(list_a_compactar)
	self.vaciar_cola()
	for y in list_a_compactar:
		self.add_block_list(y)
	
    def aux_desfragmentacion(self, list):
        list_defrag = []
	list_new = []
        list_orig = list
        list_temp = list_orig[:]
        list_temp.pop(0)
        self.bloque = MEMBLOCK(None, False , 9999 , 0)
        list_temp.append(self.bloque)
        cont = 0
	aux = 0
        for x in list_orig:
                temp = list_temp[0 + cont]
                if x.get_state() == temp.get_state() and x.get_state() == True:
			if x.get_base_dir() < temp.get_base_dir():
				self.new_block = MEMBLOCK(None, True , x.get_base_dir(), x.get_size() + temp.get_size())	
			else:
				self.new_block = MEMBLOCK(None, True , temp.get_base_dir(), x.get_size() + temp.get_size())	
                        list_defrag.append(self.new_block)
                        cont = cont + 1
                        list_orig.pop(cont)
                        cont = cont + 1
                else:
                        list_defrag.append(x)
                        cont =cont + 1
	mem = list_defrag[0]
	aux_mem = mem.get_base_dir()
	for h in list_defrag:
		self.nuevo_bloque = MEMBLOCK(h.get_pid(), h.get_state(), aux_mem, h.get_size())
		list_new.append(self.nuevo_bloque)
		aux = h.get_size()
		aux_mem = aux_mem + aux
		
        return list_new

