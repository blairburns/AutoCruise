from can import mount
from can import can
from bt import server1
import threading, queue
import atexit
print("AutoCruise has started...")

#Mount the CAN interface

values = []
stopEvent = threading.Event()

#def startup():
mount.mount()
    #server1.startService()

def bt(q, stopEvent):
    print("Starting Bluetooth Connection")
    print(q)
    server1.startService()

def test(q):
    print("test q")
    c = 0
    while True:
        c += 1
        if c >= 1000000:
            print("threaded")
            c = 0

q = queue.Queue()
btThread = threading.Thread(target=bt,args=(q,stopEvent))
#canThread = threading.Thread(targe)
testThread = threading.Thread(target=test,args=(q,))

btThread.start()
testThread.start()


#startBT()

while True:
	test = "yes"

#

def exitHandler():
    print("Closing Core.py and it's subsidies")
    stopEvent.set()

atexit.register(exitHandler)
