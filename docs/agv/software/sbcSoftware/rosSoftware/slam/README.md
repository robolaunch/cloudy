![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/rviz_slam.png)

## Slam

Launch `SLAM` for desired vehicle. If Arcelik vehicle is being used, lauch `arcelik_slam.launch.py`. If cloudy_v1 or cloudy_v2 is being used, launch `cloudy_slam.launch.py`. They launch the proper nodes for lidar sensor, laser odometry, ekstended kalman filter for sensor fusion, low level controller enabling `cmd_vel` topic, and laser filter to prevent lidar from seing the robot as obstacle. To launch SLAM with rviz set rviz parameter true by `rviz:=true`.

    source install/setup.bash
    ros2 launch robolaunch_cloudy_navigation cloudy_slam.launch.py


## Localization

Lidar and imu are used for localization, data from two places are combined with ekf, so that the positioning of the robot is not dependent on a single sensor. Improvements can be made by changing these settings.

    cd ~/imu && \
    . install/setup.bash && \
    ros2 launch mpu6050driver mpu6050driver_launch.py

## EKF
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


## Config

All config files are under config folder. There are five types of config files which are ekstended kalman filter, slam, navigation, laser filter, and mask filter.</br>
https://github.com/robolaunch/cloudy/blob/main/robolaunch_cloudy_navigation/config/

- slam.yaml         : contains parameters for cloudy agv.
- arcelik_slam.yaml : contains parameters for arcelik vehicle.
- sim_slam.yaml     : contains parameters for simulation.

