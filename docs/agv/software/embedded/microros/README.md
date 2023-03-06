![](https://micro.ros.org/img/micro-ROS_big_logo.png)

**Microcontroller Setup**

The Cloudy robot utilizes the Arduino IDE for programming and uploading to the microcontroller. It is suggested to use version 2.0 or higher of the Arduino IDE for an easier experience. Additionally, the Cloudy robot utilizes several Arduino libraries, which should be added to the Arduino IDE prior to programming. The necessary libraries can be found and downloaded below. 

1. Download Arduino IDE from https://www.arduino.cc/en/software

2. Download esp32 board add-on and select ESP32 Dev Module

3. Download to this required libraries from github or arduino libraries page.

    https://github.com/micro-ROS/micro_ros_arduino

    https://github.com/gin66/FastAccelStepper

    https://github.com/bmellink/IBusBM

    https://github.com/adafruit/Adafruit_NeoPixel

4. Copy and Paste that code in arduino ide and upload to board.

    https://github.com/robolaunch/cloudy/blob/main/robolaunch_cloudy_hardware/firmware/firmware_flysky.ino


?> For embedded software side of SBC click and go to the <a>SBC Software</a>