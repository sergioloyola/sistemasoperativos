class pcb_table:

        def __init__(self):
                self.pcb_table = {}
	
        def put(self, pid,  pcb):
                #self.pcb_table.setdefault(new, pcb)
                self.pid = pid
                self.pcb = pcb
                self.pcb_table.setdefault(self.pid, self.pcb)
        def get_all(self):
                for id in self.pcb_table:
                        print self.pcb_table[id]
