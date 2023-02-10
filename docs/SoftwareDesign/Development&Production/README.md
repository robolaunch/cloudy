## Overview

In this chapter, we will delve into the specifics of developing and producing the Cloudy software. From setting up the necessary development environments to understanding the software architecture and packages, this section will provide an in-depth look at the technical aspects of the Cloudy software. We will also cover topics such as setting up ROS2, integrating the software with [**robolaunch cloud services**](https://www.robolaunch.cloud), embedded systems, and interfaces. Finally, we will provide troubleshooting tips to help you resolve any issues that may arise during the development process. Whether you're a seasoned developer or just getting started, this chapter is designed to provide you with the information you need to develop and produce the Cloudy software with confidence.

## Environments & Setup

Cloudy's software stack is developed and tested on the systems below:

| Operating System    | ROS2 version |
|---------------------|--------------|
| Ubuntu 22.04(arm64) | Humble Hawksbill|
| Ubuntu 22.04(amd64) | Humble Hawksbill|


### Single Board Computer Setup
You can follow the [official Ubuntu installation guide](https://releases.ubuntu.com/22.04/) for setting up the operating system.
Cloudy is also tested on [RaspberryPi 4 (8 GB)](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/). You can install your preference of choice version(desktop/server) of Ubuntu 22.04 to RaspberryPi 4. 

?> If you prefer to install server version of Ubuntu, you need to [**configure network settings**](https://linuxhint.com/ubuntu-22-04-network-configuration/) and [**enable ssh communication**](https://linuxhint.com/enable-use-ssh-ubuntu/) to connect to the robot.

### Set up git

For the development of the Cloudy software, we utilize the git versioning system. To access the software packages, it is necessary to first download git, then clone the repository. If you are new to git, we suggest following the [w3schools tutorials](https://www.w3schools.com/git/).

Let's install git:

```bash
sudo apt install git
```

Configure with your credentials: 
```bash
git config --global user.name "your_user_name"
git config --global user.email "your_email"
```

### Set up ROS2
The current stable version of ROS2 is called Humble Hawksbill. Debian packages for Humble Hawksbill are available for Ubuntu Jammy, and we suggest following the [**official tutorials**](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) for setting up ROS2. For those who are new to the Robot Operating System, it is advisable to first complete [**beginner tutorials**](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools.html) to gain a solid understanding of ROS2 before proceeding.

!> **IMPORTANT** \
You have to source the ROS2 installation in same the terminal in order to use ROS2 commands. ```source /opt/ros/humble/setup.bash ```


To verify ROS2 installation use the following command:
```bash
ros2 topic list 
``` 

You should see those two topics listed: 
```bash
/parameter_events
/rosout
```

## [Software Packages](/SoftwareDesign/Development%26Production/SoftwarePackages/)

We have to initialize the workspace we are going to work on. Let's get started.

- Create a new workspace:

```bash
mkdir cloudy_ws/src -p && cd cloudy_ws/
```
- Clone the repository

```bash
git clone https://github.com/robolaunch/cloudy.git src
```

- Init rosdep if you have not already

```bash
sudo rosdep init
```

- Install dependencies

```bash
sudo rosdep update && rosdep install --from-paths src --ignore-src -y
```

- Source your ROS distribution

```bash
source  /opt/ros/$ROS_DISTRO/setup.bash
```

- Build the repository

```bash
colcon build && source install/setup.bash
```

We have prepared the ROS2 workspace. There are several software packages in Cloudy Software stack. 
For detailed explanation please check [**Software Packages**](/SoftwareDesign/Development%26Production/SoftwarePackages/) page.




### Software Architecture

#### High level
Here is a high level architecture diagram of the Cloudy software. You can access and modify the block diagram from the [link](https://whimsical.com/LxtNBwNDTjNXYP3EHM6uqS)! 
<img style="background-color:white!important" src="../../images/software_block_diagram.png" alt="detailedsoftwareblockdiagram">

#### Low level
Here is a detailed architecture diagram of the Cloudy software. You can access and modify the detailed diagram from the [link](https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/DetailedSoftwareDiagram.drawio)! 
<img style="background-color:white!important" src="../../images/DetailedSoftwareDiagram.drawio.png" alt="detailedsoftwareblockdiagram">

## Cloud Integration
## Embedded Integration
### micro-ROS agent

## Interfaces and Integration
## Troubleshoot and Tips