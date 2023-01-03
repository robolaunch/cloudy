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
      <img src="https://img.shields.io/github/issues/robolaunch/cloudy" alt="issues">
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

If you do not currently have access to a physical Cloudy robot, you can use the Gazebo simulation for experimentation. 
\
To clone the Cloudy repository, you will need to have Git and ROS installed on your system. You can check offical guide for installing <a href="https://github.com/git-guides/install-git">Git</a> and <a href="https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html">ROS</a>. Once both are installed, you can use the following commands to clone the repository:
\
\
Create a new workspace
\
```mkdir cloudy_ws/src -p && cd cloudy_ws/src```
\
\
Clone the repository
\
```git clone https://github.com/robolaunch/cloudy.git && cd ..```
\
\
Source ROS installation
\
```source /opt/ros/$ROS_DISTRO/setup.bash```
\
\
Install dependencies
\
```sudo rosdep init && rosdep update && rosdep install --from-paths src --ignore-src -y ```
\
\
Build the repository
\
```colcon build && source install/setup.bash```
\
\
Launch the simulation
\
```ros2 launch robolaunch_cloudy_simulator launch_sim.launch.py```
\
\
Control the robot
\
- In a separate terminal, source the ROS installation and run teleop node
\
```ros2 run teleop_twist_keyboard teleop_twist_keyboard```
\
\




- Create first release to stage new features
- Add custom workflows for CI/CD
- Specialize issue & PR templates if needed

## Aims & Roadmap

[EDIT THIS: Add roadmap items for the project.]

- Extending the open source conventions
- Enforcing conventional commit messages

## Contributing

Please see [this guide](./CONTRIBUTING) if you want to contribute.
