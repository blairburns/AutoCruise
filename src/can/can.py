from canard import can
from canard.hw import socketcan

# SocketCAN Interface connecting directly to CAN Device

running = True;

dev = None

# Open device connection
def start():
    global dev
    dev = socketcan.SocketCanDev("can0")
    dev.start()
    print("called")

start()


# Receive frame from CAN Interface 
def receive():
	frame = dev.recv()
	return str(frame)


# Send frame to CAN Interface 
def send(frame):
	dev.send(frame)


def candump():
	print("candump")
	frame = dev.recv()
	return str(frame)
	#if running == True:
	candump()
