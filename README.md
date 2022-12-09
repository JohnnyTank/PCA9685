# PCA9685
 Connecting Servos to the Pi Pico W
 
 The PCA9685 is a device for steering up to 16 Servos.
 (For reference get the pdf-Documentation from AZ Delivery)

It works with the I2C protocol.
If you don't solder any bridges on the module the basic adress is 0x40.

im using the Driver provided by ardafruit.
Please Connect:
PCA9685 -> PI PICO (W)
 GND -> GND
 
 SDA -> GP21
 
 SCL -> GP20
 
 VCC -> 3V3
 
A RED LED should light up on the servo board.
