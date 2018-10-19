pid_inicial = 10
id_inicial = 10
mem_inicial = 1000
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
    mem = mem + 1
    mem_inicial = mem + val - 1
    return mem

