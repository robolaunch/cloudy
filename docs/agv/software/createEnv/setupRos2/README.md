# Setup ROS 2
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
