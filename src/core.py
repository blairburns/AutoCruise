from can import mount
mount.mount()
from can import can
from bt import server1 as server
import threading, queue
import time
print("AutoCruise has started...")

#Mount the CAN interface
#mount.mount()

values = []
acceptedConnection = False

sBT_queue = queue.Queue()
rBT_queue = queue.Queue()
sCAN_queue = queue.Queue()
rCAN_queue = queue.Queue()
q = queue.Queue()

# Method to init and bluetooth
def bt():
    print("Starting Bluetooth Connection")
    server.startService()


def sendBT(data):
    server.sendData(data, sBT_queue)

def sendCAN(frame):
    #nothing yet
    yep = "yep"


# Test Method

def test():
    c = 0
    while True:
        print("threaded")
        try:
            sendBT("This is sending") #server1.sendData("Sending test\n", q    
        except:
            pass
	#try:
        time.sleep(.1)
             #   print(q.get())
            #except:
             #   print("didn't work")


btThread = threading.Thread(target=bt)
#canThread = threading.Thread(targe)
#testThread = threading.Thread(target=test,args=(q,sBT_queue))

#Start Threads
btThread.start()
#testThread.start()

test()

#startBT()
