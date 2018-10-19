#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: Toma todos los modulos para la simulacion del sistema operativo
#########################################################################################################################


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
from page_table import *

programa = program()
proceso = InterruptionManager()
cola_ready = queue()
cola_waiting = queue()
cola_ready = queue()
cola_waiting = queue()
pcbtable = pcb_table()
pagetable = page_table() #Ver como deshabilitar con asignacion continua
memoria_fisica = Memory()
swap = Swap()
#memory = Memory()
disco = disk()
procesador = CPU()
puntero = Dispacher()
reloj = clock()

#Variables booleanas para seleccion de opciones
option_schedule = True
option_type_memory = True
option_ajuste = True
option_victima = True

print "Seleccione el tipo de Schedule a utilizar\n"
print "0 - FCFS"
print "1 - Priority No Expropiativo" 
print "2 - Round Robin"
print "3 - Priority Expropiativo"
while option_schedule:
        schedule=input("Introduce tipo de Schedule: ")

        if schedule == 0:
		tarea = ScheduleFCFS()
                print "FCFS seleccionado \n"
                option_schedule = False
        if schedule == 1:
		tarea = SchedulePriority()
                print "Priority No ExpropiativoSeleccionado \n"
                option_schedule = False
        if schedule == 2:
		tarea = ScheduleRound_Robin()
		set_type_schedule(2)
                print "Round Robin Seleccionado \n"
                option_schedule = False

        if schedule == 3:
		tarea = SchedulePriority_Expropiativo()
                print "Priority Expropiativo Seleccionado \n"
                option_schedule = False

        if option_schedule:
                print "opcion incorrecta, Vuelva a intentar \n"

print "Seleccione el tipo de Memoria a utilizar\n"
print "0 - Asignacion Continua"
print "1 - Paginacion" 

while option_type_memory:
        tipo_memoria=input("Ingrese el tipo de memoria tipo de Schedule: ")

        if tipo_memoria == 0:
		#Memoria Continua
		set_type_memory(0)
                print "Selecciono asignacion continua \n"
                option_type_memory = False
        if tipo_memoria == 1:
		#Memoria Continua
		set_type_memory(1)
		print "Selecciono Paginacion \n"
                swap.frame_swap()
		memoria_fisica.frame_memory()
		option_type_memory = False

        if option_type_memory:
                print "opcion incorrecta, Vuelva a intentar \n"

if tipo_memoria == 0:
	print "Seleccione el tipo de Ajuste\n"
	print "0 - First-fit"
	print "1 - worst-fit" 
	print "2 - Best-fit" 
	
	while option_ajuste:
        	tipo_ajuste=input("Ingrese el tipo de Ajuste: ")

        	if tipo_ajuste == 0:
			bloque_memoria = First_Fit()
	                print "Selecciono First-fit \n"
	                option_ajuste = False
        	if tipo_ajuste == 1:
			bloque_memoria = Worst_Fit()
	                print "Selecciono Worst-fit \n"
	                option_ajuste = False
        	if tipo_ajuste == 2:
			bloque_memoria = Best_Fit()
	                print "Selecciono Best-fit \n"
	                option_ajuste = False
	        if option_ajuste:
        	        print "opcion incorrecta, Vuelva a intentar \n"

if tipo_memoria == 1:
	print "Seleccione el algorit de seleccion de victima \n"
	print "0 - FIFO"
	print "1 - Second Chance" 
	print "2 - LRU" 
	while option_victima:
        	tipo_victima=input("Ingrese el tipo de seleccion de victima: ")
        	if tipo_victima == 0:
			set_metodo_paginacion(0)
			bloque_memoria = Paginacion()
	                print "Selecciono FIFO \n"
	                option_victima = False
        	if tipo_victima == 1:
			set_metodo_paginacion(1)
			bloque_memoria = Paginacion()
	                print "Selecciono Second Chance \n"
	                option_victima = False
        	if tipo_victima == 2:
			set_metodo_paginacion(2)
			bloque_memoria = Paginacion()
	                print "Selecciono LRU \n"
	                option_victima = False
	        if option_victima:
        	        print "opcion incorrecta, Vuelva a intentar \n"

#Creo las flechas para memoria
memoria_fisica.set_cpu(procesador)
memoria_fisica.set_page_table(pagetable)

#Creo las flechas para proceso
proceso.set_PcbTable(pcbtable)
proceso.set_Memory(memoria_fisica)
proceso.set_queue_ready(cola_ready)
proceso.set_queue_waiting(cola_waiting)
proceso.set_schedule(tarea)
proceso.set_dispach(puntero)
proceso.set_memory_block(bloque_memoria)
proceso.set_page_table(pagetable)
proceso.set_swap(swap)

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
reloj.set_mem(memoria_fisica)
reloj.set_blockmem(bloque_memoria)
reloj.set_dispach(puntero)
reloj.set_PcbTable(pcbtable)
reloj.set_schedule(tarea)
reloj.set_queue_ready(cola_ready)
 
#Creo el Programa
programa.set_name_program("apache2")
programa.add_Instruction("CPU")
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

if tipo_memoria == 0:
	bloque_memoria.crear_block_list()
	proceso.new(disco.get_disk("postgresql"))
	proceso.new(disco.get_disk("apache2"))
	proceso.new(disco.get_disk("mysqld"))

	if schedule == 1 or schedule == 3: #Si elijo prioridad
		tarea.set_queue_ready(cola_ready)
	print "------------------------------------Arranque---------------------------"
	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"
	reloj.ticks()
	reloj.ticks()
	print "CPU => %s" % procesador.get_cpu()

	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"

	#
	reloj.ticks()
	reloj.ticks()
	print "CPU => %s" % procesador.get_cpu()

	if schedule == 3: #Simulo una expropiacion
		print "Simulo expropiacion"
		proceso.timeout()
	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"

	#

	reloj.ticks()
	reloj.ticks()
	print "CPU => %s" % procesador.get_cpu()

	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"

	#

	reloj.ticks()
	reloj.ticks()
	print "CPU => %s" % procesador.get_cpu()

	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"

	#

	reloj.ticks()
	reloj.ticks()
	print "CPU => %s" % procesador.get_cpu()

	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"

	#

	reloj.ticks()
	#reloj.ticks()
	#print "CPU => %s" % procesador.get_cpu()

	print "PCb Table"
	pcbtable.get_all()
	print "-----------------------------------------------------------------------"
if tipo_memoria == 1:
	bloque_memoria.crear_block_list()
	print "Ejecuto APACHE2"
	proceso.new(disco.get_disk("mysqld"))
	print "Ejecuto MYSQLD"
	proceso.new(disco.get_disk("apache2"))
	print "Ejecuto postgresql"
	proceso.new(disco.get_disk("postgresql"))
	print "Ejecuto MYSQLD"
	proceso.new(disco.get_disk("mysqld"))
	print "Ejecuto postgresql"
	proceso.new(disco.get_disk("postgresql"))
	bloque_memoria.lista_ordenada()
	if schedule == 1 or schedule == 3: #Si elijo prioridad
		tarea.set_queue_ready(cola_ready)

	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"

	print "---------------------------Segundo Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "---------------------------Tercer Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "---------------------------Cuarto Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "---------------------------Quinto Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "---------------------------Sexto Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------Septimo Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------Octavo Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------Noveno Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------Decimo Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------Once Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------DOCE Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------TRECE Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()

	print "---------------------------CATORCE Tick----------------------------"
	reloj.ticks()
	print "-------------------------PCB TABLE---------------------"
	pcbtable.get_all()
	print "-------------------------------------------------------"
	print "Paginas"
	bloque_memoria.lista_ordenada()
	print"--------------------------PAGE TABLE--------------------"
	pagetable.get_all()
	print"--------------------------------------------------------"
	print "-------------------------CPU---------------------------"
	print "CPU => %s" % procesador.get_cpu()
	print"--------------------------------------------------------"
	print "-------------------------------------------------------------------"

	print "Memoria Fisica"
	memoria_fisica.lista_ordenada()
	print "Memoria Swap"
	swap.swap_ordenada()
	if tipo_victima == 1:
		print "second Change"
		pagetable.imprimir_second_chance()
	if tipo_victima == 2:
		print "LRU"
		pagetable.imprimir_LRU()

