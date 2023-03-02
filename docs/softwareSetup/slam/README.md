# Slam and Localizations
![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/rviz_slam.png)

The cloudy robot has a lidar, the lidar scan position is between the chassis and the upper platform, the lidar broadcasts the raw data to the  ```/scan ``` subject. We turn the raw lidar data into a  ```/scan_filtered ``` topic so that the arms are not visible on the 4 sides of the upper platform.

