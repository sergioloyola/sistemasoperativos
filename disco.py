#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Simulacion muy minimalista de un disco en el cual se utiliza un diccionario para almacenar los programas y
#             sus instrucciones.
#########################################################################################################################


class disk:

 	def __init__(self):
		self.programs = {}
	
        def save(self, name, instructions ):
		self.programs[name]= instructions

	def get_disk(self, name):
		return self.programs[name]
