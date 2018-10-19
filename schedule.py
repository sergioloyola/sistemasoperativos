from queue import *
from kernell import *
from dispacher import *

class ScheduleFCFS:

        def set_dispacher(self, puntero):
                self.dispach = puntero

        def set_cpu(self, cpu):
                self.procesador = cpu

        def set_queue_ready(self, cola):
                self.queue_ready = cola

        def set_queue_waiting(self, cola):
                self.queue_waiting = cola

	def put(self, pcb):
		self.queue_ready.put_ready(pcb)

	def get_next(self):
		aux = self.queue_ready.get_next()
		if aux != None:
			return aux
	def put_cpu(self):
                if not cpu_state():
			aux = self.queue_ready.get_pcb()
			if aux != None:
				self.dispach.cargar_cpu(aux)
			set_cpu_state(True)
			self.queue_ready.eliminarPrimero()

	def waiting_to_ready(self):
			aux = self.queue_waiting.get_pcb()
			if aux != None:
				aux.set_state("Ready")
				self.queue_ready.put_ready(aux)
			self.queue_waiting.eliminarPrimero()

class SchedulePriority:

        def set_dispacher(self, puntero):
                self.dispach = puntero

        def set_cpu(self, cpu):
                self.procesador = cpu

        def set_queue_ready(self, cola):
		if not cola_prioridad():
#			print "COLA PRIORIDAD"
                	self.queue1 = queue()
                	self.queue2 = queue()
                	self.queue3 = queue()
                	self.queue4 = queue()
                	self.queue5 = queue()
			set_cola_prioridad(True)
		self.cola = cola
		if not self.cola.esVacio():
#			print "sergio Loyola"
			set_prog_inicio(True)
                	validar = True
                	aux = self.cola.get_next()
            		while (validar):
	                	if aux != None:
#					print ("Imprimo prioridad:", aux.get_priority())
        	                	if aux.get_priority() == 1:
                	        		self.queue1.put_ready(aux)
                			if aux.get_priority() == 2:
                        			self.queue2.put_ready(aux)
    	            			if aux.get_priority() == 3:
                        			self.queue3.put_ready(aux)
                			if aux.get_priority() == 4:
                        			self.queue4.put_ready(aux)
                			if aux.get_priority() == 5:
                        			self.queue5.put_ready(aux)
                        		aux = self.cola.get_next()
				else:
                  			validar = False

#		print "COLA 1"		
#		self.queue1.imprimirListaPrimeroUltimo()
#		print "COLA 2"		
#		self.queue2.imprimirListaPrimeroUltimo()
#		print "COLA 3"		
#		self.queue3.imprimirListaPrimeroUltimo()
#		print "COLA 4"		
#		self.queue4.imprimirListaPrimeroUltimo()
#		print "COLA 5"		
#		self.queue5.imprimirListaPrimeroUltimo()
		
        def set_queue_waiting(self, cola):
                self.queue_waiting = cola


	def put(self, pcb):

		if pcb.priority == 1:
			self.queue1.put_ready(pcb)
		if pcb.priority == 2:
			self.queue2.put_ready(pcb)
		if pcb.priority == 3:
			self.queue3.put_ready(pcb)
		if pcb.priority == 4:
			self.queue4.put_ready(pcb)
		if pcb.priority == 5:
			self.queue5.put_ready(pcb)

	def get_next(self):
		aux1 = self.queue1.get_next()
		if aux1 != None:
			aux1.set_state("terminado")
			return aux1
		aux2 = self.queue2.get_next()
		if aux2 != None:
			aux2.set_state("terminado")
			return aux2
		aux3 = self.queue3.get_next()
		if aux3 != None:
			aux3.set_state("terminado")
			return aux3
		aux4 = self.queue4.get_next()
		if aux4 != None:
			aux4.set_state("terminado")
			return aux4
		aux5 = self.queue5.get_next()
		if aux5 != None:
			aux5.set_state("terminado")
			return aux5

	def put_cpu(self): # El orden de prioridad es mientras mas chico, mayor prioridad
		check_cola = True
#		print "PUT CPU SERGIO"
                if not cpu_state():
	#		print "CPU FALSE"
			if prog_inicio():
				if not self.queue1.esVacio() and check_cola:
					aux = self.queue1.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue1.eliminarPrimero()
					check_cola = False

				if not self.queue2.esVacio() and check_cola:
					aux = self.queue2.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue2.eliminarPrimero()
					check_cola = False

				if not self.queue3.esVacio() and check_cola:
					aux = self.queue3.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue3.eliminarPrimero()
					check_cola = False

				if not self.queue4.esVacio() and check_cola:
					aux = self.queue4.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue4.eliminarPrimero()
					check_cola = False

				if not self.queue5.esVacio() and check_cola:
					aux = self.queue5.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					check_cola = False
					self.queue5.eliminarPrimero()

			else:
	                        aux = self.cola.get_pcb()
        	                if aux != None:
                	                self.dispach.cargar_cpu(aux)
                       		set_cpu_state(True)
                        	self.cola.eliminarPrimero()

	def waiting_to_ready(self):
			aux = self.queue_waiting.get_pcb()
			if aux != None:
				aux.set_state("Ready")
				self.queue_ready.put_ready(aux)
			self.queue_waiting.eliminarPrimero()


class SchedulePriority_Expropiativo:

        def set_dispacher(self, puntero):
                self.dispach = puntero

        def set_cpu(self, cpu):
                self.procesador = cpu

        def set_queue_ready(self, cola):
		if not cola_prioridad():
                	self.queue1 = queue()
                	self.queue2 = queue()
                	self.queue3 = queue()
                	self.queue4 = queue()
                	self.queue5 = queue()
			set_cola_prioridad(True)
		self.cola = cola
		if not self.cola.esVacio():
			set_prog_inicio(True)
                	validar = True
                	aux = self.cola.get_next()
            		while (validar):
	                	if aux != None:
        	                	if aux.get_priority() == 1:
                	        		self.queue1.put_ready(aux)
                			if aux.get_priority() == 2:
                        			self.queue2.put_ready(aux)
    	            			if aux.get_priority() == 3:
                        			self.queue3.put_ready(aux)
                			if aux.get_priority() == 4:
                        			self.queue4.put_ready(aux)
                			if aux.get_priority() == 5:
                        			self.queue5.put_ready(aux)
                        		aux = self.cola.get_next()
				else:
                  			validar = False

#		print "COLA 1"		
#		self.queue1.imprimirListaPrimeroUltimo()
#		print "COLA 2"		
#		self.queue2.imprimirListaPrimeroUltimo()
#		print "COLA 3"		
#		self.queue3.imprimirListaPrimeroUltimo()
#		print "COLA 4"		
#		self.queue4.imprimirListaPrimeroUltimo()
#		print "COLA 5"		
#		self.queue5.imprimirListaPrimeroUltimo()
		
        def set_queue_waiting(self, cola):
                self.queue_waiting = cola


	def put(self, pcb):

		if pcb.priority == 1:
			self.queue1.put_ready(pcb)
		if pcb.priority == 2:
			self.queue2.put_ready(pcb)
		if pcb.priority == 3:
			self.queue3.put_ready(pcb)
		if pcb.priority == 4:
			self.queue4.put_ready(pcb)
		if pcb.priority == 5:
			self.queue5.put_ready(pcb)

	def get_next(self):
		aux1 = self.queue1.get_next()
		if aux1 != None:
			aux1.set_state("terminado")
			return aux1
		aux2 = self.queue2.get_next()
		if aux2 != None:
			aux2.set_state("terminado")
			return aux2
		aux3 = self.queue3.get_next()
		if aux3 != None:
			aux3.set_state("terminado")
			return aux3
		aux4 = self.queue4.get_next()
		if aux4 != None:
			aux4.set_state("terminado")
			return aux4
		aux5 = self.queue5.get_next()
		if aux5 != None:
			aux5.set_state("terminado")
			return aux5

	def put_cpu(self):
		check_cola = True
                if not cpu_state():
			if prog_inicio():
				if not self.queue1.esVacio() and check_cola:
					aux = self.queue1.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue1.eliminarPrimero()
					check_cola = False

				if not self.queue2.esVacio() and check_cola:
					aux = self.queue2.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue2.eliminarPrimero()
					check_cola = False

				if not self.queue3.esVacio() and check_cola:
					aux = self.queue3.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue3.eliminarPrimero()
					check_cola = False

				if not self.queue4.esVacio() and check_cola:
					aux = self.queue4.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					self.queue4.eliminarPrimero()
					check_cola = False

				if not self.queue5.esVacio() and check_cola:
					aux = self.queue5.get_pcb()
					if aux != None:
						self.dispach.cargar_cpu(aux)
					set_cpu_state(True)
					check_cola = False
					self.queue5.eliminarPrimero()

			else:
	                        aux = self.cola.get_pcb()
        	                if aux != None:
                	                self.dispach.cargar_cpu(aux)
                       		set_cpu_state(True)
                        	self.cola.eliminarPrimero()

	def waiting_to_ready(self):
			aux = self.queue_waiting.get_pcb()
			if aux != None:
				aux.set_state("Ready")
				self.queue_ready.put_ready(aux)
			self.queue_waiting.eliminarPrimero()


class ScheduleRound_Robin:

        def set_dispacher(self, puntero):
                self.dispach = puntero

        def set_cpu(self, cpu):
                self.procesador = cpu

        def set_queue_ready(self, cola):
                self.queue_ready = cola

        def set_queue_waiting(self, cola):
                self.queue_waiting = cola

	def put(self, pcb):
		self.queue_ready.put_ready(pcb)

	def get_next(self):
		aux = self.queue_ready.get_next()
		if aux != None:
			return aux
	def put_cpu(self):
                if not cpu_state():
			aux = self.queue_ready.get_pcb()
			if aux != None:
				self.dispach.cargar_cpu(aux)
			set_cpu_state(True)
			self.queue_ready.eliminarPrimero()

	def waiting_to_ready(self):
			aux = self.queue_waiting.get_pcb()
			if aux != None:
				aux.set_state("Ready")
				self.queue_ready.put_ready(aux)
			self.queue_waiting.eliminarPrimero()

class ScheduleRound_Robin_aux:

        def set_dispacher(self, puntero):
                self.dispach = puntero

        def set_cpu(self, cpu):
                self.procesador = cpu

        def set_queue_ready(self, cola):
                self.queue_ready = cola

        def set_queue_waiting(self, cola):
                self.queue_waiting = cola

	def put(self, pcb):
		self.queue_ready.put_ready(pcb)

	def get_next(self):
		aux = self.queue_ready.get_next()
		if aux != None:
			return aux
	def put_cpu(self):
                if not cpu_state():
			aux = self.queue_ready.get_pcb()
			if aux != None:
				self.dispach.cargar_cpu(aux)
			set_cpu_state(True)
			self.queue_ready.eliminarPrimero()

	def waiting_to_ready(self):
			aux = self.queue_waiting.get_pcb()
			if aux != None:
				aux.set_state("Ready")
				self.queue_ready.put_ready(aux)
			self.queue_waiting.eliminarPrimero()

	def get_next(self):
		validar = True
		aux = self.queue.get_next()
               	if aux.get_burst_time() >= 2:
			pepe = aux.get_burst_time() - 2
                       	aux.set_burst_time(pepe)
			if aux.get_burst_time() >= 2:
				self.queue.agregarFinal(aux)
			return(aux)
		else:
			self.queue.agregarFinal(aux)
