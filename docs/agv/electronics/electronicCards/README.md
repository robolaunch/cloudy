# Electronic Cards
## TCA9548A I2C Multiplexer 

<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/multiplexer.jpg">

A multiplexer is a system that selects one of more than one analog or digital data source and transmits this source to a single channel as output. A multiplexer divides a single high-speed communication circuit into several low-speed circuits, allowing several devices to take advantage of this circuit at the same time. There are many arduino sensors working with i2c, they are preferred in Cloudy Mini-AGV due to their wide variety, lack of cables and powerful features. Cloudy Mini-AGV includes a multiplexer to use more than 1 of the same sensor, so you can easily connect as many same-different sensors as you want.  
## CNC Shield

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cnc_shield.jpg"/>

Cnc shield is produced as arduino uno shield and up to 4 stepper motor drivers can be connected. It facilitates the assembly and cooling of stepper motors, stepper adjustment and vref adjustment, eliminates 
cable crowding, and protects it from voltage fluctuations with the capacitors on it. You can use the empty pins on it to wiring to the sensors. The connection pins of the sensors connected to the Cloudy Mini-AGV are as follows.

| Sensor Name 	| CNC Shield Pin 	| ESP32 Pin 	| 
|         :---:	|:---:	    |:---:  |
| RC Receiver 	| X_DIR 	| D16 	|  
| Neopixel Led 	| X_STEP 	| D2 	| 

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cnc_shield_jumper.png"/>

There are 6 pins under the driver. With these pins, the step resolution of the stepper motor is adjusted. The number of steps is reduced to 1/8 by installing 2 jumpers on the M0 and M1 slots marked Cloudy Mini-AGV. This movement increases fluidity and resolution.

