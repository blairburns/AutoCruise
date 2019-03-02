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
btConnected = False

can.start()

sBT_queue = queue.Queue()
rBT_queue = queue.Queue()
sCAN_queue = queue.Queue()
rCAN_queue = queue.Queue()
btStatus = queue.Queue()
q = queue.Queue()

# Method to init and bluetooth
def bt(btStatus):
    print("Starting Bluetooth Connection")
    server.startService(btStatus)
    print("Client info: " + str(btStatus.get()))


def sendBT(data):
    server.sendData(data)

def sendCAN(frame):
    #nothing yet
    yep = "yep"


# Test Method

def test():
    print("is it connected? " + str(btStatus.get()))
    while True:
        print("threaded")
        frame = can.receive()
        sendBT(frame)
        sendBT("sending")
        time.sleep(.2)

btThread = threading.Thread(target=bt, args=(btStatus,))
#canThread = threading.Thread(targe)
#testThread = threading.Thread(target=test,args=(q,sBT_queue))

#Start Threads
btThread.start()


test()
