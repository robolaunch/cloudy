# Electronic Requriments

On Cloudy, you can easily integrate sensors using interfaces such as I2C, SPI, analog, and digital pins. The collected sensor data can then be converted into ROS2 topics via the microros platform. Sensors using the I2C interface have better cable tidiness and measurement quality. They also avoid problems caused by sensors with the same I2C addresses as the I2C multiplexer circuit.

## Wemos D1 ESP32 Devkit 1 MCU
<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://ae01.alicdn.com/kf/H4de861835bb241de85a0f85ce23112f9a/ESP32-Wemos-D1-Mini-Arduino-UNO-i-in-R3-D1-R32-WIFI-kablosuz-bluetooth-geli-tirme.jpg"/>

Cloudy is equipped with an embedded system that serves as the central control unit for all sensors and motors. You can download your high level software to the embedded level by using the i2c, spi, can-busi analog, digital pins on the microcontroller and transfer it to real life. The <a href="https://micro.ros.org/"> micro-ros platform</a>, which can work with ROS2, is preferred for communication between the embedded system and SBC. It is a serial protocol that uses micro-ros fastdds technology and transmits industrial-grade data. As the microcontroller <a href="https://www.espressif.com/en/products/socs/esp32"> Esp32 microcontroller</a> which is one of the easily found, cheap and performance chips supported by the micro ros platform, was chosen. The ESP32 Wemos D1 model was chosen for its compactness and compatibility with UNO shields that allow easy integration of additional hardware components.

## Raspberry Pi Single Board Computer

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://tr.farnell.com/productimages/large/en_GB/3051885-40.jpg"/>

In order to utilize the ROS and roslaunch platform, a Linux-based operating system is necessary. For small vehicles like the Cloudy, compact computing systems are often utilized to fulfill the computing requirements. The Cloudy's body has ample room to accommodate these computing systems. In this particular design, a Raspberry Pi 4 with 8GB of RAM has been chosen as the computing solution. robolaunch kubernetes software works with k3s and it needs at least 8gb ram for k3s installation.

##  NEMA 17 Motors
<img src="https://www.robolinkmarket.com/17hs4401s-nema17-step-motor-step-motor-robolink-22359-87-B.webp" style="width:30%; margin-left:auto; margin-right:auto; display:block"/>

Ease of supply, ease of driving, torque and longevity were taken into account in the selection of the motor, which is one of the basic parts of cloudy robot electronics, and a stepper motor, which is used in many fields today, has been preferred. High current (1.7A) nema 17HS8401S motors can carry a load of about 30KG. You can increase the carrying capacity of cloudy with more powerful stepper motors with the same mounting points. If less current draw motors are used, cloudy's operating time will increase.

##  DRV8825 Motor Drivers
<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://productimages.hepsiburada.net/s/37/375/10561893204018.jpg"/>

Stepper motors are controlled by stepper motor drivers and there are large and small versions of them. Since cloudy is a small robot here, drivers such as a4988, tmc2209, drv8825, which are also used in tools such as 3D printers, were preferred. DRV8825 model driver has been selected due to Arduino cnc shield compatibility, ability to work with high current and works silent.

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://www.makerguides.com/wp-content/uploads/2019/02/DRV8825-pinout.jpg"/>

**Features**<br/>
* PWM Microstepping Stepper Motor Driver<br/>
* 8.2-V to 45-V Operating Supply Voltage Range<br/>
* Simple STEP/DIR Interface<br/>
* Up to 1/32 Microstepping
* Silent Working
* 2.5A x 2 Maximum Drive Current at 24 V<br/>


**Vref Settings**
<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://www.nkxmotor.com/wp-content/uploads/2021/05/vref.png"/>

The Vref voltage sets the current of the driver. You should adjust this setting according to the current characteristics of your motor and your purpose. The Vref voltage increases in direct proportion to the driver current. If you increase the driver current too much, the motor will run with more torque, but the driver and motor will draw excessive power and heat up. If the drive current is low, it will cause less electricity consumption, but the torque of the motor, that is, the carrying capacity, will decrease.

The drv8825 default Vref voltage is around ```1.0V```, is enought to the drive robot clearly, but if you want to carry 30KG with the robot, you need to increase the vref voltage to ```2.0V```. The fan in the electronic box will prevent the motor driver from overheating.
 

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

## MPU6050 IMU Sensor 

<img style="width:30%; margin-left:auto; margin-right:auto; display:block"  src="https://www.direnc.net/mpu6050-3-axis-gyro-ve-egim-sensoru-mems-ve-egim-sensorleri-china-29093-62-B.jpg"/>

Required Imu for Cloudy positioning system. Imu is directly connected to sbc computer with i2c protocol. It gives us approximate position and angle information by measuring the speed and acceleration of the robot. The mpu6050 imu consists of 6 DOFs and this number is sufficient for a land vehicle with diff drive. The EKF filter receives the imu data and the desired axes of the imun are selected. By default, only yaw axis data is retrieved from the imu.

Launch IMU:

```bash
cd ~/imu && \
. install/setup.bash && \
ros2 launch mpu6050driver mpu6050driver_launch.py
```

##  SSD1306 Oled Screen

<img style="width:30%; margin-left:auto; margin-right:auto; display:block"  src="https://www.direnc.net/128x64-oled-4pin-is-spi-lcd-display-128x64-grafik-lcd-displays-china-36880-44-B.jpg"/>

The 0.96" Oled display is a small and easy to connect display. It is connected to esp32 via multiplexer using ı2c protocol. The arduino library required for its use and the code on the robot are given below.

https://github.com/adafruit/Adafruit_SSD1306


```
#include "SPI.h"              
#include "Wire.h"              
#include "Adafruit_SSD1306.h" 
#include <Fonts/FreeSerif9pt7b.h>
int width = 128; 
int height = 64; 
int address = 0x3C;  
Adafruit_SSD1306 screen(width, height, &Wire);  

void setup() {
  screen.begin(SSD1306_SWITCHCAPVCC, address); 
  Serial.begin(115200);
}
void loop() {
  screen.clearDisplay(); 
  show_text(74, "Ready"); //demo Batt percentage is 74 and demo Robot Status is Ready 
  screen.display();
}
//define functions
void show_text(int percent, String status) {
  screen.setTextSize(1);  // Yazı boyutu
  screen.setTextColor(SSD1306_WHITE);
  screen.setFont(&FreeSerif9pt7b);
  screen.setCursor(20, 15); 
  screen.print("robolaunch");
  screen.setFont();
  screen.setCursor(10, 30);
  screen.print("Battery  :  % ");
  screen.println(percent);
  screen.setCursor(10, 40);
  screen.print("Status   :  ");
  screen.println(status);
  screen.display();
}

```
## WS2812B Neopixel Leds 
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://www.direnc.net/neopixel-stick-5050-adreslenebilir-rgb-led-serit-diger-led-urunleri-adafruit-44448-46-B.jpg" />
The Neopixel LED allows for individual programming of each LED chip's color, making it perfect for a variety of lighting effects. These effects include light animations, status LEDs, loading bars, and turn signals. Its flexibility and versatility make it a powerful tool for anyone looking to add a unique touch to their lighting design.

 ```/neopixel_led [Float8]``` Led is subscribed to this topic, and changes animation according to the sent numbers.

```0``` Park Mode, front bumper Leds turn white and rear is turn purple<br/>
```1``` Blink Mode, all leds blink for collision avoidance.

https://github.com/adafruit/Adafruit_NeoPixel

```
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif
#define PIN        6 // Esp32 pin for Led
#define NUMPIXELS 32 // Cloudy have connected serial 32 leds.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
void setup() {
#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
  pixels.begin();
}
void headlight() {
  for (int i = 7; i >= 0; i--) {
    pixels.setPixelColor(i, pixels.Color(200, 0, 100));
    j = 15 - i;
    pixels.setPixelColor(j, pixels.Color(200, 0, 100));
    j = 23 - i;
    pixels.setPixelColor(j, pixels.Color(200, 200, 200));
    j = i + 24;
    pixels.setPixelColor(j, pixels.Color(200, 200, 200));
    pixels.show();
  }
}
void loop() {

headlight();
}
``` 

##  INA219 Voltage And Current
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://ae01.alicdn.com/kf/Hf8e46be8e1b044bba6ced52175c80ca0c/10-adet-INA219-GY-219-GY219-ak-m-g-kayna-sens-r-kesme-panosu-mod-l.jpg_Q90.jpg_.webp"/>
<a href="https://tr.aliexpress.com/item/4000983502344.html?spm=a2g0o.productlist.main.15.74684be78NNSOq&algo_pvid=5385c799-29fd-4e92-ab3a-8278056e2b2c&aem_p4p_detail=202303010026424541665638641810003817171&algo_exp_id=5385c799-29fd-4e92-ab3a-8278056e2b2c-7&pdp_ext_f=%7B%22sku_id%22%3A%2210000013192851076%22%7D&pdp_npi=3%40dis%21TRY%2133.86%2127.45%21%21%21%21%21%402100baf316776592024184587d06d2%2110000013192851076%21sea%21TR%21800775013&curPageLogUid=yz0chc5OdZDn&ad_pvid=202303010026424541665638641810003817171_8&ad_pvid=202303010026424541665638641810003817171_8">

INA219</a> sensor utilizes the I2C protocol to provide voltage and current readings. It has a maximum voltage measurement capability of 26V, which is sufficient for monitoring LiPo or Li-ion battery packs with up to 6S. Additionally, it can measure the robot's current consumption up to 3.2 amps.

```/voltage [Float8]``` Topic is publish Battery Voltage </br>
```/current [Float8]``` Topic is publish Instant Current

https://github.com/adafruit/Adafruit_INA219

```
#include <Wire.h>
#include <Adafruit_INA219.h>
Adafruit_INA219 ina219;
void setup(void) 
{
  Serial.begin(115200);
  while (!Serial) {
      delay(1);
  }    
  Serial.println("Hello!");
  if (! ina219.begin()) {
    Serial.println("Failed to find INA219 chip");
    while (1) { delay(10); }
  }
  Serial.println("Measuring voltage and current with INA219 ...");
}
void loop(void) 
{
  float shuntvoltage = 0;
  float busvoltage = 0;
  float current_mA = 0;
  float loadvoltage = 0;
  float power_mW = 0;

  shuntvoltage = ina219.getShuntVoltage_mV();
  busvoltage = ina219.getBusVoltage_V();
  current_mA = ina219.getCurrent_mA();
  power_mW = ina219.getPower_mW();
  loadvoltage = busvoltage + (shuntvoltage / 1000);
  Serial.print("Bus Voltage:   "); Serial.print(busvoltage); Serial.println(" V");
  Serial.print("Shunt Voltage: "); Serial.print(shuntvoltage); Serial.println(" mV");
  Serial.print("Load Voltage:  "); Serial.print(loadvoltage); Serial.println(" V");
  Serial.print("Current:       "); Serial.print(current_mA); Serial.println(" mA");
  Serial.print("Power:         "); Serial.print(power_mW); Serial.println(" mW");
  Serial.println("");
  delay(2000);
}

}
```
 
## APDS-8960 Distance Sensors 

<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://productimages.hepsiburada.net/s/24/375/10076208332850.jpg"/>
<a href="https://tr.aliexpress.com/item/1005003518769618.html?spm=a2g0o.productlist.main.15.27383618OKAScH&algo_pvid=be2f2ec7-98fa-46a3-8b44-ca692cce9eaa&aem_p4p_detail=202303010104574003209801479040003846531&algo_exp_id=be2f2ec7-98fa-46a3-8b44-ca692cce9eaa-7&pdp_ext_f=%7B%22sku_id%22%3A%2212000026150196181%22%7D&pdp_npi=3%40dis%21TRY%2137.67%2137.67%21%21%21%21%21%402100baf316776614974026237d06d2%2112000026150196181%21sea%21TR%21800775013&curPageLogUid=PKbIWPDJSLLR&ad_pvid=202303010104574003209801479040003846531_8&ad_pvid=202303010104574003209801479040003846531_8">

APDS-9960</a> sensor is an advanced sensor with several features. With its distance measurement feature, it allows the robot to detect objects in front of it. In addition, the robot has this sensor in its bumper to detect the ground. This safety feature allows the robot to navigate high surfaces safely without any risk of falling. The sensor also features hand gesture detection and allows the user to send commands to the robot with intuitive gestures. This feature makes it easy for anyone, regardless of technical expertise, to control the robot. Finally, the sensor includes an RGB color detection feature that provides information about the colors in the robot's environment. It has many practical applications such as adding this feature to the bottom sensor of the robot and recognizing the ground color.

 ```/right_collision_distance [Float8]``` Topic is publish distance between 4-8 inch
 ```/left_collision_distance [Float8]``` Topic is publish distance between 4-8 inch
  ```/ground_floor [Boolean]``` Topic is publish if detect ground floor True else False

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
##  AS5600 Motor Encoder
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://ae01.alicdn.com/kf/H50439b1bc6a9428e9af7024ce3474465P/AS5600-manyetik-kodlay-c-manyetik-nd-ksiyon-a-s-l-m-sens-r-mod-l-12bit.jpg_Q90.jpg_.webp"/>
<a href="https://tr.aliexpress.com/item/4001145068547.html?spm=a2g0o.productlist.main.3.5ef93747hGhVQf&algo_pvid=e088815a-848d-4625-a702-3fa0a540f93d&aem_p4p_detail=202303010340167927039469412100004309933&algo_exp_id=e088815a-848d-4625-a702-3fa0a540f93d-1&pdp_ext_f=%7B%22sku_id%22%3A%2210000014887911007%22%7D&pdp_npi=3%40dis%21TRY%2124.04%2122.84%21%21%21%21%21%402100b88516776708168128835d06c2%2110000014887911007%21sea%21TR%21800775013&curPageLogUid=hrZCnCXrbPlG&ad_pvid=202303010340167927039469412100004309933_2&ad_pvid=202303010340167927039469412100004309933_2">

AS5600 Encoder</a> sensor works with i2c connection and can share position and speed information of wheels with 4096 pulse in 1 turn.Cloudy robot uses step count of stepper motors instead of encoder by default, but supports this sensor for improvements.

## Voltage Regulators
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://m.media-amazon.com/images/I/61ylcedZCBL._AC_UF1000,1000_QL80_.jpg"/>

Battery Eliminator Circuit (BEC) is converting battery voltage to demanded voltage such as 5V. Cloudy robot's SBC and microcontroller works with 5v. Since both can draw high currents, separate bec circuits are used in the robot for both. <a href="https://tr.aliexpress.com/item/32256292826.html?pdp_npi=2%40dis%21TRY%21TRY%20473.93%21TRY%20236.95%21%21%21%21%21%40211b446516777645114013824e2321%2112000028967443703%21btf&_t=pvid%3Aa7db28e0-30b3-408c-8964-39b7a42f84a8&afTraceInfo=32256292826__pc__pcBridgePPC__xxxxxx__1677764511&spm=a2g0o.ppclist.product.mainProduct&gatewayAdapt=glo2tur">Hobbywing 5V 3A</a> bec circuit can give 15w, is enought for microcontroller and Raspberry Pi 4. But if you want more power <a href="https://tr.aliexpress.com/item/4000013753385.html?pdp_npi=2%40dis%21TRY%21TRY%20160.18%21TRY%20160.17%21%21%21%21%21%40211b446516777646754255619e2321%2110000000034287844%21btf&_t=pvid%3A8b55dd82-d8d1-47b4-83b8-5c99c8c8bf95&afTraceInfo=4000013753385__pc__pcBridgePPC__xxxxxx__1677764675&spm=a2g0o.ppclist.product.mainProduct&gatewayAdapt=glo2tur">Henge 5V 6A </a>bec circuit is a good choice.


## Battery 
<img style="width:40%; margin:0 50px 0 50px; float:left;" src="https://sc04.alicdn.com/kf/H679bc52188464178b6d691d1a91de5cfP.jpg"/>
<img style="width:40%;" src="http://sc04.alicdn.com/kf/H0fd0f1acec0342899e9b45ce4fa5bbdeT.jpg"/>

The power required for the operation of all systems on Cloudy is obtained from 18650 lion batteries in a 6s1p arrangement.The 3200mAh capacity of the battery allows Cloudy to run for a duration of over two hour. By modifying the battery cover to accommodate larger batteries, the operating time can potentially be extended to 10 hours.
<div style="margin: 0 0 0 100px" >

| Payload 	| Test Type 	| Duration 	| BattV Starting 	| BattV Finishing 	| Notes 	|
|:---:	|:---:	|:---:	|:---:	|:---:	|:---:	|
| 2KG 	| Driving 	| 30 Minutes 	| 24.2 	| 22.9 	| Ok 	|
| 8KG 	| Driving 	| 30 Minutes 	| 22.9 	| 21.95 	| Ok 	|
| 0KG 	| Stopping 	| 30 Minutes 	| 21.95 	| 21.48 	| Ok 	|

 </div>