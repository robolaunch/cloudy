# <img src="https://raw.githubusercontent.com/robolaunch/trademark/main/logos/svg/rocket.svg" width="40" height="40" align="top"> robolaunch Cloudy
<p align="center">
<img src="https://github.com/robolaunch/cloudy/blob/main/docs/cloudy-v2.png" width="500">
</p>

<div align="center">
  <p align="center">
  <a href="https://github.com/robolaunch/cloudy/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/robolaunch/cloudy?color=brightgreen"/></a>
    <a href="https://github.com/robolaunch/cloudy/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/robolaunch/cloudy" alt="license">
    </a>
    <a href="https://github.com/robolaunch/cloudy/issues">
      <img src="https://img.shields.io/github/issues/robolaunch/cloudy?color=brightgreen" alt="issues">
    </a>
  <a href="https://github.com/robolaunch/cloudy/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/robolaunch/cloudy" /></a>
  </p>
</div>

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Contributing](#contributing)


## Overview

Cloudy is an open-source, 3D-printed robot designed and built by Robolaunch. With its advanced capabilities and innovative design, Cloudy is poised to become a key player in the world of robotics. Whether you're a seasoned DIY enthusiast or just getting started in the world of robotics, Cloudy has something to offer.

- Explore the world of robotics and learn about the latest technology and techniques
- Build, customize, and program your own robot using open-source software and hardware
- Experiment with sensors, motors, and other components to see what Cloudy can do
- Share your creations and collaborate with others in the ROS community


## Quick Start
\
**Simulation**
\
\
If you do not currently have access to a physical Cloudy robot, you can use the Gazebo simulation for experimentation. 
\
To clone the Cloudy repository, you will need to have Git and ROS installed on your system. You can check offical guide for installing <a href="https://github.com/git-guides/install-git">Git</a> and <a href="https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html">ROS</a>. Once both are installed, you can use the following commands to clone the repository:

- Create a new workspace

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

- Build the repository

```bash
colcon build && source install/setup.bash
```

- Launch the simulation

```bash
ros2 launch robolaunch_cloudy_simulator launch_sim.launch.py
```

- Control the robot

In a separate terminal, source the ROS installation and run teleop node

```bash
source /opt/ros/$ROS_DISTRO/setup.bash && ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

\
**Real Robot**
\
\
If you have access to a physical Cloudy robot, you have to install the firmware to the ESP32 and ROS packages to the internal board computer. Follow the simulation installation for building the Cloudy workspace.
\
Install firmware code to the ESP32

- Install Arduino IDE 2.0 from <a href="https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing">official website</a>
- Open Arduino IDE->Boards Manager, find esp32 by Espressif Systems, install **(version 2.0.2)**.
- Check the available micro-ros-arduino library from the [official releases](https://github.com/micro-ROS/micro_ros_arduino/releases). Download zip library, go to Arduino IDE -> Sketch -> Include Library -> Add .ZIP library and choose the downloaded library
- Choose the board from Tools -> Board -> esp32 -> DOIT ESP32 DEVKIT V1
- Open library manager, install FastAccelStepper **(version 0.28.3)**
- Open the firmware file from File -> Open and choose cloudy_ws/robolaunch_cloudy_hardware/firmware/firmware.ino
- Choose the correct port from Tools -> Port (/dev/ttyUSB0 in an example case)
- Upload the file to the ESP32

\
Install micro-ROS and ROS2 packages to the internal computer

- micro-ROS tools installation
```bash
# Source the ROS 2 installation
source /opt/ros/$ROS_DISTRO/setup.bash

# Go to Cloudy workspace and download the micro-ROS tools
cd cloudy_ws
git clone -b $ROS_DISTRO https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup

# Update dependencies using rosdep
sudo apt update && rosdep update
rosdep install --from-paths src --ignore-src -y

# Install pip
sudo apt-get install python3-pip

# Build micro-ROS tools and source them
colcon build
source install/local_setup.bash
```
- Create and build micro-ROS agent

```bash
ros2 run micro_ros_setup create_agent_ws.sh
```
```bash
ros2 run micro_ros_setup build_agent.sh
```
```bash
source install/local_setup.bash
```
```bash
ros2 run micro_ros_agent micro_ros_agent serial --dev [device] #(device is the same with port you've choosen in the previous step, ex. /dev/ttyUSB0)
```
Note: If the agent is not active you can try pushing the boot button on the ESP32.


 - Launch Cloudy nodes

Launch the nodes, in a new terminal:
```bash
source install/setup.bash && ros2 launch robolaunch_cloudy_bringup diffbot_system.launch.py
```
- Controlling the robot

Use the teleop keyboard, in a new terminal : 
```bash
source install/setup.bash && ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=diffbot_base_controller/cmd_vel_unstamped
```

## Community
- [Website](https://www.robolaunch.io/)
- [LinkedIn](https://www.linkedin.com/company/robolaunch)
- [Twitter](https://twitter.com/robolaunch)
- [Slack]() - *soon*
- [Discord]() - *soon*
- [robolaunch Forum]() - *soon*

## Contributing

Please see [this guide](./CONTRIBUTING.md) if you want to contribute.


