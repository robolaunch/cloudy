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

## Config

All config files are under config folder. There are five types of config files which are ekstended kalman filter, slam, navigation, laser filter, and mask filter.
Slam Parameters are in slam.yaml file.

https://github.com/robolaunch/cloudy/blob/main/robolaunch_cloudy_navigation/config/slam.yaml
