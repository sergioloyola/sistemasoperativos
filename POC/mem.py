from irqmanager import *

reg_mem= {}
class Memory:
	def memory_table(self, address, inst):
       		global reg_mem
        	self.address = address - 1
		self.inst = inst
		print self.inst
		for x in self.inst:
			self.address = self.address +1
	        	reg_mem.setdefault(self.address, x)

	def get_memory_table(self):
        	for id in reg_mem:
	        	print id, ":" , reg_mem[id]
