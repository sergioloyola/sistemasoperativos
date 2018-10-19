import time
from pcb_table import *
from sistemasoperativo import *
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

	def cargar_cpu(self):
		if not cpu_state():
#			print self.tarea.get_next()
			tarea_cpu = self.tarea.get_next()
			tarea_cpu.set_state("Running")		
#			self.procesador.put_cpu(self.tarea.get_next())
			self.procesador.put_cpu(tarea_cpu)
			#print self.tarea.get_next()
			#llamo al schedule le pido el proximo proceso y lo pongo en cpu
#	def take_cpu(): 
