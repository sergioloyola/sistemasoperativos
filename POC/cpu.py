from queue import *

class CPU:

	def put_cpu(self, pcb):
		self.pcb_cpu = pcb
#		print self.pcb_cpu
	def get_cpu(self):
		print self.pcb_cpu
