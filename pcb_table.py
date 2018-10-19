#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Simulacion de la tabla PCB
#########################################################################################################################

class pcb_table:

        def __init__(self):
                self.pcb_table = {}
	
        def put(self, pid,  pcb):
                #self.pcb_table.setdefault(new, pcb)
                self.pid = pid
                self.pcb = pcb
                self.pcb_table.setdefault(self.pid, self.pcb)
        def get_all(self):
#		print self.pcb_table
                for id in self.pcb_table:
                        print self.pcb_table[id]
#                        return self.pcb_table[id]
	def get_value(self, id):
    		return self.pcb_table[id]

	def get_list_key(self):
		return self.pcb_table.keys()

	def eliminar_key(self, id):
		self.pcb_table.pop(id, None)

        def existe_pid(self, valor):
                self.resul = True
                for id in self.pcb_table:
                        self.elemento_tabla = self.pcb_table[id]
                        if self.elemento_tabla.get_pid() == valor.get_pid():
                                self.resul = False
                                return self.resul
                return self.resul

