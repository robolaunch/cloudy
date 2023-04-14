# Electrical Components

## WS2812B Neopixel Leds 
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/neopixel_led.jpg" />

The Neopixel LED allows for individual programming of each LED chip's color, making it perfect for a variety of lighting effects. These effects include light animations, status LEDs, loading bars, and turn signals. Its flexibility and versatility make it a powerful tool for anyone looking to add a unique touch to their lighting design.

##  SSD1306 Oled Screen

<img style="width:30%; margin-left:auto; margin-right:auto; display:block"  src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/ssd1306_oled_screen.jpg"/>

The 0.96" Oled display is a small and easy to connect display. It is connected to esp32 via multiplexer using ı2c protocol. The arduino library required for its use and the code on the robot are given below. Visit [**here**](https://github.com/adafruit/Adafruit_SSD1306) for more.


##  DRV8825 Motor Drivers
<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/drv8825.jpg"/>

Stepper motors are controlled by stepper motor drivers and there are large and small versions of them. Since cloudy is a small robot here, drivers such as a4988, tmc2209, drv8825, which are also used in tools such as 3D printers, were preferred. DRV8825 model driver has been selected due to Arduino cnc shield compatibility, ability to work with high current and works silent.

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/drv8825_pinout.jpg"/>

**Features**<br/>
* PWM Microstepping Stepper Motor Driver<br/>
* 8.2-V to 45-V Operating Supply Voltage Range<br/>
* Simple STEP/DIR Interface<br/>
* Up to 1/32 Microstepping
* Silent Working
* 2.5A x 2 Maximum Drive Current at 24 V<br/>


**Vref Settings**
<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/vref_setting.png"/>

The Vref voltage sets the current of the driver. You should adjust this setting according to the current characteristics of your motor and your purpose. The Vref voltage increases in direct proportion to the driver current. If you increase the driver current too much, the motor will run with more torque, but the driver and motor will draw excessive power and heat up. If the drive current is low, it will cause less electricity consumption, but the torque of the motor, that is, the carrying capacity, will decrease.

The drv8825 default Vref voltage is around ```1.0V```, is enought to the drive robot clearly, but if you want to carry 30KG with the robot, you need to increase the vref voltage to ```2.0V```. The fan in the electronic box will prevent the motor driver from overheating.
 
## Ibus Receiver Flysky ia6b

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/flysky_ia6b.jpg"/>

An rc system with flysky ibus protocol has been chosen due to its easy availability, simplicity, durability and easy software programming. Flysky i6, i6X, i6S controllers are compatible as ibus-compatible. Since the ibus pin sends data to the microcontroller, it works by connecting to one of the serial rx pins.

For alternative you can use other ibus receivers; Flysky x6b, Flysky ia10b, FS-rx2a, Uruav ux14, Flit10.