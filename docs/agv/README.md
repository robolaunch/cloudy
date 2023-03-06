# Robolaunch Cloudy Home

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/CLOUDY%20MK2%20(5).png" width="400" height="295" align="right">

## Robolaunch Cloudy AGV
Cloudy is a fully 3d printable, open-source and autonomous robotics learning and development platform based on ROS framework, allowing users to fully customize and modify the platform for their own educational purposes. And it fits in to your backpack.

## Overview

### Source code

?> **check the repository from the [Github](https://github.com/robolaunch/cloudy).**

Why is Cloudy open source?

- Easily produced by generic 3d printers to be accessible to everyone in the world.
- Better performing AI, CPU heavy operations with native cloud integration with Robolauch (optional).
- Electronic hardware is fully customizable for unlimited applications without vendor dependency.
- Customizable mechanical parts to integrate different sensors without expensive impractical equipment.
- Focus on your specific needs, such as software design, with an inexpensive production quality platform
- For your next autonomy operation, payload delivery or any other fun software project feel free to join community. Create and issue, give feed back.
- Cloudy is available in both assembled and unassembled form, either as a fully-assembled product with different options or as a DIY kit. Both accessible from our store.

### Chassis and drivetrain


The Cloudy features a differential drive control system with four preloaded caster wheels for weight support and smooth operation. It is designed for indoor flat surfaces and has a payload capacity of 20 kilograms.
<br>

![](https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20dimensions%201.png)



### Embedded Hardware
The Cloudy is equipped with an embedded system that serves as the central control unit for all sensors and motors. The embedded system supports various software controllers, including ROS, ROS2, Ardupilot, and PX4. Cloudy utilizes the ROS2 platform and employs an ESP32 microcontroller due to its micro-ROS support. The ESP32 Arduino UNO version was selected for its compactness and compatibility with UNO shields, allowing for easy integration of additional hardware components.
### Single Board Computer
 In order to utilize the ROS and roslaunch platform, a Linux-based operating system is necessary. The Cloudy's body has ample room to accommodate these computers. In this particular design, a Raspberry Pi 4 with 8GB of RAM has been chosen as the computing solution.
### Cloud Based
Powered by robolaunch platform

- Transfer your sensor data into cloud, process sensor data real-time in heavy AI applications using the best GPUs available and reflect the results to the robot!
- Gazebo/Rviz/Isaac Sim(optional)/MuJoCo simulation over cloud VDI for virtual development purposes. 
- Access Cloudy development environment with a cloud IDE in just minutes and start developing your algorithms on a cloud VDI.
- Utilize NVIDIA powered Isaac ROS packages on cloud GPUs and run AI applications on Cloudy!
- 5G Robot control remotely.


### Customisable Add-Ons
By incorporating hardware accessories, you can expand the functionality of your robot. A Thermal camera can detect any heat anomalies, while the 360 camera provides situational awareness. Cloudy comes equipped with a Rplidar A1M8 lidar model and an intel realsense d435i stereo depth camera, enabling it to create and navigate maps autonomously. 

Cloudy has been designed to be easily upgradeable and expandable, so you can continue to develop it to meet your needs.

### Dimensions

## Video

<iframe  height=600 width=800 src="https://www.youtube.com/watch?v=I4ivsS-1b_o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



**Powered by**

![logo](https://micro.ros.org/img/micro-ROS_big_logo.png ':size=20%')
![logo](https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/01-nvidia-logo-horiz-500x200-2c50-d.png ':size=15%')
![logo](https://navigation.ros.org/_static/nav2_logo.png ':size=5%')
![logo](https://avatars.githubusercontent.com/u/3979232?s=280&v=4 ':size=10%')
![logo](https://gazebosim.org/assets/images/logos/gazebo_horz_pos.png ':size=15%')
![logo](https://control.ros.org/master/_static/logo_ros-controls.png ':size=7%')