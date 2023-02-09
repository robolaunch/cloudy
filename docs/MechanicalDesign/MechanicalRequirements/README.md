## Technical Requirements




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
- [TEST](index)


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

### Preparing Parts## [Technical Requirements](/Design%26Production/)




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
- [TEST](index)


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

