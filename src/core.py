from can import mount
from can import can
from bt import server1
import threading, queue
import atexit
print("AutoCruise has started...")

#Mount the CAN interface
mount.mount()

values = []

# Method to init and bluetooth
def bt(q):
    print("Starting Bluetooth Connection")
    print(q)
    server1.startService()

# Test Method
def test(q):
    print("test q")
    c = 0
    while True:
        c += 1
        if c >= 1000000:
            print("threaded")
            c = 0

q = queue.Queue()

btThread = threading.Thread(target=bt,args=(q))
#canThread = threading.Thread(targe)
testThread = threading.Thread(target=test,args=(q,))

#Start Threads
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
