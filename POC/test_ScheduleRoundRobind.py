from schedule import *
from queue import *

#### setup
cola = queue()
#tarea = ScheduleFCFS()
tarea = ScheduleRound_robin()
x= PCB(6, "Waiting",  31032016, 9, 15)
y= PCB(5, "Running",  01042016, 3, 20)
z= PCB(7, "Waiting",  10042016, 10, 13)
h= PCB(10, "Waiting",  12042016, 12, 5)

tarea.put(x)
tarea.put(y)
tarea.put(z)
tarea.put(h)

#### Test
next = tarea.get_next()
while next is not None:
	print(next)
        next = tarea.get_next()

