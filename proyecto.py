from irqmanager import *
from kernell import *
from programas import *
from disco import *
from pcb_table import *
from mem import *
from schedule import *
from dispacher import *
from cpu import *
from queue import *
from clock import *

#Memoria Continua
set_type_memory(0)
#Creo instacias de las clases.
programa = program()
proceso = InterruptionManager() 
cola_ready = queue()
cola_waiting = queue()
#tarea = ScheduleFCFS()
tarea = SchedulePriority()
#tarea = ScheduleRound_Robin()
bloque_memoria = First_Fit()
#bloque_memoria = Best_Fit()
#bloque_memoria = Worst_Fit()
  
#tarea = SchedulePriority() 
pcbtable = pcb_table() 
memory = Memory()
disco = disk()
procesador = CPU()
puntero = Dispacher()
reloj = clock()

#Creo las flechas para proceso
proceso.set_PcbTable(pcbtable)
proceso.set_Memory(memory)
proceso.set_queue_ready(cola_ready)
proceso.set_queue_waiting(cola_waiting)
proceso.set_schedule(tarea)
proceso.set_dispach(puntero)
proceso.set_memory_block(bloque_memoria)

#Creo las flechas para tarea
tarea.set_dispacher(puntero)
tarea.set_cpu(procesador)
tarea.set_queue_ready(cola_ready)
tarea.set_queue_waiting(cola_waiting)

#Creo las flechas para puntero
puntero.set_cpu(procesador)
puntero.set_queue_ready(cola_ready)
puntero.set_queue_waiting(cola_waiting)
puntero.set_schedule(tarea)

#Creo flecha para reloj
reloj.set_cpu(procesador)
reloj.set_irq(proceso)
reloj.set_mem(memory)
reloj.set_blockmem(bloque_memoria)
 
#Creo el Programa
programa.set_name_program("apache2")
programa.add_Instruction("CPU")
programa.add_Instruction("CPU")
programa.add_Instruction("CPU")
programa.add_Instruction("end")
#Lo guardo en Disco
disco.save(programa.get_name(), programa.get_list())

#Creo el Programa
programa.set_name_program("mysqld")
programa.add_Instruction("CPU")
programa.add_Instruction("end")
#Lo guardo en Disco
disco.save("mysqld", programa.get_list())

programa.set_name_program("postgresql")
programa.add_Instruction("CPU")
programa.add_Instruction("CPU")
programa.add_Instruction("end")
#Lo guardo en Disco
disco.save(programa.get_name(), programa.get_list())

#Ejecuto los programas
bloque_memoria.crear_block_list()
#bloque_memoria.imprimirListaDeBloques()
proceso.new(disco.get_disk("postgresql"))
proceso.new(disco.get_disk("apache2"))
proceso.new(disco.get_disk("mysqld"))
#proceso.new(disco.get_disk("apache2"))
#proceso.new(disco.get_disk("mysqld"))
#bloque_memoria.imprimirListaDeBloques()
#bloque_memoria.lista_ordenada()
bloque_memoria.lista_ordenada()

#print "Memoria"
#memory.get_memory_table()
#print "Memoria libre"
#memory.get_memory_libre()
'''print "Cola"
cola_ready.imprimirListaPrimeroUltimo()
print "PCb Table"
pcbtable.get_all()
print "Memoria"
memory.get_memory_table()
print "CPU => %s" % procesador.get_cpu()
'''
reloj.ticks()
reloj.ticks()
reloj.ticks()

'''print "Despues del timeOUT"
proceso.timeout()
print "Cola"
cola_ready.imprimirListaPrimeroUltimo()
print "PCb Table"
pcbtable.get_all()
print "Memoria"
memory.get_memory_table()
print "CPU => %s" % procesador.get_cpu()

print "---------------------------------------------------"
print "Hago un ticks"
reloj.ticks()
print "Cola Ready"
cola_ready.imprimirListaPrimeroUltimo()
print "PCb Table"
pcbtable.get_all()
print "Memoria"
memory.get_memory_table()
print "CPU => %s" % procesador.get_cpu()

print "---------------------------------------------------"
print "Hago un ticks"
reloj.ticks()
print "Cola Ready"
cola_ready.imprimirListaPrimeroUltimo()
print "PCb Table"
pcbtable.get_all()
print "Memoria"
memory.get_memory_table()
print "CPU => %s" % procesador.get_cpu()

print "---------------------------------------------------"
print "Hago un ticks end"
reloj.ticks()
print "Cola Ready"
cola_ready.imprimirListaPrimeroUltimo()
print "PCb Table"
pcbtable.get_all()
print "Memoria"
memory.get_memory_table()
#memory.crear_tabla_libre()
print "CPU => %s" % procesador.get_cpu()
#memory.get_memory_libre()
#print disco.get_disk("postgresql")
#print disco.get_disk("apache2")
#print disco.get_disk("mysqld")
proceso.new(disco.get_disk("postgresql"))
print "Memoria RAM2"
#memory.get_memory_table()
bloque_memoria.lista_ordenada()

print "-----------PCB TABLE------------------"
pcbtable.get_all()
print "--------------------------------------"

reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
bloque_memoria.lista_ordenada()
print "Ejecuto MYSQLD"
proceso.new(disco.get_disk("mysqld"))
bloque_memoria.lista_ordenada()

reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
reloj.ticks()
print "-----------PCB TABLE------------------"
pcbtable.get_all()
print "--------------------------------------"

print "-----------BLOQUE DE MEORIA-----------"
bloque_memoria.lista_ordenada()
print "--------------------------------------"
'''
#print "Ejecuto MYSQLD"
#proceso.new(disco.get_disk("mysqld"))

print "-----------BLOQUE DE MEORIA-----------"
bloque_memoria.lista_ordenada()
print "--------------------------------------"



'''print "CPU => %s" % procesador.get_cpu()
reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
reloj.ticks()
print "CPU => %s" % procesador.get_cpu()
bloque_memoria.lista_ordenada()
print "Ejecuto MYsql"
proceso.new(disco.get_disk("mysqld"))
bloque_memoria.lista_ordenada()
'''
print "Compacto Memoria RAM"
bloque_memoria.compactar()

#print "Ejecuto MYSQLD"
#proceso.new(disco.get_disk("mysqld"))
print "----------------BLOCK LIST ----------------------"
bloque_memoria.lista_ordenada()
print "-------------------------------------------"

#reloj.ticks()
print "-----------PCB TABLE------------------"
pcbtable.get_all()
print "--------------------------------------"
reloj.ticks()
print "-----------PCB TABLE------------------"
pcbtable.get_all()
print "--------------------------------------"
print "----------------BLOCK LIST ----------------------"
bloque_memoria.lista_ordenada()
print "-------------------------------------------"

print "Compacto Memoria RAM"
bloque_memoria.compactar()

print "----------------BLOCK LIST ----------------------"
bloque_memoria.lista_ordenada()
print "-------------------------------------------"

'''reloj.ticks()
print "-----------PCB TABLE------------------"
pcbtable.get_all()
print "--------------------------------------"
'''
