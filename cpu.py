#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Simulacion de la cpu y como entran y salen los procesos que maneja
#########################################################################################################################

from queue import *
from kernell import *

class CPU:

	def del_cpu(self):
		self.pcb_cpu = None
		return self.pcb_cpu
	def put_cpu(self, pcb):
		self.pcb_cpu = pcb
		set_cpu_state(True)
	def get_cpu(self):
		return self.pcb_cpu
