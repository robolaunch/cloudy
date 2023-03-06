# Electronic Requriments

On Cloudy, you can easily integrate sensors using interfaces such as I2C, SPI, analog, and digital pins. The collected sensor data can then be converted into ROS2 topics via the microros platform. Sensors using the I2C interface have better cable tidiness and measurement quality. They also avoid problems caused by sensors with the same I2C addresses as the I2C multiplexer circuit.

## Overview
<img src="https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/cloudy-open-version.png">


Cloudy uses the esp32 micro controller on the embedded hardware side.

Cloudy robot has a Hardware Stack containing the main electronics and computer, all the parts here are cooled by a powerful fan. The Hardware Stack is easily separated from the body of the cloudy, which allows you to easily replace them and use them outside of the robot.

The first layer of the Hardware Stack contains an esp32 microcontroller. This board is known as uno esp32 and is compatible with most arduino uno shields.

The second layer contains shield for the motor drivers. Depending on your motor type (step, dc, brushless) you can choose different shield to the compatible driver board.this layer ensures the stable operation of the motor drivers.

On the top layer, there is a single board computer. Cloudy supports raspberry pi, orange pi 5, jetson nano and Intel Nuc computers. You can easily access the USBs on it and use add-ons such as stereo camera and lidar.

In addition, the body of the Cloudy is equipped with many sensors. These sensors work with i2c protocol and are connected with i2c multiplexer so you can connect multiple same sensors. 

The Cloudy robot comes equipped with three distance sensors, two of which are located within the bumper while the third is positioned at the bottom. Additionally, this device makes use of the same type of sensor technology found in the Samsung Galaxy S5 phone, which enables it to detect the direction of hand movements made on its surface. This innovative technology enables users to send commands to the Cloudy device using simple hand gestures, adding a new level of convenience and interactivity to the user experience.

 This sensors Also there are neopixel LEDs on all four sides, these LEDs are used for robot visibility and status indication. You can learn the battery voltage and status with the tiny oled screen at the top.
 <img width="300" height="300" style="margin-left:250px; margin-top:30px;" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cloudyvoltage.jpg">
<br/>
<br/><br/>
<br/>