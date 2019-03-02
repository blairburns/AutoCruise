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

can.start()

sBT_queue = queue.Queue()
rBT_queue = queue.Queue()
sCAN_queue = queue.Queue()
rCAN_queue = queue.Queue()
btStatus = queue.Queue()
q = queue.Queue()

# Method to init and bluetooth
def bt():
    print("Starting Bluetooth Connection")
    server.startService(btStatus)
    print("Client info: " + str(btStatus.get()))


def sendBT(data):
    server.sendData(data, sBT_queue)

def sendCAN(frame):
    #nothing yet
    yep = "yep"


# Test Method

def test():
    c = 0
    #can.start()
<<<<<<< HEAD
    while True:
        #print("threaded")
=======
    while btStatus.get() == True: #True
        print("threaded")
>>>>>>> d340d8874d90cde54cf44506e597809c9f540a3e
        frame = can.receive()
        try:
            sendBT(frame) #server1.sendData("Sending test\n", q    
        except:
            continue
        time.sleep(.1)

btThread = threading.Thread(target=bt, args=(btStatus,))
#canThread = threading.Thread(targe)
#testThread = threading.Thread(target=test,args=(q,sBT_queue))

#Start Threads
btThread.start()
#testThread.start()

test()

#startBT()
