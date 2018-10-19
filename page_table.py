#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Simulacion de la tabla de paginacion.
#########################################################################################################################

from irqmanager import *
from kernell import *
from mem import *

fifo = []
second_chance = []
LRU = []

class page_table:

        def __init__(self):
                self.page_table = {}

        def put(self, element):
		global fifo
		global second_chance
		global LRU
		self.fifo = fifo
		self.second_chance = second_chance
		self.LRU = LRU
		self.elemento = element
		cont = self.elemento.get_pid() * 100 + self.elemento.get_page()
	        self.page_table.setdefault(cont, self.elemento)
		self.fifo.append(cont)
		self.second_chance.append([cont,1])
		self.LRU.append([cont,self.elemento.get_timestamp()])

	def get_fifo(self):
		return self.fifo

	def get_second_chance(self):
		return self.second_change

	def get_LRU(self):
		return self.LRU

	def get_replace_element(self):
		cont=0
		while cont != 2:
			self.imprimir_second_chance()
			elemento = 0
                	for v in self.second_chance:
	                	if v[1] == 0:
					result = v[0]
					self.second_chance.append(v)
					self.second_chance.pop(elemento)
					print ("Imprimo Segunda Chance:", v[0])
        	                	return result
                        	else:
                                	v[1] = 0
				elemento = elemento + 1
			cont=cont +1

	def get_replace_element_LRU(self):
		elemento = 0
               	for v in self.second_chance:
			result = v[0]
			self.second_chance.append(v)
			self.second_chance.pop(elemento)
		#	print ("Imprimo Segunda Chance:", v[0])
                       	return result
			elemento = elemento + 1

	def imprimir_fifo(self):
		for v in self.fifo:
			print v		

	def imprimir_LRU(self):
		for v in self.LRU:
			print v		

	def imprimir_second_chance(self):
		for v in self.second_chance:
			print v		
		
        def get_all(self):
	        for id in self.page_table:
                        print self.page_table[id]
        def get_value(self, id):
                return self.pcb_table[id]

        def set_page_element(self, id, swap, state):
                var = self.page_table[id]
		var.set_swap(swap)
		var.set_load(state)
		return var.get_frame()

        def set_page_timestamp(self, id, swap, state):
                var = self.page_table[id]
		var.set_swap(swap)
		var.set_load(state)
		return var.get_frame()

        def get_list_key(self):
                return self.page_table.keys()

        def eliminar_key(self, id):
                self.pcb_table.pop(id, None)

	def existe_pageID(self, valor):
		self.resul = True
		for id in self.page_table:
			self.elemento_tabla = self.page_table[id]
#			print ("Elemento: ", self.elemento_tabla)
			if self.elemento_tabla.get_pid() == valor.get_pid() and self.elemento_tabla.get_page() == valor.get_page():
				self.resul = False
				return self.resul
		return self.resul
