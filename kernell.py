#########################################################################################################################
#Autor: Sergio Loyola
#Correo: sergio.loyola@unq.edu.ar
#Fecha: 28/06/2016
#Descripcion: En este elemeto se almacenan todas las variables necesarias para la implementacion del sistema operativo.
#########################################################################################################################

pid_inicial = 10
id_inicial = 10
mem_inicial = 1000
cpu_idle = False
inicio = False
priority_queue = False
inicio_memoria = False
process_state = False
type_memory = None
tipo_metodo_paginacion = 0 # Si es 0 = FIFO, 1 = Second change, 2 = LRU
type_schedule = None # 0 es FCFS, 1 Priority, 2 Round Robin

def inc_pid():
    global pid_inicial
    pid = pid_inicial
    pid = pid + 1
    pid_inicial = pid
    return pid

def inc_id():
    global id_inicial
    id = id_inicial
    id = id + 1
    id_inicial = id
    return id

def inc_mem(val):
    global mem_inicial
    mem = mem_inicial
    mem_inicial = mem + val
    return mem

def cpu_state():
    global cpu_idle
    cpuIdle = cpu_idle
    return cpuIdle

def set_cpu_state(state):
    global cpu_idle
    cpu_idle = state	

def prog_inicio():
    global inicio
    progInicio = inicio
    return progInicio

def set_prog_inicio(state):
    global inicio
    inicio = state	

def cola_prioridad():
    global priority_queue
    Prioqueue = priority_queue
    return Prioqueue

def set_cola_prioridad(state):
    global priority_queue
    priority_queue = state	

def inicio_de_memoria():
    global incio_memoria
    ini_mem = inicio_memoria
    return ini_mem
def set_inicio_de_memoria(memoria):
    global inicio_memoria
    inicio_memoria = memoria	

def get_type_memory():
    global type_memory
    type_mem = type_memory
    return type_mem

def set_type_memory(memoria):
    global type_memory
    type_memory = memoria	

def get_metodo_paginacion():
    global tipo_metodo_paginacion
    tipo_metodo = tipo_metodo_paginacion
    return tipo_metodo

def set_metodo_paginacion(metodo):
    global tipo_metodo_paginacion
    tipo_metodo_paginacion = metodo	

def get_type_schedule():
    global type_schedule
    type_sche = type_schedule
    return type_sche

def set_type_schedule(schedule):
    global type_schedule
    type_schedule = schedule	

def get_state_process():
    global process_state
    state_process = process_state
    return state_process

def set_state_process(state):
    global process_state
    process_state = state	
