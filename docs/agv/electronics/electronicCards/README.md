
## TCA9548A I2C Multiplexer 

<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://cdn-learn.adafruit.com/guides/cropped_images/000/001/124/medium640/tcasmall.jpg?1515089926">

A multiplexer is a system that selects one of more than one analog or digital data source and transmits this source to a single channel as output. A multiplexer divides a single high-speed communication circuit into several low-speed circuits, allowing several devices to take advantage of this circuit at the same time. There are many arduino sensors working with i2c, they are preferred in cloudy robot due to their wide variety, lack of cables and powerful features. Cloudy includes a multiplexer to use more than 1 of the same sensor, so you can easily connect as many same-different sensors as you want.
Below is an example of simultaneous data acquisition of 3 apds-9960 distance and motion sensors using i2c and multiplexer.
 ```
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_APDS9960.h>
#include <Adafruit_TCA9548A.h>

#define TCAADDR 0x70 // TCA9548A adress
Adafruit_TCA9548A tca = Adafruit_TCA9548A(TCAADDR);

#define APDSADDR1 0x39 // APDS-9060 1 adress
#define APDSADDR2 0x29 // APDS-9060 2 adress
#define APDSADDR3 0x49 // APDS-9060 3 adress
Adafruit_APDS9960 apds1, apds2, apds3;

void setup() {
  Wire.begin(21, 22); // I2C pimleri ayarla
  Wire.beginTransmission(TCAADDR);
  Wire.write(0);
  Wire.endTransmission();
  Serial.begin(9600);

  tca.begin();
  if (!apds1.begin(APDSADDR1, &tca)) {
    Serial.println("APDS-9060 1 sensors couldn't find.");
    while (1);
  }
  if (!apds2.begin(APDSADDR2, &tca)) {
    Serial.println("APDS-9060 2 sensors couldn't find.");
    while (1);
  }
  if (!apds3.begin(APDSADDR3, &tca)) {
    Serial.println("APDS-9060 3 sensors couldn't find.");
    while (1);
  }

  apds1.enableLightSensor(false); // Activate light sensor
  apds2.enableLightSensor(false);
  apds3.enableLightSensor(false);
}

void loop() {
  // TCA9548A channel 0
  tca.select(1 << 0);
  uint16_t als1 = apds1.readAmbientLight();
  Serial.print("APDS-9060 1: ");
  Serial.print(als1);
  Serial.println(" lux");

  // TCA9548A channel 1
  tca.select(1 << 1);
  uint16_t als2 = apds2.readAmbientLight();
  Serial.print("APDS-9060 2: ");
  Serial.print(als2);
  Serial.println(" lux");

  // TCA9548A channel 2
  tca.select(1 << 2);
  uint16_t als3 = apds3.readAmbientLight();
  Serial.print("APDS-9060 3: ");
  Serial.print(als3);
  Serial.println(" lux");

  delay(1000);
}


```

## CNC Shield

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://www.direnc.net/arduino-uno-cnc-shield-3d-printer-parcalari-china-22203-95-B.jpg"/>

Cnc shield is produced as arduino uno shield and up to 4 stepper motor drivers can be connected. It facilitates the assembly and cooling of stepper motors, stepper adjustment and vref adjustment, eliminates 
cable crowding, and protects it from voltage fluctuations with the capacitors on it. You can use the empty pins on it to wiring to the sensors. The connection pins of the sensors connected to the cloudy robot are as follows.

| Sensor Name 	| CNC Shield Pin 	| ESP32 Pin 	| 
|         :---:	|:---:	    |:---:  |
| RC Receiver 	| X_DIR 	| D16 	|  
| Neopixel Led 	| X_STEP 	| D2 	| 

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cnc_shield_jumper.png"/>

There are 6 pins under the driver. With these pins, the step resolution of the stepper motor is adjusted. The number of steps is reduced to 1/8 by installing 2 jumpers on the M0 and M1 slots marked Cloudy. This movement increases fluidity and resolution.

