## Micro-ROS Agent

* Follow the steps below to install the micro ros agent</br>.
* Clone the updated repository to SBC from [**here**](https://github.com/micro-ROS/micro_ros_setup</br>).
* Build the micro_ros_setup and open src directory on terminal.</br>

        sudo apt install python3-rosdep
        ros2 run micro_ros_setup create_agent_ws.sh
        ros2 run micro_ros_setup build_agent.sh
        source install/local_setup.sh

* Connect Esp32 to SBC via Usb cable.
* To find out which tty port of esp32 is, run the command below. The serial code of Esp32 is always CH341 and the port number is written next to it. example (dev/tty1)
        sudo dmesg | grep USB
* Check the tty port and run this ros command to start the connect.
        ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB1
* Press the Reset Button on top of the Cloudy Mini-AGV, this equals to reset esp32

You can see the avaible topics with that command below 
        
        ros2 topic list
