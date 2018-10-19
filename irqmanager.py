#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: En este elemento se implemento la emulacion de las interrupciones que existen en un sistemas opertativo
#########################################################################################################################

import time
from pcb_table import *
from kernell import *
from programas import *
from disco import *
from queue import *
from mem import *
from dispacher import *
from page_table import *

class InterruptionManager:

	def set_dispach(self, puntero):
		self.dispach = puntero

	def set_PcbTable(self, pcbTable):
		self.pcbtable = pcbTable

	def set_Memory(self, memory):
		self.memory = memory

	def set_queue_ready(self, queue):
		self.queue_ready = queue

	def set_queue_waiting(self, queue):
		self.queue_waiting = queue

	def set_schedule(self, tarea):
		self.tarea = tarea

	def set_memory_block(self, bloque):
		self.bloque = bloque

        def set_page_table(self, pagina):
                self.pagetable = pagina

        def set_swap(self, swap):
                self.swap = swap

	def new(self, inst):
 		if get_type_memory() == 0:
			self.inst = inst
			self.base_dir = self.bloque.block_list_search(len(self.inst))
			if self.base_dir != None:
				self.var_mem = PCB(inc_pid(), "New",  time.strftime("%d%m%y"), len(self.inst), 15, 0, self.bloque.block_list_search(len(self.inst)), self.inst)
				self.bloque.change_block(len(self.inst))
				self.var_bloque = MEMBLOCK(self.var_mem.get_pid(), False , self.var_mem.get_basedir(), len(self.inst))
				self.bloque.add_block_list(self.var_bloque)
				self.var_mem.set_state("Ready")
				self.queue_ready.put_ready(self.var_mem)
				self.pcbtable.put(inc_id(), self.var_mem)
				self.tarea.put_cpu() #Esto venia despues de self.memory.memory_table, lo cambie para paginacion
				self.memory.memory_table(self.var_mem.get_basedir(), self.var_mem.get_inst())
			else:
				print "No hay memoria Disponible"
		else:
			self.inst = inst
			self.var_mem = PCB(inc_pid(), "New",  time.strftime("%d%m%y"), len(self.inst), 15, 0, None, self.inst)
			self.var_mem.set_state("Ready")
                        self.queue_ready.put_ready(self.var_mem)

	def timeout(self):
		self.pcb = self.dispach.take_cpu()
		self.queue_ready.agregarFinal(self.pcb)
		self.pcbtable.eliminar_key(self.pcb.get_pid())
		self.pcbtable.put(self.pcb.get_pid(), self.pcb)
		self.dispach.sacar_cpu()
		#Agregado para Schedule Priority
		self.tarea.set_queue_ready(self.queue_ready)
		#Fin de lo agregado para Schedule Priority
		self.tarea.put_cpu()


	def io(self):
		self.pcb = self.dispach.take_cpu()
		self.pcb.set_state("I/O")
		self.queue_waiting.agregarFinal(self.pcb)
		self.pcbtable.eliminar_key(self.pcb.get_pid())
		self.pcbtable.put(self.pcb.get_pid(), self.pcb)
		self.dispach.sacar_cpu()
		self.tarea.put_cpu()
		set_cpu_state(False)

	def io_end(self):
		self.tarea.waiting_to_ready()		

	def kill(self):
		self.pcb = self.dispach.take_cpu()
		self.pcb.set_state("Terminado")
		self.pcbtable.eliminar_key(self.pcb.get_pid())
		self.pcbtable.put(self.pcb.get_pid(), self.pcb)
		self.dispach.sacar_cpu()
		self.tarea.put_cpu()

	def pageFault(self, pcb):
		self.pcb = pcb
                self.aux = PAGETABLE_ELEM(self.pcb.get_pid(), self.pcb.get_pc()/4, None, None, True, 1, time.time())
		if self.pagetable.existe_pageID(self.aux):
			self.id = None
			self.bloque_de_memoria = MEMBLOCK(self.pcb.get_pid(), False , None, len(self.pcb.get_inst()))
			self.bloque.add_block_list(self.bloque_de_memoria)
			if self.memory.search_memoria_fisica_disponible():
				validar = True
                		aux = self.memory.firstMem
                		while (validar):
               				var=aux.getValor()
					#print ("Estado de Memoria fisica:", var.get_state())
					if var.get_state():
						self.id = var.get_n_frame()
						var.set_state(False) 
                                		validar = False
                        		else:
                                		aux = aux.next
                		self.elemento_tabla = PAGETABLE_ELEM(self.pcb.get_pid(), self.pcb.get_pc()/4, self.id, None, True, 1, time.time())
                		self.pagetable.put(self.elemento_tabla)
			else:
				if get_metodo_paginacion() == 0:
					self.pagefault_fifo(pcb) 		
				if get_metodo_paginacion() == 1:
					self.pagefault_second_change(pcb) 		
				if get_metodo_paginacion() == 2:
					self.pagefault_LRU(pcb) 		

	def pagefault_LRU(self, pcb):
		self.pcb = pcb
		if len(self.pcb.get_inst())<=4:
			if self.swap.search_swap_disponible():
				validar_aux = True
                           	aux_swap = self.swap.firstSwap
                                while (validar_aux):
                                    	var_swap=aux_swap.getValor()
                                        if var_swap.get_state():
                                             	self.id_swap = var_swap.get_n_frame()
                                                var_swap.set_state(False)
                                                validar_aux = False
                                        else:
                                              	aux_swap = aux_swap.next
				reemplazo = self.pagetable.get_replace_element_LRU()
				print ("Imprimo reemplazo: ", reemplazo)
				memoria_fisica = self.pagetable.set_page_element(reemplazo, self.id_swap, False)
				self.memory.memoria_fisica_cambiar_estado(memoria_fisica)
				self.aux_pagefault(pcb)


	def pagefault_second_change(self, pcb):
		self.pcb = pcb
		if len(self.pcb.get_inst())<=4:
			if self.swap.search_swap_disponible():
				validar_aux = True
                           	aux_swap = self.swap.firstSwap
                                while (validar_aux):
                                    	var_swap=aux_swap.getValor()
                                        if var_swap.get_state():
                                             	self.id_swap = var_swap.get_n_frame()
                                                var_swap.set_state(False)
                                                validar_aux = False
                                        else:
                                              	aux_swap = aux_swap.next
				reemplazo = self.pagetable.get_replace_element()
				print ("Imprimo reemplazo: ", reemplazo)
				memoria_fisica = self.pagetable.set_page_element(reemplazo, self.id_swap, False)
				self.memory.memoria_fisica_cambiar_estado(memoria_fisica)
				self.aux_pagefault(pcb)
		

	def pagefault_fifo(self, pcb):
		self.pcb = pcb
		if len(self.pcb.get_inst())<=4:
			if self.swap.search_swap_disponible():
				lista_fifo = self.pagetable.get_fifo()
				validar_aux = True
                           	aux_swap = self.swap.firstSwap
                                while (validar_aux):
                                    	var_swap=aux_swap.getValor()
                                        if var_swap.get_state():
                                             	self.id_swap = var_swap.get_n_frame()
                                                var_swap.set_state(False)
                                                validar_aux = False
                                        else:
                                              	aux_swap = aux_swap.next
				memoria_fisica = self.pagetable.set_page_element(lista_fifo[0], self.id_swap, False)
				lista_fifo.remove(lista_fifo[0])
				self.memory.memoria_fisica_cambiar_estado(memoria_fisica)
				self.aux_pagefault(pcb)

	def aux_pagefault(self, pcb):
		self.pcb = pcb
                self.aux = PAGETABLE_ELEM(self.pcb.get_pid(), self.pcb.get_pc()/4, None, None, True, 1, time.time())
		if self.pagetable.existe_pageID(self.aux):
			self.id = None
			self.bloque_de_memoria = MEMBLOCK(self.pcb.get_pid(), False , None, len(self.pcb.get_inst()))
			self.bloque.add_block_list(self.bloque_de_memoria)
			if self.memory.search_memoria_fisica_disponible():
				validar = True
                		aux = self.memory.firstMem
                		while (validar):
               				var=aux.getValor()
					#print ("Estado de Memoria fisica:", var.get_state())
					if var.get_state():
						self.id = var.get_n_frame()
						var.set_state(False) 
                                		validar = False
                        		else:
                                		aux = aux.next
                		self.elemento_tabla = PAGETABLE_ELEM(self.pcb.get_pid(), self.pcb.get_pc()/4, self.id, None, True, 1, time.time())
                		self.pagetable.put(self.elemento_tabla)

