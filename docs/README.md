# <img src="./robolaunch Yatay Logo - Black (1).png" height="75px" > 
# robolaunch Cloudy Manual

<p>
Welcome to the technical documentation of robolaunch Cloudy.
</p>

<iframe  height=600 src="https://www.youtube.com/embed/7wn2tVbTrz8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


# Overview


<p align="center">
<img src="https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/cloudy-v2.png" alt="Cloudy" >
</p>



Cloudy is an open-source, 3D-printed robot designed and built by Robolaunch. Whether you're a seasoned DIY enthusiast, robotics professional or just getting started in the world of robotics, Cloudy has something to offer for you. 


- Powered by robolaunch platform:
    - Transfer your sensor data into cloud, process sensor data real-time in heavy AI applications using the best GPUs available and reflect the results to the robot!
    - Gazebo/Rviz/Isaac Sim(optional)/MuJoCo simulation over cloud VDI for virtual development purposes. 
    - Access Cloudy development environment with a cloud IDE in just minutes and start developing your algorithms on a cloud VDI.
    - Utilize NVIDIA powered Isaac ROS packages on cloud GPUs and run AI applications on Cloudy!<img src="https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/01-nvidia-logo-horiz-500x200-2c50-d.png" alt="nvidia" height="80px" >
    - 5G Robot control remotely.(If available) 
- State of the art autonomous navigation stack (ROS2 Nav2).<img src="https://navigation.ros.org/_static/nav2_logo.png" alt="nav2" height="80px" >
    - Waypoint follower
    - Obstacle avoidance
    - Flexible algorithm selection and various plugins based on different use cases.
- Simultaneous localization and mapping(SLAM) using LIDAR, IMU and motor encoders.
- Flexible and modifiable ros2_control algorithm. <p>
<img src="https://control.ros.org/master/_static/logo_ros-controls.png" alt="roscontrol" height="40px" >
</p>
- Powered by micro-ROS, start developing your embedded software on ESP32 
and connect them into ROS environment! 
<p>
<img src="https://micro.ros.org/img/micro-ROS_big_logo.png" alt="microros" height="40px" >
</p>
- Light enough to be carried in a backpack! (~3 kg)
- Strong enough to lift 20 kg payload!




<button name="button" onclick="window.open('https://github.com/robolaunch/cloudy','_blank')">Go to Github</button>

# Manufacturing Guide

Welcome to the manufacturing guide for Cloudy, if you purchased the Cloudy then you can skip this part and jump into [Quick Start](?id=quick-start). In this guide, you are going to find out how to manufacture and assemble mechanical parts of Cloudy. 

As a starting point, you have to 3D print the mechanical parts of the Cloudy. STL files of Cloudy can be downloaded from the official Github <a href="https://github.com/robolaunch/cloudy_stl" target=”_blank” >repository</a>. 
- If you don't have a 3D printer, you can use a printing service.
- Once you've printed Cloudy parts, you have to acquire components in the mechanical hardware list. Those components in the mechanical hardware list are necessary to assemble printed parts.

## Print facts
The table shows the facts related to printing a single Cloudy.

| **Part**        | **Print time** | **Material amount** | **Material cost** |
|-----------------|----------------|---------------------|-------------------|
| Mechanic parts  | 62 hours       | 1035 gr             | (ESUN PLA+)$19    |
| Bodywork parts  | 132 hours      | 835 gr              | (ESUN PLA+)$16    |
## Tested Printers
The table shows the printers that are tested and successfully print Cloudy.

| **Model**                | **Cost** | **URL**                                                                                                  |
|--------------------------|----------|----------------------------------------------------------------------------------------------------------|
| Artillery Sidewinder X2  | $469     | [link](https://www.amazon.com/Artillery-Sidewinder-SW-X2-pre-Assembled-300x300x400mm/dp/B09GVTFGCZ?th=1) |
| Creality Ender-3 S1 Plus | $574     | [link](https://www.amazon.com/Creality-Ender-3-S1-Plus-Printer/dp/B0B3WNZDBG)                            |


## Table of Contents

- [Overview and technical specifications](#overview)
    - Frame 
    - Caster wheels
    - Drive train
- [Bill Of Materials](#Billofmaterials)
    - Manufacturing part list
    - Mechanical hardware list
- [Assembly Guide](#AssemblyGuide)


## Overview and Technical specifications

Cloudy is an open-source, 3D-printed robot designed and built by Robolaunch. With its advanced capabilities and innovative design, Cloudy is poised to become a key player in the world of robotics. Whether you're a seasoned DIY enthusiast or just getting started in the world of robotics, Cloudy has something to offer.

- Explore the world of robotics and learn about the latest technology and techniques
- Build, customize, and program your own robot using open-source software and hardware
- Experiment with sensors, motors, and other components to see what Cloudy can do
- Share your creations and collaborate with others in the ROS community
### Dimensions
Robot has a length of 340mm, width 240mm, height 108mm and ground clearence of 18mm's which gives optimum capability to overcome obstackles and enough space for potential use cases.


<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20dimensions%201.png" width="600" height="400" align="top">


### Frame

Cloud2 frame has 3 piece chassis reinforced with aluminum sigma profiles. Able to handle 20kgs of payload 
 Drive train consist of a drive wheel between two caster wheels making a total of 4 caster wheels and 2 drive 
wheels.(fig2)

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20frame%20illus%203.png" width="800" height="350" align="top">

### Caster Wheels

Caster wheels are spring preloaded 4 bar linkage to ensure constant contact with ground.
Ball bearings are used for all hinges and rotating components.
Orings are used as tires on wheels for smooth operation (fig3)

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20caster%20illus%201.png" width="800" height="370" align="top">


### Drive Wheels

Drive wheels are belt driven, reduction ratio is i:3.15. Ratio can be customised by advanced users by custom sized 
pulleys. Belt tension can be adjusted via screws shown below.(fig4)

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20drive%20illus%201.png" width="800" height="620" align="top">


## BILL OF MATERIALS

 Hardware BOM and manufacturing BOM is provided seperately.

### BOM

| ITEM NO. | PART NUMBER                            | DESCRIPTION                   | QTY. |
|----------|----------------------------------------|-------------------------------|------|
| 1        | 0404_011                               |                               | 1    |
| 1.1      | 0404_033                               | Middle frame                  | 1    |
| 1.2      | 0401_002                               |                               | 2    |
| 1.2.1    | 0401_001                               | Caster wheel                  | 1    |
| 1.2.2    | 0401_003                               | Caster wheel                  | 1    |
| 1.2.3    | 0401_004                               | Caster wheel                  | 1    |
| 1.2.4    | O-ring D25_30 d5                       |                               | 1    |
| 1.2.5    | 0401_005                               | Caster wheel                  | 1    |
| 1.2.6    | 0401_006                               | Caster wheel                  | 1    |
| 1.2.7    | 0404_012                               | Caster fixture                | 1    |
| 1.2.8    | Bearing SKF - 634 - 4 x 16 x 5         |                               | 7    |
| 1.2.9    | Circlip DIN 472 - 16 x 1               |                               | 4    |
| 1.2.10   | Hexagon Nut ISO 4032 - M4 - W - N      |                               | 6    |
| 1.2.11   | ISO 7045 - M4 x 16 - Z - 16N           |                               | 6    |
| 1.2.12   | ISO 7046-1 - M3 x 16 - Z - 16N         |                               | 3    |
| 1.3      | 0404_014                               | Rear frame                    | 1    |
| 1.4      | 0404_024                               | Front frame                   | 1    |
| 1.5      | sigma20x20                             |                               | 2    |
| 1.6      | 0404_016                               |                               | 2    |
| 1.6.1    | 0401_004                               | Caster wheel                  | 1    |
| 1.6.2    | O-ring D25_30 d5                       |                               | 1    |
| 1.6.3    | 0404_012                               | Caster fixture                | 1    |
| 1.6.4    | 0404_017                               | Caster wheel                  | 1    |
| 1.6.5    | 0404_018                               | Caster wheel                  | 1    |
| 1.6.6    | 0404_070                               | Caster wheel                  | 1    |
| 1.6.7    | 0404_020                               | Caster wheel                  | 1    |
| 1.6.8    | Bearing SKF - 634 - 4 x 16 x 5         |                               | 7    |
| 1.6.9    | Circlip DIN 472 - 16 x 1               |                               | 4    |
| 1.6.10   | Hexagon Nut ISO 4032 - M4 - W - N      |                               | 6    |
| 1.6.11   | ISO 7045 - M4 x 30 - Z - 30N           |                               | 6    |
| 1.6.12   | ISO 7046-1 - M3 x 16 - Z - 16N         |                               | 3    |
| 1.7      | 0404_059                               |                               | 1    |
| 1.7.1    | 0404_028_50T                           | Drive wheel pulley            | 1    |
| 1.7.2    | 0404_029                               | Motor Flange                  | 1    |
| 1.7.3    | 0404_030                               | Drive train                   | 1    |
| 1.7.4    | 0404_031                               | Drive train                   | 1    |
| 1.7.5    | O-ring D45_50 d5                       |                               | 2    |
| 1.7.6    | AS5600 v1.step                         |                               | 1    |
| 1.7.7    | 0404_034                               | Sensor magnet holder          | 1    |
| 1.7.8    | 0404_035                               | Wheel sensor holder           | 1    |
| 1.7.9    | 17HS8401                               |                               | 1    |
| 1.7.10   | 16 teeth pulley GT2 6mm                |                               | 1    |
| 1.7.11   | GT2 122T BELT 6mm                      |                               | 1    |
| 1.7.12   | 0404_032                               | Wheel                         | 1    |
| 1.7.13   | Bearing SKF - 624 - 4 x 13 x 5         |                               | 4    |
| 1.7.14   | ISO - 4032 - M4 - W - N                |                               | 11   |
| 1.7.15   | Tapping screw DIN 7049-ST2.2x13-C-H-N  |                               | 4    |
| 1.7.16   | ISO 7045 - M4 x 30 - Z - 30N           |                               | 15   |
| 1.8      | 0404_039                               | Rc module holder              | 1    |
| 1.9      | 0404_027                               |                               | 1    |
| 1.9.1    | 0404_028_50T                           | Drive wheel pulley            | 1    |
| 1.9.2    | 0404_029                               | Motor Flange                  | 1    |
| 1.9.3    | 0404_030                               | Drive train                   | 1    |
| 1.9.4    | O-ring D45_50 d5                       |                               | 2    |
| 1.9.5    | AS5600 v1.step                         |                               | 1    |
| 1.9.6    | 0404_034                               | Sensor magnet holder          | 1    |
| 1.9.7    | 0404_035                               | Wheel sensor holder           | 1    |
| 1.9.8    | 17HS8401                               |                               | 1    |
| 1.9.9    | 16 teeth pulley GT2 6mm                |                               | 1    |
| 1.9.10   | GT2 122T BELT 6mm                      |                               | 1    |
| 1.9.11   | 0404_032                               | Wheel                         | 1    |
| 1.9.12   | 0404_060                               | Drive train                   | 1    |
| 1.9.13   | Bearing SKF - 624 - 4 x 13 x 5         |                               | 4    |
| 1.9.14   | ISO - 4032 - M4 - W - N                |                               | 11   |
| 1.9.15   | Tapping screw DIN 7049-ST2.2x13-C-H-N  |                               | 4    |
| 1.9.16   | ISO 7045 - M3 x 20 - Z - 20N           |                               | 15   |
| 1.10     | Hexagon Nut ISO 4032 - M3 - W - N      |                               | 21   |
| 1.11     | ISO - 4032 - M3 - W - N                |                               | 13   |
| 1.12     | ISO 7045 - M3 x 10 - Z - 10N           |                               | 14   |
| 1.13     | Ext. Spring 1/4'' x 7/8''              |                               | 4    |
| 1.14     | Ext. Spring 11/32'' x 1-27/32''        |                               | 2    |
| 1.15     | Sigma nut K8 M4                        |                               | 4    |
| 2        | 0404_045                               |                               | 1    |
| 2.1      | 0404_044                               | Front panel     (COSMETIC)    | 1    |
| 2.2      | Intel D435i                            |                               | 1    |
| 2.3      | led sticker 8led                       |                               | 2    |
| 2.4      | VL6180X-Time_of_Flight_Sensor.stp      |                               | 2    |
| 2.5      | 0404_046                               | Front lighting     (COSMETIC) | 1    |
| 2.6      | Tapping screw DIN 7049-ST2.2x6.5-C-H-N |                               | 8    |
| 2.7      | ISO 7045 - M3 x 12 - Z - 12N           |                               | 4    |
| 3        | 0404_048                               |                               | 1    |
| 3.1      | 0404_047                               | Rear panel     (COSMETIC)     | 1    |
| 3.2      | led sticker 8led                       |                               | 2    |
| 3.3      | Push Button Switch E-Stop mini D16     |                               | 1    |
| 3.4      | OLED Display 128x64                    |                               | 1    |
| 3.5      | GX12-2P v2                             |                               | 1    |
| 3.6      | 0404_054                               | Rear lighting     (COSMETIC)  | 2    |
| 3.7      | 0404_053                               | Rear Lighting     (COSMETIC)  | 1    |
| 3.8      | 0404_066_USB_HDMI_ETHERNET_POWER       |                               | 1    |
| 3.9      | USB Type A - panel mount               |                               | 1    |
| 3.10     | hdmi_f_chassis                         |                               | 1    |
| 3.11     | PJ-011A                                |                               | 1    |
| 3.12     | Tapping screw DIN 7049-ST2.9x6.5-C-H-N |                               | 8    |
| 3.13     | Button_ 12_Switch                      |                               | 1    |
| 3.14     | Push Switch Button (12mm) R            |                               | 1    |
| 4        | 0404_051                               | Power box                     | 1    |
| 5        | 0404_052                               | Battery cap (COSMETIC)        | 1    |
| 6        | 0404_064                               | Side panel (COSMETIC)         | 1    |
| 7        | 0404_055                               | Side Panel (COSMETIC)         | 1    |
| 8        | 0404_071                               |                               | 1    |
| 8.1      | 0404_067                               | Battery bottom (COSMETIC)     | 1    |
| 8.2      | 0404_049                               | Top panel (COSMETIC)          | 1    |
| 8.3      | Tapping screw DIN 7049-ST2.9x9.5-C-H-N |                               | 5    |
| 9        | Tapping screw DIN 7049-ST2.9x16-C-H-N  |                               | 4    |
| 10       | DIN EN ISO 7045 - M3 x 16 - Z - 16N    |                               | 4    |
| 11       | ISO 7046-1 - M3 x 16 - Z - 16N         |                               | 4    |

### BOM Hardware

ISO 7045 --> countersunk roundhead cross recessed
ISO 

| ITEM NO. | PART NUMBER                            | DESCRIPTION | QTY. |
|----------|----------------------------------------|-------------|------|
| 1        | ISO 7045 - M3 x 8 - Z - 8N             |             | 8    |
| 2        | ISO 7045 - M3 x 10 - Z - 10N           |             | 6    |
| 3        | ISO 7045 - M3 x 12 - Z - 12N           |             | 16   |
| 4        | ISO 7045 - M3 x 16 - Z - 16N           |             | 8    |
| 5        | ISO 7046-1 - M3 x 16 - Z - 16N         |             | 16   |
| 6        | ISO 7045 - M3 x 20 - Z - 20N           |             | 4    | 
| 7        | ISO 7045 - M3 x 25 - Z - 25N           |             | 4    |
| 8        | ISO 7045 - M4 x 12 - Z - 12N           |             | 4    |
| 9        | ISO 7045 - M4 x 16 - Z - 16N           |             | 20   |
| 10       | ISO 7045 - M4 x 30 - Z - 30N           |             | 6    |
| 11       | Hexagon Nut ISO 4032 - M3 - W - N      |             | 54   |
| 12       | Hexagon Nut ISO 4032 - M4 - W - N      |             | 26   |
| 13       | Tapping screw DIN 7049-ST2.2x6.5-C-H-N |             | 12   |
| 14       | Tapping screw DIN 7049-ST2.2x13-C-H-N  |             | 4    |
| 15       | Tapping screw DIN 7049-ST2.9x9.5-C-H-N |             | 9    |
| 16       | Tapping screw DIN 7049-ST2.9x6.5-C-H-N |             | 4    |
| 17       | Tapping screw DIN 7049-ST2.9x16-C-H-N  |             | 4    |
| 18       | Bearing SKF - 61800 - 10 x 19 x 5      |             | 2    |
| 19       | Bearing SKF - 61804 - 20 x 32 x 7      |             | 2    |
| 20       | Bearing SKF - 634 - 4 x 16 x 5         |             | 28   |
| 21       | Bearing SKF - 624 - 4 x 13 x 5         |             | 4    |
| 22       | Circlip DIN 472 - 16 x 1               |             | 16   |
| 23       | O-ring D25_30 d5                       |             | 4    |
| 24       | O-ring D45_50 d5                       |             | 4    |
| 25       | sigma20x20                             |             | 2    |
| 26       | 17HS8401                               |             | 2    |
| 27       | 16 teeth pulley GT2 6mm                |             | 2    |
| 28       | GT2 122T BELT 6mm                      |             | 2    |
| 29       | Ext. Spring 1/4'' x 7/8''              |             | 4    |
| 30       | Ext. Spring 11/32'' x 1-27/32''        |             | 2    |
| 30       | Sigma nut K8 M4                        |             | 4    |

### BOM Manufacture

All of the robot parts are completely 3d printable. We recommend using maximum 0.6mm nozzle and setting maximum 0.32mm layer 
thickness for printing non cosmetic parts for faster printing while maintaining minimum required dimensional tolerances.

 We recommend using PLA for all parts. For custom applications requiring more durable materials ABS, PETG or other high strength material 
can be used.
 
 Cosmetic parts are bodywork parts, thinner layer thickness, smaller diameter nozzle and slower printing speed may be preferred for better surface finish comrimising printing time.

| ITEM NO. | PART NUMBER  | DESCRIPTION                   | QTY. |
|----------|--------------|-------------------------------|------|
| 1        | 0404_033     | Middle frame                  | 1    |
| 2        | 0401_001     | Caster wheel                  | 2    |
| 5        | 0401_003     | Caster wheel                  | 2    |
| 7        | 0401_004     | Caster wheel                  | 4    |
| 9        | 0401_005     | Caster wheel                  | 2    |
| 10       | 0401_006     | Caster wheel                  | 2    |
| 11       | 0404_012     | Caster fixture                | 4    |
| 16       | 0404_014     | Rear frame                    | 1    |
| 17       | 0404_024     | Front frame                   | 1    |
| 19       | 0404_017     | Caster wheel                  | 2    |
| 20       | 0404_018     | Caster wheel                  | 2    |
| 21       | 0404_070     | Caster wheel                  | 2    |
| 22       | 0404_020     | Caster wheel                  | 2    |
| 23       | 0404_028_50T | Drive wheel pulley            | 2    |
| 24       | 0404_029     | Motor Flange                  | 2    |
| 25       | 0404_030     | Drive train                   | 2    |
| 27       | 0404_031     | Drive train                   | 1    |
| 34       | 0404_034     | Sensor magnet holder          | 2    |
| 35       | 0404_035     | Wheel sensor holder           | 2    |
| 41       | 0404_032     | Wheel                         | 2    |
| 47       | 0404_039     | Rc module holder              | 1    |
| 48       | 0404_060     | Drive train                   | 1    |
| 61       | 0404_044     | Front panel     (COSMETIC)    | 1    |
| 65       | 0404_046     | Front lighting     (COSMETIC) | 1    |
| 66       | 0404_047     | Rear panel     (COSMETIC)     | 1    |
| 73       | 0404_054     | Rear lighting     (COSMETIC)  | 2    |
| 74       | 0404_053     | Rear Lighting     (COSMETIC)  | 1    |
| 82       | 0404_051     | Power box                     | 1    |
| 83       | 0404_052     | Battery cap (COSMETIC)        | 1    |
| 84       | 0404_064     | Side panel (COSMETIC)         | 1    |
| 87       | 0404_055     | Side Panel (COSMETIC)         | 1    |
| 89       | 0404_067     | Battery bottom (COSMETIC)     | 1    |
| 90       | 0404_049     | Top panel (COSMETIC)          | 1    |

## Assembly Guide

### Preparing Parts
 Before assembling, all the parts must be cleaned of support structures. Mounting surfaces and holes must be levelled of 
imperfections.
Tools required for part preparations;
- Pliers
- Utility knife
- flat head screwdriver

 Follow step by step guide for complete mechanical systems assembly.
Tools required for assembly:
- Philips screwdriver
- Small assembly hammer
- Pliers
- Allen key for m3 setscrew

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%201.png" width="800" height="420" align="top">
<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%201.1.png" width="800" height="420" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%202.png" width="800" height="520" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%203.png" width="800" height="590" align="top">

------------------------------------------------------------------------------
<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%204.png" width="800" height="600" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%205.png" width="800" height="600" align="top">
<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%205.3.png" width="800" height="600" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%206.png" width="800" height="500" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%207.png" width="800" height="510" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%208.png" width="800" height="620" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%209.1.png"  align="top"  >

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2010.png" width="800" height="520" rotate="90" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2011.png" width="800" height="560" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2012.png" width="800" height="420" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2013.png" width="800" height="730" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2014.png" width="800" height="630" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2015.png" width="800" height="500" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2016.png" width="800" height="750" align="top">

------------------------------------------------------------------------------

<img src="https://raw.githubusercontent.com/robolaunch/cloudy_stl/main/images/cloudy%20assem%20step%2017.png" width="800" height="420" align="top">

------------------------------------------------------------------------------

# Hardware Guide
## Specifications
Cloudy uses the esp32 micro controller on the embedded hardware side.

Cloudy robot has a Hardware Stack containing the main electronics and computer, all the parts here are cooled by a powerful fan. The Hardware Stack is easily separated from the body of the cloudy, which allows you to easily replace them and use them outside of the robot.<br/>
<img style="width:400px; height:400px;" src="https://ae01.alicdn.com/kf/H4de861835bb241de85a0f85ce23112f9a/ESP32-Wemos-D1-Mini-Arduino-UNO-i-in-R3-D1-R32-WIFI-kablosuz-bluetooth-geli-tirme.jpg_Q90.jpg_.webp"/>
  <figcaption>Esp32 Wemos D1 Uno</figcaption>
<br/>
The first layer of the Hardware Stack contains an esp32 microcontroller. This board is known as uno esp32 and is compatible with most arduino uno shields.<br/><br/><br/>
<img style="width:170px; height:170px; float:left;" src="https://st.myideasoft.com/idea/cd/40/myassets/products/058/cnc-shield.jpg?revision=1484509194"/>
<img style="width:170px; height:170px;" src="https://image.robotistan.com/vnh3asp30-step-motor-surucusu-38119-98-O.jpg"/>  
<figcaption>CNC Shield - Monster Moto Shield</figcaption><br/>
The second layer contains shield for the motor drivers. Depending on your motor type (step, dc, brushless) you can choose different shield to the compatible driver board.this layer ensures the stable operation of the motor drivers.<br/><br/><br/>
<img style="width:170px; height:170px; float:left;" src="https://m.media-amazon.com/images/I/41cn6diLE0L.jpg"/>
<img style="width:170px; height:170px;" src="https://live.staticflickr.com/65535/52217221682_6e7508c486_o.png"/>
<img style="width:170px; height:170px;" src="https://www.robotsepeti.com/nvidia-jetson-nano-2gb-developer-kit-wifi-nvidia-nvidia-13114-68-B.png"/>
  <figcaption>Raspberry Pi 4 - Orange Pi 5 - Jetson Nano</figcaption><br/>
On the top layer, there is a single board computer. Cloudy supports raspberry pi, orange pi 5, jetson nano computers. You can easily access the USBs on it and use add-ons such as stereo camera and lidar.
<br/>
<br/>
In addition, the body of the Cloudy is equipped with many sensors. These sensors work with i2c protocol and are connected with i2c multiplexer so you can connect multiple same sensors.Cloudy includes 3 distance sensors, 2 for collision avoidance in the bumper, and 1 for protection from falling from a height. Also there are neopixel LEDs on all four sides, these LEDs are used for robot visibility and status indication. You can learn the battery voltage and status with the tiny oled screen at the top.
<br/>
<br/><br/>
<br/>
<img style="width:170px; height:170px; float:left;" src="https://st.myideasoft.com/idea/cd/40/myassets/products/827/ws2812-8li-serit-rgb-led-modulu-rgb-stick-modul-drone-1-1.JPG?revision=1582459848"/>
<img style="width:170px; height:170px;" src="https://www.direnc.net/vl6180-optik-sensor-modulu-arduino-uyumlu-lazer-ve-lazerli-sensorler-estardyn-40330-14-B.jpg"/>
<img style="width:170px; height:170px;" src="https://www.robotistan.com/13-inch-i2c-oled-ekran-ssd1106-25686-80-O.jpg"/>
<img style="width:170px; height:170px;" src="https://robiz.net/image/cache/data/sensors/gyro/mpu6050/mpu6050_01-500x500.jpg"/>
<br/><br/><br/>

## Robot Build Roadmap: 
This roadmap shows the order of parts to be selected for robot manufacture for all robot types. Starting from step 1, you can create the robot you want to build.
<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/BUsidHoXK9xqfDExd4iyRW@7YNFXnKbYmPnTJDWNcchx"></iframe>

| **Attribute**            | **Description** |
|--------------------------|-----------------|
| Weight                   | ~2.7 kg         |
| Chassis material         | PLA(Default)    |
| Maximum linear velocity  |                 |
| Maximum angular velocity |                 |
| Maximum payload          |                 |
| Battery life             |                 |
| Wi-Fi range&throughput   |                 |
| RC Control Range         |     ~ 300m      |

## Block Diagram

A block diagram of robolaunch Cloudy components and connections between them.</br>

<p align="center">
<img src="https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/scheme.png" alt="Scheme">
</p>

## Wiring Diagram

The detailed wiring diagram is below. If you want to improve or modify this diagram, you can download the fritzing application file <a href="#">here</a> and modify it.

<p align="center">
<img src="https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/cloudy_hardware4_bb.png" alt="Scheme">
</p>

## Part List

| **Part Type**            | **Amount** |
|--------------------------|-----------------|
| Raspberry Pi 4 8GB         | 1    |
| Orange Pi 5 16GB  | Optional                |
| Jetson Nano | Optional                |
| Wemos D1 R32         | 1                |
| Arduino Cnc Shield             | 1                |
| Monster Moto Shield            | Optional                |
| UBEC 5V 6A          |  1      |
| Hobbywing 5V 3A Ubec         |  Optional      |
| Apm Power Module         |  1      |
| 24V Cooling Fan        |  1      |
|6S 3200 mAh Li-on Battery Pack | 1 |
|6S 2200 mAh Lipo Battery | Optional |
|Nema 17 Stepper Motor | 2 |
| 12V DC Motor With Encoder| Optional (2) |
|DRV8825 Stepper Motor Controller | 2 |
|MPU6050 IMU | 1 |
| IA6B Ibus Receiver| 1 |
|Intel Realsense D435i | 1 |
|RPlidar A1M8 Lidar | 1 |
|Neopixel Led Stick 8x | 4 |
|Adafruit TCA9548A | 1 |
| Usb Micro Usb Cable 20cm | 1 |
| Push button 12mm | 1 |
| Emergency Button 16mm | 1 |
| OLED I2C 0.96" Display | 1 |
| VL6180X TOF Distance Sensor | 3 |
| AS5600 encoder | 2 |
|JST Connector Female | 7 |
| JST Connector Male | 7 |
|Splice Terminal | 18 |
|Easy PDB Body 5 channel | 1 |
| Easy PDB connector | 5 |
| Xt30 Connector Pair| 1 |








## Installation Guide

## Hardware Box Setup


# Software Guide

Welcome to Software Guide of Cloudy. In this guide we will look at the software requirements, components and how to use them. All the software is available on the [Github repository](https://github.com/robolaunch/cloudy). Feel free to contribute!

## Requirements

Cloudy is tested on the systems below:

| Operating System    | ROS2 version |
|---------------------|--------------|
| Ubuntu 22.04(arm64) | Humble       |
| Ubuntu 22.04(amd64) | Humble       |


## High-Level Architecture
Here is a high level architecture diagram of the Cloudy software. You can access and modify the block diagram from the [link](https://whimsical.com/LxtNBwNDTjNXYP3EHM6uqS)! 
<p align="center">
<img src="./software_block_diagram.png" alt="softwareblockdiagram">
</p>

## Detailed Architecture

Here is a detailed architecture diagram of the Cloudy software. You can access and modify the detailed diagram from the [link](https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/DetailedSoftwareDiagram.drawio)! 
<p align="center">
<img src="./DetailedSoftwareDiagram.drawio.png" alt="detailedsoftwareblockdiagram">
</p>

## Components

In this section software components of the Cloudy will be explained. We will start from the Low Level components in the diagram then move to High Level components. 

### micro-ROS

micro-ROS bridges the gap between resource-constrained microcontrollers and larger processors in robotic applications that are based on the Robot Operating System(ROS). micro-ROS source code can be found at [link](https://github.com/micro-ROS). We are using ESP32 with precompiled micro-ROS library, in addition to that to receive signals from controller we are using an [IBus library](https://github.com/bmellink/IBusBM), to control motors [step motor library](https://github.com/gin66/FastAccelStepper) and to configure leds a [led library](https://github.com/adafruit/Adafruit_NeoPixel). Since micro-ROS enables the seamless integration with ROS2, we can control motors and configure leds using ROS2 topics published from computer! 

You can check the firmware code from [Github repository](https://github.com/robolaunch/cloudy/blob/main/robolaunch_cloudy_hardware/firmware/firmware_flysky.ino).

- Note that the remote controlling is optional. You can still drive your robot using teleoperation from ROS2. The teleoperation is explained in [Teleoperating Cloudy](?id=teleoperation)

Here is a table of topics consumed by ESP32 microcontroller

| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /left_motor_speed  | std::Msg::Float32 | Desired left motor speed in radians                  |
| /right_motor_speed | std::Msg::Float32 | Desired right motor speed in radians                 |
| /neopixel_led      | std::Msg::Int8    | 1-headlight 2-emergency 3-left_signal 4-right_signal |



### Teleoperation
There are 3 core packages for teleoperating Cloudy: [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description), [robolaunch_cloudy_bringup](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_bringup) and [robolaunch_cloudy_hardware](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_hardware). We will examine those packages step by step.
#### robolaunch_cloudy_description
 The first package is [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) which is includes URDF files describing Cloudy and sensors. Other packages uses [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package to define a physical robot instance. 



| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /robot_description  | std::Msg::String | Robot descriptions in XML format                     |

Let's check the descriptions:
```bash
ros2 launch robolaunch_cloudy_description description.launch.py
```


Now the [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package publishes robot descriptions to the ROS2 network. We can visualize the robot description using RViz.

<p align="center">
<img src="./cloudy_rviz.png" alt="cloudyrviz" height="500px">
</p>

#### robolaunch_cloudy_bringup

The second package is [robolaunch_cloudy_bringup](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_bringup) which defines the [ros2_control](https://control.ros.org/master/index.html) parameters and spawns controllers&state publishers(using [robolaunch_cloudy_description](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_description) package). Controller nodes subscribes to /cmd_vel topic. To control the robot we have to publish `Twist` type message to  `/cmd_vel` topic. Configurations related to control can be adjusted from the `/config/diffbot_diff_drive_controller.yaml` file. 

| **Topic**          | **Type**          | **Description**                                      |
|--------------------|-------------------|------------------------------------------------------|
| /cmd_vel  | geometry::Msg::Twist | Velocity command in radians per second                     |

#### robolaunch_cloudy_hardware

The [robolaunch_cloudy_hardware](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_hardware) package creates a hardware interface to communicate with actuators. By design choice we decide to perform control calculations with ros2_control on Single Board Computer. Then the desired velocities gets forward to ESP32 over `left_motor_speed` and `right_motor_speed` topics. To remember topic descriptions refer to [micro-ROS](?id=micro-ros) section.

#### Controlling robot

To control the robot we have to launch [robolaunch_cloudy_bringup](https://github.com/robolaunch/cloudy/tree/main/robolaunch_cloudy_bringup) node.

```bash
ros2 launch robolaunch_cloudy_bringup diffbot_system.launch.py
```

Now Cloudy is alive! Let's move it by opening a new terminal:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
<p align="center">
<img src="./cloudy_bringup.gif" alt="cloudyrviz" height="500px">
</p>

### SLAM and Navigation

**Vehicle Types**
- cloudy_v2 (default)
- cloudy_v1
- arcelik

#### Simulation

The launch files for simulation are collected under `sim_launch` folder. All config files are under `config` folder and the ones starting with `sim_` are used for simulation.

First source the workspace
```bash
source install/setup.bash
```
In order to launch both SLAM and navigation run:
```bash
ros2 launch robolaunch_cloudy_navigation sim_launch_all.launch.py
```

To launch with other robolaunch robots set the `vehicle` launch argument to one of the vehicle types given above. Openning `arcelik` vehicle might take a few minutes since it has detailed parts.
```bash
ros2 launch robolaunch_cloudy_navigation sim_launch_all.launch.py vehicle:="'arcelik'"
```

If you want to launch saperately, first open the simulation. The default vehicle is `cloudy_v2` but if you wish to use another robot, set the `vehicle` parameter to one of the vehicles listed above. Default map is warehouse but if you wish to open on playground world use `world:=playground`.
```bash
ros2 launch robolaunch_cloudy_simulator gazebo.launch.py
```

Then launch slam:
```bash
ros2 launch robolaunch_cloudy_navigation sim_slam.launch.py
```

Finally, launch navigation. If you would like to open rviz set rviz parameter true by adding `rviz:=true` at the end of the command:
```bash
ros2 launch robolaunch_cloudy_navigation sim_nav.launch.py
```

#### Physical

##### Cloudy

Connect to the robot via ssh and launch the sensor nodes: (password: robolaunch)

```bash
ssh ubuntu@172.16.44.219
```
Launch `rplidar` and check the scan data:

```bash
ros2 launch rplidar_ros rplidar.launch.py
```

```bash
ros2 topic echo /scan
```
If there is no data on the topic, change the serial port of the lidar. First see the available ports:

```bash
ls /dev/ | grep USB
```

Then change the port with `'serial_port': '/dev/ttyUSB0'` parameter.

```bash
sudo nano /opt/ros/humble/share/rplidar_ros/launch/rplidar.launch.py
```
After the change source the ros distro once again.

```bash
source /opt/ros/humble/setup.bash
```

Launch IMU:

```bash
cd ~/imu && \
. install/setup.bash && \
ros2 launch mpu6050driver mpu6050driver_launch.py
```

Launch micro ROS agent with the other port and push the little silver button on top of the robot:

```bash
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB1
```

Follow the instructions below in a remote computer which is connected to the same network as the robot. They would all work also in robots computer; however, since the nodes that are going to be run are computationally havy, this would not work optimally. **Do not give ROS_DOMAIN_ID** the low level controller will not work if it is given.

The launch files used for physical world are under `launch` folder. The config files that do not start with `_sim` are for physical world. Since Arcelik robot has different sensor set and since it uses different low level controller it has saperate launch files. The files starting with `arcelik_` are for Arcelik robot only. The files starting with `cloudy_` can be used both with `cloudy_v2` and `cloudy_v1` by setting the parameter `vehicle:="'<vehicle name>'"`, if the parameter is not set the default vehicle is `cloudy_v2`. 

First source the workspace:

```bash
source install/setup.bash
```

Launch `SLAM` for desired vehicle. If Arcelik vehicle is being used, lauch `arcelik_slam.launch.py`. If cloudy_v1 or cloudy_v2 is being used, launch `cloudy_slam.launch.py`. They launch the proper nodes for lidar sensor, laser odometry, ekstended kalman filter for sensor fusion, low level controller enabling `cmd_vel` topic, and laser filter to prevent lidar from seing the robot as obstacle. To launch SLAM with rviz set rviz parameter true by `rviz:=true`.

```bash
ros2 launch robolaunch_cloudy_navigation cloudy_slam.launch.py
```

Then in a new terminal launch `nav2` for autonomous navigation. This file only launches bringup for nav2 using the proper config file.
```bash
source install/setup.bash \
ros2 launch robolaunch_cloudy_navigation cloudy_nav.launch.py
```

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



## Community
- [Website](https://www.robolaunch.io/)
- [LinkedIn](https://www.linkedin.com/company/robolaunch)
- [Twitter](https://twitter.com/robolaunch)
- [Slack]() - *soon*
- [Discord]() - *soon*
- [robolaunch Forum]() - *soon*

## Contributing

Please see [this guide](./CONTRIBUTING.md) if you want to contribute.

