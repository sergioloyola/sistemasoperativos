class disk:

 	def __init__(self):
		self.programs = {}
	
        def save(self, name, instructions ):
		self.programs[name]= instructions

	def get_disk(self, name):
		return self.programs[name]
