# https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
#from servo import Servos
from machine import Pin, I2C
from servo import Servos
from time import sleep_ms

# machine.I2C(id, *, scl, sda, freq=400000)
# SCL -> Pin(21)
# SDA -> Pin(20)
ID = 0
_scl = Pin(1)
_sda = Pin(0)
i2c = I2C( id=ID, scl=_scl, sda=_sda)
adr_room = i2c.scan()
for adr in adr_room:
    print(hex(adr))

    
servo_board = Servos(i2c=i2c)

for servo in range(16):
    servo_board.position(index=servo, degrees=0)

sleep_ms(3000)
for servo in range(16):
    servo_board.position(index=servo, degrees=90)
    
sleep_ms(3000)
for servo in range(16):
    servo_board.position(index=servo, degrees=180)