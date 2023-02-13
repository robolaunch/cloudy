## Overview
Cloudy uses the esp32 micro controller on the embedded hardware side.

Cloudy robot has a Hardware Stack containing the main electronics and computer, all the parts here are cooled by a powerful fan. The Hardware Stack is easily separated from the body of the cloudy, which allows you to easily replace them and use them outside of the robot.

The first layer of the Hardware Stack contains an esp32 microcontroller. This board is known as uno esp32 and is compatible with most arduino uno shields.

The second layer contains shield for the motor drivers. Depending on your motor type (step, dc, brushless) you can choose different shield to the compatible driver board.this layer ensures the stable operation of the motor drivers.

On the top layer, there is a single board computer. Cloudy supports raspberry pi, orange pi 5, jetson nano and Intel Nuc computers. You can easily access the USBs on it and use add-ons such as stereo camera and lidar.

In addition, the body of the Cloudy is equipped with many sensors. These sensors work with i2c protocol and are connected with i2c multiplexer so you can connect multiple same sensors.Cloudy includes 3 distance sensors, 2 for collision avoidance in the bumper, and 1 for protection from falling from a height. Also there are neopixel LEDs on all four sides, these LEDs are used for robot visibility and status indication. You can learn the battery voltage and status with the tiny oled screen at the top.
<br/>
<br/><br/>
<br/>

## Components
<img src="https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/cloudy-open-version.pngs">

## Environments & Setup
**Wiring Simulation**

The electronic schematic for the Cloudy robot has been created using the free, open-source tool Fritzing. This tool can be downloaded from its official website. The Fritzing design for the Cloudy robot can be accessed and downloaded from the provided link below.

https://fritzing.org/<br/>
<a href="#">Cloudy Fritzing Design</a>

**Microcontroller Setup**

The Cloudy robot utilizes the Arduino IDE for programming and uploading to the microcontroller. It is suggested to use version 2.0 or higher of the Arduino IDE for an easier experience. Additionally, the Cloudy robot utilizes several Arduino libraries, which should be added to the Arduino IDE prior to programming. The necessary libraries can be found and downloaded below. 

https://github.com/micro-ROS/micro_ros_arduino

https://github.com/gin66/FastAccelStepper

https://github.com/ibus/ibus

https://github.com/adafruit/Adafruit_NeoPixel

**SBC Computer Setup**

1. Download ubuntu 20.04 image for selected SBC.
2. Write the image to sd card with win32 disk imager or balena etcher.
3. Install ROS2 from <a href="https://docs.ros.org/en/humble/Installation.html">ROS2 Humble installation</a>.
4. Clone the cloudy robot repository from https://github.com/robolaunch/cloudy
5. Clone the micro ros setup from https://github.com/micro-ROS/micro_ros_setup


The Cloudy robot utilizes Micro ROS for connecting to ROS2. In order to use the Cloudy robot with ROS2, it is necessary to setup the Micro ROS Agent package on the SBC computer that will be controlling the robot.

```ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0```

For detailed explanation please check [Electronic Components](/Electrical%26ElectronicalDesign/Development%26Production/Components/)
## Actual Architecture

## Actuators


## Cabling & Mounting
**Tools for Cloudy Robot**

The Cloudy robot is compact and hooded, making it important to have some basic hobby tools on hand for assembly. It is crucial to ensure that the wires are installed firmly and in an organized manner for optimal functionality and appearance of the robot."

<img style="width:180px; height:180px; margin:30px;" src="https://productimages.hepsiburada.net/s/184/550/110000148856195.jpg/format:webp"/>
<img style="width:180px; height:180px;  margin:30px;" src="https://www.robolinkmarket.com/montaj-kablosu-paketi-22awg-6x15m-cok-damarli-jumper-dupont-kablo-marxlow-6995-71-O.webp"/>
<img style="width:180px; height:150px; margin-bottom:40px;" src="https://st.myideasoft.com/idea/jd/10/myassets/products/474/isiso-hs-700d-kablo-soyma-pensesi-perpaotomasyon.jpg?revision=1646898140"/>

?>  It is important to verify that the mechanical assembly of the device has been completed fully before proceeding to this step."

**Wiring Diagram**

See below for a wiring diagram of the Cloudy robot. You may find it useful to reference this during the assembly process.It can also download for <a href="#">fritzing file</a>

<img src="https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/cloudy_hardware5_bb.png">

**Box Stack Installation**


1. Wemos ESP32 D1
2. Raspberry Pi 4
3. Arduino CNC Shield
4. DRV8825 Motor Driver x2
5. 24V Fan
6. Jumper pin x4


## Interfaces and Integration
## Troubleshoot and Tips