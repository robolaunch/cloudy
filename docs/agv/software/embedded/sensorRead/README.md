## I2C Muliplexer 

![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2021/07/TCA9548A-How-it-Works.png?resize=739%2C363&quality=100&strip=all&ssl=1)

There are various sensors on Cloudy agv and these sensors work with i2c protocol. Normally the use of sensors with the same i2c addresses is not supported. For this reason, by using the i2c multiplexer electronic card, it is possible to instantly connect to the desired sensor and perform the desired data receiving and sending data operation.

https://github.com/arduino-libraries/Arduino_APDS9960

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
