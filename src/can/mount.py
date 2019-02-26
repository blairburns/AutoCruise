import subprocess
import time


#try:
#	subprocess.check_output(['slcand -o -c -s6 /dev/ttyACM0 can0'], shell=True)
#	time.sleep(3)
#	subprocess.run(['ip link set can0 up'], shell=True)
#	print("Successfully connected to the CAN Interface")
#except:
#	print("Failed to initiate the CAN interface")


def mount():
	try:
        	subprocess.check_output(['slcand -o -c -s6 /dev/ttyACM0 can0'], shell=True)
        	time.sleep(3)
        	subprocess.run(['ip link set can0 up'], shell=True)
        	print("Successfully connected to the CAN Interface")
	except:
        	print("Failed to initiate the CAN interface")
