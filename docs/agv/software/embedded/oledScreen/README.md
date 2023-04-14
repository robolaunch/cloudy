#  Oled Screen SSD1306 

<img style="width:30%; margin-left:auto; margin-right:auto; display:block"  src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/ssd1306_oled_screen.jpg"/>

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
