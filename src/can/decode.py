from canard import can, bus
import jsondb
from canard.hw import socketcan

parser = jsondb.JsonDbParser()
b = parser.parse('example_db.json')

dev = socketcan.SocketCanDev('can0')
dev.start()

while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        for s in signals:
            print(s)
