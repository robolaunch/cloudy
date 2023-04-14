## **ROS Packages**

## robolaunch_cloudy_description

The [**robolaunch_cloudy_description**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package is one of the core packages of Cloudy. 
[**robolaunch_cloudy_description**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package includes URDF files describing Cloudy and sensors. Other packages uses [**robolaunch_cloudy_description**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package to describe a robot instance. 

Let's check the descriptions:
```bash
ros2 launch robolaunch_cloudy_description description.launch.py
```

The execution of the launch command initializes a [**robot state publisher**](http://wiki.ros.org/robot_state_publisher) node. This node reads the URDF packages specified in the launch file and publishes robot descriptions to the ROS2 network.


| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /robot_description  | std::Msg::String | Robot descriptions in XML format                     |


We can visualize the robot description using RViz.

![logo](https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cloudy_rviz.png)

## robolaunch_cloudy_hardware
<img style="display:block; margin:auto;" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/microros_scheme.png"/>

The [robolaunch_cloudy_hardware](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_hardware) package creates a hardware interface to communicate with actuators. By design choice we decide to perform control calculations with ros2_control on Single Board Computer. Then the desired velocities gets forward to ESP32 over `left_motor_speed` and `right_motor_speed` topics. 
You can follow the <a>Micro Ros Agent</a> and <a>Micro ROS</a> page for more.

| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /left_motor_speed  | std::Msg::Float32 | Desired left motor speed in radians                  |
| /right_motor_speed | std::Msg::Float32 | Desired right motor speed in radians                 |

## robolaunch_cloudy_bringup
The [**robolaunch_cloudy_bringup**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_bringup) package defines the [**ros2_control**](https://control.ros.org/master/index.html) parameters and spawns controllers&state publishers(using [**robolaunch_cloudy_description**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package). The controller nodes subscribe to the `/cmd_vel` topic, and to control the robot, one must publish a Twist type message to this topic. The configurations related to control can be modified in the /config/diffbot_diff_drive_controller.yaml file. 
You can follow the <a>Ros2 Control & Teleoperation</a> page for its launch bringup.

| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /cmd_vel  | geometry::Msg::Twist | Velocity command in radians per second                     |

## robolaunch_cloudy_navigation
The [**robolaunch_cloudy_navigation**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_navigation) packages includes the navigation plugin developed with nav2. Cloudy robot also added waypoint follower feature. 
You can follow the <a>navigation</a> page for its launch navigation.

## robolaunch_cloudy_simulation
The [**robolaunch_cloudy_simulation**](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_simulator) packages includes all the features of the Cloudy such as teleoperation, slam and navigation. </br>
You can follow the <a>simulation</a> page for its launch simulation.

## Lidar Package
_RPLidar_ ROS2 wrapper [**package**](https://github.com/Slamtec/sllidar_ros2). 

Example command to launch the RPLidar A1: 
```bash
ros2 launch sllidar_ros2 view_sllidar_launch.py
```

?>We are utilizing Humble version of the [**package**](https://github.com/Slamtec/sllidar_ros2/pull/15).

## Stereo Camera Package 
Intel Realsense D435i [**package**](https://github.com/IntelRealSense/realsense-ros).

Example command to launch the Intel Realsense D435i: 
```bash
ros2 launch realsense2_camera rs_launch.py
```
## Lidar Scan Filtered
Universal Lidar Scan Filtered [**package**](https://github.com/ros-perception/laser_filters).

The cloudy robot has a lidar, the lidar scan position is between the chassis and the upper platform, the lidar broadcasts the raw data to the  ```/scan ``` subject. We turn the raw lidar data into a  ```/scan_filtered ``` topic so that the arms are not visible on the 4 sides of the upper platform.

```bash
ros2 launch laser_filters box_filter.launch.py
```
