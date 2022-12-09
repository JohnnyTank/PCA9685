import PCA9685
from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(20), sda=Pin(21), freq=100000)
adr_room = i2c.scan()
for adr in adr_room:
    print(hex(adr))