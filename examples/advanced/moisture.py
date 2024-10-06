import time

import adafruit_shtc3
import board

from grow.moisture import Moisture

print("""moisture.py - Print out sensor reading in Hz

Press Ctrl+C to exit!

""")

i2c = board.I2C()
shtc3 = adafruit_shtc3.SHTC3(i2c)


m1 = Moisture(1)
m2 = Moisture(2)
m3 = Moisture(3)

while True:
    print(f"""1: {m1.moisture}
2: {m2.moisture}
3: {m3.moisture}
T: {shtc3.temperature}
RH: {shtc3.relative_humidity}
""")
    time.sleep(1.0)

