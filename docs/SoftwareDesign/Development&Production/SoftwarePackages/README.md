## Software Packages

### robolaunch_cloudy_description

The [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package is one of the core packages of Cloudy. [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package includes URDF files describing Cloudy and sensors. Other packages uses [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package to describe a robot instance. 

Let's check the descriptions:
```bash
ros2 launch robolaunch_cloudy_description description.launch.py
```

The execution of the launch command initializes a [robot state publisher](http://wiki.ros.org/robot_state_publisher) node. This node reads the URDF packages specified in the launch file and publishes robot descriptions to the ROS2 network.


| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /robot_description  | std::Msg::String | Robot descriptions in XML format                     |


We can visualize the robot description using RViz.

![logo](https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cloudy_rviz.png)

### robolaunch_cloudy_hardware
The [robolaunch_cloudy_hardware](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_hardware) package creates a hardware interface to communicate with actuators. By design choice we decide to perform control calculations with ros2_control on Single Board Computer. Then the desired velocities gets forward to ESP32 over `left_motor_speed` and `right_motor_speed` topics. 

| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /left_motor_speed  | std::Msg::Float32 | Desired left motor speed in radians                  |
| /right_motor_speed | std::Msg::Float32 | Desired right motor speed in radians                 |

### robolaunch_cloudy_bringup
The [robolaunch_cloudy_bringup](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_bringup) package defines the [ros2_control](https://control.ros.org/master/index.html) parameters and spawns controllers&state publishers(using [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package). The controller nodes subscribe to the `/cmd_vel` topic, and to control the robot, one must publish a Twist type message to this topic. The configurations related to control can be modified in the /config/diffbot_diff_drive_controller.yaml file. 

| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /cmd_vel  | geometry::Msg::Twist | Velocity command in radians per second                     |

### robolaunch_cloudy_navigation & robolaunch_cloudy_simulator




#### Configuration

All config files are under `config` folder. There are five types of config files which are ekstended kalman filter, slam, navigation, laser filter, and mask filter.

---

#### EKF

<pre>
- arcelik_ekf.yaml : contains parameters for arcelik vehicle.
- sim_ekf.yaml     : contains parameters for simulation.
- ekf.yaml         : contains parameters for cloudy.
</pre>

| Parameter              |      Explanation            | 
|------------------------|:---------------------------|
| frequency              |  The frequency, in Hz, at which the filter  will output a position estimate.                       |
| two_d_mode (true/flase)|    ignores 3D information   |
| publish_tf (true/flase)| Publishes odom transform    |
| map_frame              | name of the map frame       |
| odom_frame             | name of the odom frame      |
| base_link_frame        | name of the base_link frame |
| world_frame            | name of the world frame     |


Give name to your sensor parameter and define what sensor datas are needed to be fused with EKF.

data_name: topic_name

data_name_config: 2D array of bool determinning wether or not to fuse sensor data like described below. Fusing datas which are derivative of each other is not recomended, see <a href="https://navigation.ros.org/setup_guides/odom/setup_odom.html">nav2 documentation</a> for detailed information. 

|       X         |        Y        |        Z       | 
|-----------------|-----------------|----------------|
| x position      |  y position     |  z position    |
| roll position   |  pitch position |  yaw position  |
| x velocity      |  y velocity     |  z velocity    |
| roll velocity   |  pitch velocity |  yaw velocity  |
| x acceleration  |  y acceleration |  z acceleration|

---

#### Laser Filter

<pre>
- box_filter.yaml   : filters laser range data in a rectangle.
- range_filter.yaml : filters laser range outside a given interval.
</pre>

**Box Filter**

| Parameter |      Explanation                       | 
|-----------|:---------------------------------------|
| type      | laser_filters/LaserScanBoxFilter       |
| name      | name of the filter                     |
| box_frame | frame name                             |
| max_x     | front of the rectangle                 |
| max_y     | left side of the rectangle             |
| max_z     | top of the rectangle                   |
| min_x     | (negative) back of the rectangle       |
| min_y     | (negative) right side of the rectangle |
| min_z     | (negative) bottom of the rectangle     |



**Range Filter**

| Parameter                |      Explanation                           | 
|--------------------------|:-------------------------------------------|
| name:                    | name of the filter                         |
| type:                    | laser_filters/LaserScanRangeFilter         |
| lower_threshold          | ignores shorter laser ranges (in meters)   |
| upper_threshold          | ignores longer laser ranges (in meters)    |
| lower_replacement_value  | (.inf / -.inf) replacement for short ranges|
| upper_replacement_value  | (.inf / -.inf) replacement for long ranges |

---

#### SLAM

<pre>
- sim_slam.yaml: parameters for SLAM in simulation.
- sim_slam.yaml: parameters for SLAM in physical world.
</pre>

Important `SLAM Toolbox` parameters. See <a href="https://github.com/SteveMacenski/slam_toolbox">slam toolbox github</a> for more detailed information.

| Parameter                |      Explanation                           | 
|--------------------------|:-------------------------------------------|
| scan_topic               | name of the laser scan topic
| mode                     | (mapping/localization) set to localization if no addition to map will be made|
| map_file_name            | map file path without file extension        |
| map_start_pose           | starting position with respect to map origin|
| map_start_at_dock        | (true/false) start at the pose where you started mapping.|
| debug_logging            | (true/false) set to false while not debugging to prevent abundant logs |
| map_update_interval      | period of map updating in second            |
| max_laser_range          | max laser range to be considered in mapping and localization|

---

#### Keepout Filter

<pre>
- map_filter.yaml: parameters for navigation with keepout zones
</pre>

If there are restricted areas on the map that the robot should not enter, keepout zones should be used. Parameters to be set are explained in the tabel below. See <a href="https://navigation.ros.org/tutorials/docs/navigation2_with_keepout_filter.html">nav2 documentation</a> for more detailed explanation.

| Parameter |      Explanation                       | 
|-----------|:---------------------------------------|
| type      | for Keepout Filter the type of costmap filter should be set to 0|
| name      | name of the filter                     |
| box_frame |    frame name                          |
| max_x     | front of the rectangle                 |
| max_y     | left side of the rectangle             |
| max_z     | top of the rectangle                   |
| min_x     | (negative) back of the rectangle       |
| min_y     | (negative) right side of the rectangle |
| min_z     | (negative) bottom of the rectangle     |

---

#### Navigation

<pre>
- sim_navigation.yaml: parameters for navigation in simulation.
- navigation.yaml    : parameters for navigation in physical world.
</pre>

- For behaviour threes see <a href="https://navigation.ros.org/behavior_trees/index.html">nav2 documentation</a>

**AMCL**

| Parameter       |      Explanation                       | 
|-----------------|:---------------------------------------|
| robot_model_type| (holonomic / differential-drive / legged / ackermann) `holonomic`: can go every direction, `differential-drive`: turns with speed difference in wheels, `ackerman`: car-like|
| scan_topic      | name of the laser scan topic           |

**Controller Server**

| Parameter                    |      Explanation                         | 
|------------------------------|:-----------------------------------------|
| controller_frequency:        |frequency of the control loop in Hz       |
| min_x_velocity_threshold:    |min velocity in x direction (front +)     |
| min_y_velocity_threshold     |min velocity in y direction (left +)      |
| min_theta_velocity_threshold |min angular velocity (counter clockwise +)|
| failure_tolerance            |amount of toleratable error in meters     |
| progress_checker_plugin      | <a href="https://navigation.ros.org/plugins/index.html#progress-checkers">progress checker plugin list</a> |
| goal_checker_plugins         |<a href="https://navigation.ros.org/plugins/index.html#goal-checkers">goal checker plugin list</a> |
| controller_plugins           |<a href="https://navigation.ros.org/plugins/index.html#controllers">controller plugin list</a> |

**General Goal Checker**

| Parameter          |      Explanation                                     | 
|--------------------|:-----------------------------------------------------|
| plugin:            |<a href="https://navigation.ros.org/plugins/index.html#goal-checkers">goal checker plugin list</a>|
| xy_goal_tolerance: |error in meters on xy plane to check the goal reached |
| yaw_goal_tolerance |error in radian on yaw angle to check the goal reached|

**Follow Path**

| Parameter      |      Explanation                 | 
|----------------|:---------------------------------|
| min_vel_x      |min velocity in x direction       |
| min_vel_y      |min velocity in y direction       |
| max_vel_x      |max velocity in x direction       |
| max_vel_y      |max velocity in y direction       |
| max_vel_theta  |max velocity in yaw angle         |
| min_speed_xy   |min velocity in xy plane          |
| max_speed_xy   |max velocity in xy plane          |
| min_speed_theta|min velocity in yaw angle         |
| acc_lim_x      |acceleration limit in x direction |
| acc_lim_y      |acceleration limit in y direction |
| acc_lim_theta  |decceleration limit in yaw angle  |
| decel_lim_x    |decceleration limit in x direction|
| decel_lim_y    |decceleration limit in y direction|
| decel_lim_theta|decceleration limit in yaw angle  |

**Costmap**

| Parameter|      Explanation                               | 
|----------|:-----------------------------------------------|
| plugin   |<a href="https://navigation.ros.org/plugins/index.html#costmap-layers">costmap layer plugin list</a>          |
| filters  |`keepout_filter` if map mask is going to be used|


**Keepout Filter**

| Parameter         |      Explanation                       | 
|-------------------|:---------------------------------------|
| plugin:           |`nav2_costmap_2d::KeepoutFilter`        |
| enabled           |(true / false)                          |
| filter_info_topic |topic name for map filter info          |

**Inflation Layer**

| Parameter        |      Explanation                       | 
|------------------|:---------------------------------------|
| plugin:          |<a href="https://navigation.ros.org/plugins/index.html#progress-checkers">costmap layer plugin list</a> |
| inflation_radius |distance in meters to avoid obstacles   |

**Voxel2D Layer**

| Parameter |      Explanation                       | 
|-----------|:---------------------------------------|
| plugin    |<a href="https://navigation.ros.org/plugins/index.html#progress-checkers">costmap layer plugin list</a>|
| enabled   |(true / false)                          |

**Planner Server**

| Parameter                     |      Explanation                       | 
|-------------------------------|:---------------------------------------|
| expected_planner_frequency    |planning frequency in Hz|
| use_final_approach_orientation|(true / false) goal poses have orientation data, to ignore orientation set to true|
| allow_unknown                 |(true / false) allows making road plans from unknown reagions of the map|
| use_astar                     |(true / false) defaul shortest path algorithm is dijkstar, to use A* set to true|
| plugin                        |<a href="https://navigation.ros.org/plugins/index.html#planners">planner plugin list</a> |

If the desired path is always linear straigh line planner can be used with following parameters; however it is experimental. It does not avoid collision and it is not stable. To use it checkout to the experimental branch.

<pre>
planner_server:
  ros__parameters:
    plugins: ["GridBased"]
    use_sim_time: True
    GridBased:
      plugin: nav2_straightline_planner/StraightLine
      interpolation_resolution: 0.1
      current_goal_checker: "nav2_controller::SimpleGoalChecker"
</pre>

### rf2o_laser_odometry
Description from the public [rf2o_laser_odometry](https://github.com/MAPIRlab/rf2o_laser_odometry) repository:

>Estimation of 2D odometry based on planar laser scans. Useful for mobile robots with innacurate base odometry.
>
>RF2O is a fast and precise method to estimate the planar motion of a lidar from consecutive range scans. For every scanned point we formulate the range flow constraint equation in terms of the sensor velocity, and minimize a robust function of the resulting geometric constraints to obtain the motion estimate. Conversely to traditional approaches, this method does not search for correspondences but performs dense scan alignment based on the scan gradients, in the fashion of dense 3D visual odometry.
>
>Its very low computational cost (0.9 milliseconds on a single CPU core) together whit its high precission, makes RF2O a suitable method for those robotic applications that require planar odometry.
>
>For full description of the algorithm, please refer to: Planar Odometry from a Radial Laser Scanner. A Range Flow-based Approach. ICRA 2016 Available at: http://mapir.isa.uma.es/work/rf2o

?>We are utilizing Humble version of the [repository](https://github.com/MAPIRlab/rf2o_laser_odometry/pull/34) ported by one of our developers.

### sllidar_ros2

_RPLidar_ ROS2 wrapper [package](https://github.com/Slamtec/sllidar_ros2). 

Example command to launch the RPLidar A1: 
```bash
ros2 launch sllidar_ros2 view_sllidar_launch.py
```

?>We are utilizing Humble version of the [package](https://github.com/Slamtec/sllidar_ros2/pull/15).