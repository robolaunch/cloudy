#include "SPI.h"              
#include "Wire.h"              
#include "Adafruit_SSD1306.h" 
#include <Fonts/FreeSerif9pt7b.h>

int genislik = 128; 
int yukseklik = 64; 
int adres = 0x3C;  
Adafruit_SSD1306 ekran(genislik, yukseklik, &Wire);  

void setup() {
  ekran.begin(SSD1306_SWITCHCAPVCC, adres); 
}
void loop() {
  ekran.clearDisplay(); 
  yaziyaz(68, "Ready"); 
  ekran.display();
}


//define functions
void yaziyaz(int percent, String status) {
  ekran.setTextSize(1);  // Yazı boyutu
  ekran.setTextColor(SSD1306_WHITE);
  ekran.setFont(&FreeSerif9pt7b);
  ekran.setCursor(20, 15); 
  ekran.print("robolaunch");
  ekran.setFont();
  ekran.setCursor(10, 30);
  ekran.print("Battery  :  % ");
  ekran.println(percent);
  ekran.setCursor(10, 40);
  ekran.print("Status   :  ");
  ekran.println(status);
  ekran.display();
}
void draw_rect() {
  ekran.clearDisplay();
  ekran.drawRect(0, 0, 128, 32, SSD1306_WHITE);
  ekran.display();
}