from schedule import *
from queue import *

#### setup
cola = queue()
tarea = SchedulePriority()
#x= PCB(6, "Waiting",  31032016, 1, 15)
y= PCB(5, "Running",  01042016, 2, 20)
a= PCB(5, "Running",  01042016, 2, 20)
b= PCB(5, "Running",  01042016, 2, 20)
z= PCB(7, "Waiting",  10042016, 4, 13)
h= PCB(10, "Waiting",  12042016, 5, 5)

tarea.put(a)
tarea.put(b)
#tarea.put(x)
tarea.put(y)
tarea.put(z)
tarea.put(h)

#### Test
next = tarea.get_next()
while next is not None:
        print(next)
        next = tarea.get_next()
