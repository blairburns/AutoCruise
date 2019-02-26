from can import mount
from can import can
from bt import server1

print("AutoCruise has started...")

#Mount the CAN interface
mount.mount()

def startBT():
	print("Starting Bluetooth Connection")
	server1.startService()


startBT()

while True:
	test = "yes"

#

