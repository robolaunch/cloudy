## **Setup With SD Card**

<img style="width:50%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/rpimager.jpg"/>

You can follow the [official Ubuntu installation guide](https://releases.ubuntu.com/22.04/) for setting up the operating system.
Cloudy is also tested on [RaspberryPi 4 (8 GB)](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/). You can install your preference of choice version(desktop/server) of Ubuntu 22.04 to RaspberryPi 4. 

* Download ubuntu 22.04 image for selected SBC
* Write the image to sd card with <a href="https://win32diskimager.org/">win32 disk imager</a> or <a href="https://www.balena.io/etcher">balena etcher</a>.
* Install ROS2 Humble from <a href="https://docs.ros.org/en/humble/index.html">ROS Documentation</a>.
* Clone the cloudy robot repository to SBC from https://github.com/robolaunch/cloudy
* Clone the micro ros setup to SBC from https://github.com/micro-ROS/micro_ros_setup


?> If you prefer to install server version of Ubuntu, you need to [**configure network settings**](https://linuxhint.com/ubuntu-22-04-network-configuration/) and [**enable ssh communication**](https://linuxhint.com/enable-use-ssh-ubuntu/) to connect to the robot.

