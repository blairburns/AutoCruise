import can
from threading import Thread




can.running = True
can.candump()

#can.receive()

#def dump():
#	c.candump()
#t = Thread(target=dump)
#t.start()

#def change():
#	for  x in range(10000):
#		if x > 1000:
#			can.running = False
#			print("tes")
#
#b = Thread(target=change)
#b.start()
