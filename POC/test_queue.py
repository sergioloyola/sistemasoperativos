from queue import *

#### setup
cola = queue()
x= PCB(6, "Waiting",  31032016, 9, 15)
y= PCB(5, "Running",  01042016, 3, 20)
z= PCB(7, "Waiting",  10042016, 10, 13)
h= PCB(10, "Waiting",  12042016, 12, 5)

cola.put_ready(x)
cola.put_ready(y)
cola.put_ready(z)
cola.put_ready(h)

#### Test
next = cola.get_next()
while next is not None: 
	print(next)
	next = cola.get_next()
