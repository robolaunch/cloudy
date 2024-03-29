![](https://raw.githubusercontent.com/robolaunch/trademark/main/repository-media/cloudy/images/ros2_control.png)

https://control.ros.org/master/doc/ros2_controllers/diff_drive_controller/doc/userdoc.html

Ros2 control software supports many types of robots. Cloudy Mini-AGV robot uses the **diffbot** control method from these robot types. It launches as shown below. </br>

        ros2 launch robolaunch_cloudy_bringup diffbot_system.launch.py

After launching, the /cmd_vel topic will be opened and you will be able to control the robot via microros with the twist type message you will send over this topic. At the same time, a Cloudy Mini-AGV model will be started on rviz2 and you will be able to observe the movements from there. The diffbot_control package under Ros2 control will calculate the speed that should go to the motors depending on the speed sent from the ```/cmd_vel``` topic and publish it to the 
```/left_motor_speed``` and ```/right_motor_speed``` topic.

You can use the ros keyboard control function below to simply drive the robot.

        ros2 run teleop_twist_keyboard teleop_twist_keyboard

    
