![](https://automaticaddison.com/wp-content/uploads/2021/09/4-launch-basic-mobile-robot-v5-2.jpg)

## Navigation

One of the big tasks of Cloudy agv is indoor delivery and it comes with 2 navigation features to serve this purpose. If you wish, you can make the vehicle go there by giving a target on the map obtained as a result of the slam operation, or you can navigate the predetermined coordinates with the `waypoints_commander` script.





    source install/setup.bash \
    ros2 launch robolaunch_cloudy_navigation cloudy_nav.launch.py

## Config

All config files are under config folder. There are five types of config files which are ekstended kalman filter, slam, navigation, laser filter, and mask filter.
Navigation Parameters are in navigation.yaml file.

https://github.com/robolaunch/cloudy/blob/main/robolaunch_cloudy_navigation/config/navigation.yaml
