#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Simulacion del reloj del sistema operativo.
#########################################################################################################################

from kernell import *
from irqmanager import *
from pcb_table import *

burst_count = 0

class clock:
	def set_cpu(self, cpu):
		self.cpu = cpu

	def set_mem(self, mem):
		self.mem = mem

	def set_irq(self, irq):
		self.proceso = irq

	def set_blockmem(self, memblock):
		self.mem_block = memblock

        def set_schedule(self, tarea):
                self.tarea = tarea

        def set_PcbTable(self, pcbTable):
                self.pcbtable = pcbTable

        def set_dispach(self, puntero):
                self.dispach = puntero

        def set_queue_ready(self, cola):
                self.queue_ready = cola
	
	def ticks(self):
		global burst_count
		if get_type_schedule() == 2:
			burst_count = burst_count + 1
			if burst_count < 2:
				self.ticks_aux()
			else:
				#Voy a hacer content switch
#				print ("Estado del proceso:", get_state_process())
				self.ticks_aux()
               			self.pcb = self.dispach.take_cpu()
				if get_state_process() == False: 
               				self.pcb.set_state("Ready")
					self.queue_ready.agregarFinal(self.pcb)
          				#self.pcbtable.eliminar_key(self.pcb.get_pid())
               				self.pcbtable.put(self.pcb.get_pid(), self.pcb)
               				self.dispach.sacar_cpu()
               				self.tarea.put_cpu()
					burst_count = 0
               				#set_cpu_state(False)
				else:
					set_state_process(False)
#					print "Cambio el estado a False"
							
		else:
			self.ticks_aux()

	def ticks_aux(self):
		if get_type_memory() == 0:
			self.pcb = self.cpu.get_cpu()
			if self.pcb == None:
				set_cpu_state(False)
			if cpu_state():
#				print self.pcb
				self.inst = self.pcb.get_inst()
				self.inst_aux = self.pcb.get_inst()
				self.reg = self.mem_block.search_for_pid(self.pcb.get_pid()) + self.pcb.get_pc()
				if self.inst[0 + self.pcb.get_pc()] != "end":
					if self.inst[0 + self.pcb.get_pc()] != "io":
						self.pcb.set_pc(self.pcb.get_pc() + 1)

					else:
						self.pcb.set_pc(self.pcb.get_pc() + 1)
						self.proceso.io()				
				else:	
					self.mem_block.liberar_bloque(self.pcb.get_pid())
					self.pcb.set_pc(self.pcb.get_pc() + 1)
					self.pcb.set_inst(self.inst)
					self.cpu.put_cpu(self.pcb)
#					print ("El siguiente proceso termino:", self.pcb.get_pid())
					self.proceso.kill()
					if get_type_schedule() == 2:
						set_state_process(True)
			else:
				print "No hay procesos disponibles"
		else: #paginacion
			if cpu_state():
				self.pcb = self.cpu.get_cpu()
				self.inst = self.pcb.get_inst()
				self.inst_aux = self.pcb.get_inst()
				if self.inst[0 + self.pcb.get_pc()] != "end":
					if self.inst[0 + self.pcb.get_pc()] != "io":
						self.pcb.set_pc(self.pcb.get_pc() + 1)
					else:
						self.pcb.set_pc(self.pcb.get_pc() + 1)
						self.proceso.io()				
					self.proceso.pageFault(self.cpu.get_cpu())
				else:	
					self.pcb.set_pc(self.pcb.get_pc() + 1)
					self.pcb.set_inst(self.inst)
					self.cpu.put_cpu(self.pcb)
					self.proceso.kill()
					self.pcbtable.put(inc_id(), self.cpu.get_cpu())
	
			else:
				self.tarea.put_cpu()
				self.pcbtable.put(inc_id(), self.cpu.get_cpu())
				self.proceso.pageFault(self.cpu.get_cpu())


	def ticks_bkp(self):
		global burst_count
		if not self.queue_ready.esVacio():
			if get_type_schedule() == 2:
				burst_count = burst_count + 1
				if burst_count < 2:
					self.ticks_aux()
				else:
					#Voy a hacer content switch
					print ("Estado del proceso:", get_state_process())
					self.ticks_aux()
                			self.pcb = self.dispach.take_cpu()
					if get_state_process() == False: 
	                			self.pcb.set_state("Ready")
						self.queue_ready.agregarFinal(self.pcb)
                				#self.pcbtable.eliminar_key(self.pcb.get_pid())
                				self.pcbtable.put(self.pcb.get_pid(), self.pcb)
                				self.dispach.sacar_cpu()
                				self.tarea.put_cpu()
						burst_count = 0
                				#set_cpu_state(False)
					else:
						set_state_process(False)
						print "Cambio el estado a False"
								
			else:
				self.ticks_aux()
		else:
			print "No hay mas procesos por Procesar"
