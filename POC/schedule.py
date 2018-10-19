from queue import *

class ScheduleFCFS:

	def __init__(self):
		self.queue = queue()

	def put(self, pcb):
		self.queue.put_ready(pcb)

	def get_next(self):
		aux = self.queue.get_next()
		if aux != None:
			aux.set_state("terminado")
			return aux

class SchedulePriority:
	def __init__(self):
		self.queue1 = queue()
		self.queue2 = queue()
		self.queue3 = queue()
		self.queue4 = queue()
		self.queue5 = queue()

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

class ScheduleRound_robin:

	def __init__(self):
		self.queue = queue()

	def put(self, pcb):
		self.queue.put_ready(pcb)

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
