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
 

