import time
from pcb_table import *
from sistemasoperativo import *
from programas import *
from disco import *
from queue import *
from mem import *


class InterruptionManager:

	def set_PcbTable(self, pcbTable):
		self.pcbtable = pcbTable

	def set_Memory(self, memory):
		self.memory = memory

#	def timeout(self):
	def new(self, inst):
		self.inst = inst
		self.var_mem = PCB(inc_pid(), "New",  time.strftime("%d%m%y"), 9, 15, 0, inc_mem(len(self.inst)), self.inst)
		self.pcbtable.put(inc_id(), self.var_mem)
		self.memory.memory_table(self.var_mem.get_basedir(), self.var_mem.get_inst())
#	def io(self):
#	def io_end(self):
#	def kill(self):



