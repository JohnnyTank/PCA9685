# PCA9685
 Connecting Servos to the Pi Pico W
 
 The PCA9685 is a device for steering up to 16 Servos.
 (For reference get the pdf-Documentation from AZ Delivery)

It works with the I2C protocol.
If you don't solder any bridges on the module the basic adress is 0x40.

im using the Driver provided by [Kevin McAleer](https://github.com/kevinmcaleer/pca9685_for_pico).

Please Connect:

PCA9685 -> PI PICO (W)

GND -> GND
 
 * SDA -> GP20
 
 * SCL -> GP21
 
 * VCC -> 3V3
 
A RED LED should light up on the servo board.

You need a Powersource that is strong enough for the board.
The Voltage between anny black and anny red Pin on the servoboard should be about 5V.

I Am using an Pico-expansionboard by keyestudio which has a powerconnector for up to 12V - so you can get the 5V Suply for the Servos from the Board.

Don't use the Pico as Powersupply for the servos - it will get damaged!
