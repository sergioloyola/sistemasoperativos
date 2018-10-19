from programas import *
from disco import *
from pcb_table import *
from kernell import *
from queue import *

programa = program()
programa.set_name_program("mysqld")
programa.add_Instruction("CPU")
programa.add_Instruction("CPU")
programa.add_Instruction("IO")

disk = disk()
disk.save(programa.get_name(), programa.get_list())

pcbtable = pcb_table()
memory = Memory()
irqmanager = irqmanager()
irqmanager.set_PcbTable(pcbtable)
irqmanager.set_Memory(memory)

#irqmanager.register(kill, killroutine())

cpu = cpu(memory, irqmanager)
clock = clock()
clock.Add(cpu)

loader = loader(memory, disk)



dispatcher = dispatcher(cpu, pcbTable)

schedule = schechuleFCFS()
kernel = kernel(dispacher, irqmanager, loader, schedule)

kernel.starup()
kernel.execute("mysqld")

clock.ticks()
clock.ticks()

kernel.execute("prueba.exe")
kernel.execute("prueba1.exe")
kernel.execute("prueba2.exe")
kernel.execute("prueba3.exe")
kernel.shutdown()
