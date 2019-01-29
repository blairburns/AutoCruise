from canard import can
from canard.hw import socketcan

# SocketCAN Interface connecting directly to CAN Device

running = True;

# Open device connection
dev = socketcan.SocketCanDev("can0")
dev.start()

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
