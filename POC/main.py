from programas import *
from disco import *
from pcb_table import *
from sistemasoperativos import *
from queue import *

programa = program()
programa.set_name_program("fifa.exe")
programa.add_Instruction("CPU")
programa.add_Instruction("CPU")
programa.add_Instruction("IO")

disk = disk()
disk.save(programa.get_name(), programa.get_list())

pcbtable = pctable()
memory = memory ()

irqmanager = irqmanager()
irqmanager.set_PcbTable(pcbtable)
irqmanager.set_Memory(memory)

irqmanager.register(kill, killroutine())

cpu = cpu(memory, irqmanager)
clock = clock()
clock.Add(cpu)

loader = loader(memory, disk)



dispatcher = dispatcher(cpu, pcbTable)

schedule = schechuleFCFS()
kernel = kernel(dispacher, irqmanager, loader, schedule)

kernel.starup()
kernel.execute("fifa.exe")

clock.ticks()
clock.ticks()

kernel.execute("prueba.exe")
kernel.execute("prueba1.exe")
kernel.execute("prueba2.exe")
kernel.execute("prueba3.exe")
kernel.shutdown()
