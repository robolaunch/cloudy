## Software Setup

**Microcontroller Setup**

The Cloudy robot utilizes the Arduino IDE for programming and uploading to the microcontroller. It is suggested to use version 2.0 or higher of the Arduino IDE for an easier experience. Additionally, the Cloudy robot utilizes several Arduino libraries, which should be added to the Arduino IDE prior to programming. The necessary libraries can be found and downloaded below. 

https://github.com/micro-ROS/micro_ros_arduino

https://github.com/gin66/FastAccelStepper

https://github.com/bmellink/IBusBM

https://github.com/adafruit/Adafruit_NeoPixel

**SBC Computer Setup**

1. Download ubuntu 20.04 image for selected SBC.
2. Write the image to sd card with win32 disk imager or balena etcher.
3. Install ROS2 from <a href="https://docs.ros.org/en/humble/Installation.html">ROS2 Humble installation</a>.
4. Clone the cloudy robot repository from https://github.com/robolaunch/cloudy
5. Clone the micro ros setup from https://github.com/micro-ROS/micro_ros_setup


The Cloudy robot utilizes Micro ROS for connecting to ROS2. In order to use the Cloudy robot with ROS2, it is necessary to setup the Micro ROS Agent package on the SBC computer that will be controlling the robot.

```ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0```
