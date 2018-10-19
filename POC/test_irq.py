from irqmanager import *
from sistemasoperativo import *
from programas import *
from disco import *
from pcb_table import *
from mem import *

programa = program()
disco = disk()
proceso = InterruptionManager()
pcbtable = pcb_table()
memory = Memory()
 

proceso.set_PcbTable(pcbtable)
proceso.set_Memory(memory)

programa.set_name_program("fifa")
programa.add_Instruction("CPU")
programa.add_Instruction("CPU")
programa.add_Instruction("IO")
disco.save(programa.get_name(), programa.get_list())

programa.set_name_program("prog")
programa.add_Instruction("CPU")
programa.add_Instruction("IO")
disco.save("prog2", programa.get_list())


proceso.new(disco.get_disk("fifa"))
proceso.new(disco.get_disk("prog2"))
#memory.get_memory_table()

