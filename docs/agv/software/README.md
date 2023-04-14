

## Software
<style>
a:link { text-decoration: none; }
a:visited { text-decoration: none; }
a:hover { text-decoration: none; }
a:active { text-decoration: none; }
</style>
1. [**Embedded Software:**](/agv/software/embedded/) 
Cloudy Mini-AGV uses a microcontroller for motor driving, sensors and electronics supply. It transmits the data it receives and needs to send to the computer with the micro-ros protocol.

2. [**SBC (Single Board Computer) Software:**](/agv/software/sbcSoftware/)
Cloudy Mini-AGV robot is a ros2 robot and it needs a simple computer. When the computer power is insufficient, you can limit your robot's power by connecting it to the robolaunch cloud platform.
3. [**Simulation:**](/agv/software/simulation/)
You don't need to have one of them to use Cloudy Mini-AGV. You can perform operations such as teleoperation, slam, nav, waypoint follower via gazebo and rviz2.

## High Level Software Architecture
Here is a high level architecture diagram of the Cloudy Mini-AGV software. 

<img src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/software_block_diagram.png?raw=true">

## Low Level Software Architecture
Here is a detailed architecture diagram of the Cloudy Mini-AGV software. 

<img src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/DetailedSoftwareDiagram.drawio.png?raw=true">
