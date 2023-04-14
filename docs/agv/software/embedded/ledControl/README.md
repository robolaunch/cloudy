# Neopixel Leds WS2812B

<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/neopixel_led.jpg" />

Neopixel led have individual rgb control chip per every led, so you can change the color of each led individually. Cloudy Mini-AGV have headlight, blink led example and you can add more function.

For more info about neopixel leds please check [**here**](https://learn.adafruit.com/adafruit-neopixel-uberguide).

 ```/neopixel_led [Float8]``` Led is subscribed to this topic, and changes animation according to the sent numbers.

```0``` Park Mode, front bumper Leds turn white and rear is turn purple<br/>
```1``` Blink Mode, all leds blink for collision avoidance.

Example: ```ros2 topic pub /neopixel_led std_msgs/msg/Int8 data:\ 1\ ```

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
