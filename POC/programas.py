class program:

	def __init__(self, name=None):
		self.name = name
		self.inst =[]
        def set_name_program(self, name ):
		self.name = name
		self.inst = []
	def add_Instruction(self, inst):
		self.inst.append(inst)
	def get_Instruction(self):
		for x in self.inst:
	     		print x
	def get_name(self):
		return self.name

	def get_list(self):
		return self.inst
