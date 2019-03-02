import os
import glob
import time
import random

from bluetooth import *
import queue

server_sock = BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

acceptedConnection = False
client_sock = None
client_info = None


uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "AutoCruise",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )


def openThreads():
  print("Starting send and receive threads")

  
def startService(btStatus):
    print("Waiting for connection on RFCOMM channel %d" % port)
    global client_sock, client_info
    client_sock, client_info = server_sock.accept()
    btStatus.put(client_info)
    #server_sock.accept()
    print("Accepted connection from ") #, client_info)
    acceptedConnection = True
    #q.put(acceptedConnection)
    #print(q)
    openThreads()

def sendData(data, q):
    #client_sock, client_info = server_sock.accept()
    client_sock.send(data)
    test = "yes this worked"
    q.put(test)

def recData():
    try:
        req = client_sock.recv(1024)
        if len(req) == 0:
            print("No data")
        print("received [%s]" % req)
        client_sock.send(req)

        data = None
        if req in ('temp', '*temp'):
            data = str(random.random())+'!'
        else:
            pass

        if data:
            print("sending [%s]" % data)
            client_sock.send(data)

    except IOError:
        pass

    except KeyboardInterrupt:

        print("disconnected")

        client_sock.close()
        server_sock.close()
        print("all done")

