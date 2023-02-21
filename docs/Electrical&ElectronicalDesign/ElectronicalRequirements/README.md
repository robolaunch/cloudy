
# General Robot Build Roadmap: 
This roadmap shows the order of parts to be selected for robot manufacture for all robot types. Starting from step 1, you can create the robot you want to build. Cloudy Robot was created with use this roadmap.
<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/BUsidHoXK9xqfDExd4iyRW@7YNFXnKbYmPnTJDWNcchx"></iframe>

# Chassis
The Cloudy AGV (Automated Guided Vehicle) features a differential drive control system with free-wheeling capabilities on all four sides. It is designed for indoor operation on flat floors and has a maximum carrying capacity of 30 kilograms. Additional payloads, such as robotic arms and drones, can be integrated onto the Cloudy platform to increase its functionality.
<br>

# Motors
The Nema 17 stepper motor has been selected for use in the Cloudy due to its durability, quiet operation, and increased torque (achieved through the use of a drive belt). To further enhance performance, two gaskets made of rubber are employed. It should also be noted that the design of the Cloudy can be modified to allow for the use of brushed motors with DC encoders.
<br>

# Motor Driver Shield
To maximize the output power from the Nema 17 motors, the Cloudy utilizes DRV8825 motor drivers. The Vref voltage of these drivers has been increased to 1.8 volts, allowing for a maximum carrying capacity of 30 kilograms. A fan within the hardware box is employed to effectively remove any heat generated during operation.

# Embedded Hardware
The Cloudy is equipped with an embedded system that serves as the central control unit for all sensors and motors. Commands can be sent to the embedded system from a computer, such as speed commands, or relevant data can be read, such as battery voltage. The embedded system supports various software controllers, including ROS, ROS2, Ardupilot, and PX4. In this design, the Cloudy utilizes the ROS2 platform and employs an ESP32 microcontroller due to its micro-ROS support. The ESP32 Arduino UNO version was selected for its compactness and compatibility with UNO shields, allowing for easy integration of additional hardware components.
# Sensors & Perhiperals

Cloudy is equipped with a variety of sensors. When using sensors that operate using the I2C protocol, it is not possible to connect multiple identical sensors directly. To address this issue, the Cloudy employs a TCA9548 I2C multiplexer, which enables the connection of up to 8 identical or different I2C sensors. This number can be increased through modifications to the Cloudy's design. Currently, the Cloudy features 3 VL6180X distance sensors (2 at the bumper and 1 at the bottom), 8 programmable NeoPixel LED lights located at the 4 corners, and a 0.96-inch mini OLED screen.
 # Single Board Computer

 In order to utilize the ROS and roslaunch platform, a Linux-based operating system is necessary. For small vehicles like the Cloudy, compact computing systems are often utilized to fulfill the computing requirements. The Cloudy's body has ample room to accommodate these computing systems. In this particular design, a Raspberry Pi 4 with 8GB of RAM has been chosen as the computing solution.
 # Add-Ons

By incorporating hardware accessories, you can expand the functionality of your robot. The thermal camera can detect any heat anomalies, while the 360 camera provides situational awareness. Cloudy comes equipped with a Rplidar A1M8 lidar model and an intel realsense d435i stereo depth camera, enabling it to create and navigate maps autonomously. Cloudy has been designed to be easily upgradeable and expandable, so you can continue to develop it to meet your needs.
# Networking Layer

One of the key features of a mobile robot is the ability to remotely monitor and control it. Cloudy can be controlled directly through the embedded system, and with the 2.4 GHz iBus receiver on board, you can start controlling the robot within 2 seconds without having to wait for your computer to boot up. An internet connection is required to connect to the Robolaunch platform and utilize the ROS platform. Cloudy uses a USB 5G WiFi connection.
# Power Distribution

The more features a robot has, the more cables it comes with, but there are various products available to simplify cable management. Cloudy has both direct battery voltage-powered components and regulated voltage-powered equipment on board. The design of Cloudy has been created to keep all these parts and cables neat and organized.
# Buttons & Switches

The battery cover of Cloudy is easily removable. To turn off the power of Cloudy, you can use the illuminated on/off button located on the back. In emergency situations, there is an emergency button to instantly cut off the power to the engines. Cloudy also includes a charging port for recharging and additional power output ports for connecting external equipment both inside and outside the device.
# Voltage Regulator

The voltage needs of the parts on the robot are different. There are 2 voltage regulators on Cloudy. One of them used only to power the computer. The 2nd bec is used to power the Esp32 and all other sensors and peripherals.

# Battery

"The power required for the operation of all systems on Cloudy is obtained from 18650 lion batteries in a 6s1p arrangement.The 3200mAh capacity of the battery allows Cloudy to run for a duration of over one hour. By modifying the battery cover to accommodate larger batteries, the operating time can potentially be extended to a maximum of 10 hours.
# Bill Of Materials List
| **Part Type**            | **Amount**             |   **Part Type**            | **Amount** |
|-|-|-|-|
| Raspberry Pi 4 8GB         | 1    |Nema 17 Stepper Motor | 2 |
| Orange Pi 5 16GB  | Optional                | 12V DC Motor With Encoder| Optional (2) |
| Jetson Nano | Optional                |DRV8825 Stepper Motor Controller | 2 |
| Wemos D1 R32         | 1                |MPU6050 IMU | 1 |
| Arduino Cnc Shield             | 1                |USB WIFI| 1 |
| Monster Moto Shield            | Optional                |IA6B Ibus Receiver| 1 |
| UBEC 5V 6A          |  1      |Intel Realsense D435i | 1 |
| Hobbywing 5V 3A Ubec         |  Optional      |RPlidar A1M8 Lidar | 1 |
| Apm Power Module         |  1      |Neopixel Led Stick 8x | 4 |
| 24V Cooling Fan        |  1      |Adafruit TCA9548A | 1 |
|6S 3200 mAh Li-on Battery Pack | 1 |Usb Micro Usb Cable 20cm | 1 |
|6S 2200 mAh Lipo Battery | Optional |Push button 12mm | 1 |
|Emergency Button 16mm | 1 |JST Connector Female | 7 |
|OLED I2C 0.96" Display | 1 | JST Connector Male | 7 |
| VL6180X TOF Distance Sensor | 3 |Splice Terminal | 16 |
|AS5600 encoder | 2 |Easy PDB Body 5 channel | 1 |
| Easy PDB connector | 5 |Xt30 Connector Pair| 1 | 

