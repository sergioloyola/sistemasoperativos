#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: En este elemento se trato de emular el trabajo realizar por el dispacher en un sistema operativos
#########################################################################################################################

import time
from pcb_table import *
from kernell import *
from programas import *
from disco import *
from queue import *
from mem import *
from cpu import *

class Dispacher:
	
	def set_schedule(self, schedule):
	        self.tarea = schedule

	def set_cpu(self, cpu):
	        self.procesador = cpu

	def set_queue_ready(self, cola):
	        self.queue_ready = cola

	def set_queue_waiting(self, cola):
	        self.queue_waiting = cola

	def cargar_cpu(self, pcb):
			pcb_cpu = pcb
			pcb_cpu.set_state("Running")		
			self.procesador.put_cpu(pcb_cpu)

#			self.queue_ready.eliminarPrimero()
			#llamo al schedule le pido el proximo proceso y lo pongo en cpu
	def take_cpu(self): 
			self.pcb_cpu = self.procesador.get_cpu()
#			print self.procesador.get_cpu()
			if self.procesador.get_cpu() != None:
				self.pcb_cpu.set_state("Ready")
				set_cpu_state(False)
#				self.pcb_cpu = self.procesador.del_cpu()
				return self.pcb_cpu
			else:
				return None		

	def sacar_cpu(self):
			self.cpu_vacio = self.procesador.del_cpu()
			return self.cpu_vacio
