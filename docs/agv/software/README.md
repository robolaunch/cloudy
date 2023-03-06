

## Software Architecture
In this chapter, we will delve into the specifics of developing and producing the Cloudy software. From setting up the necessary development environments to understanding the software architecture and packages, this section will provide an in-depth look at the technical aspects of the Cloudy software. We will also cover topics such as setting up ROS2, integrating the software with [**robolaunch cloud services**](https://www.robolaunch.cloud), embedded systems, and interfaces. Finally, we will provide troubleshooting tips to help you resolve any issues that may arise during the development process. Whether you're a seasoned developer or just getting started, this chapter is designed to provide you with the information you need to develop and produce the Cloudy software with confidence.

#### High level
Here is a high level architecture diagram of the Cloudy software. You can access and modify the block diagram from the [link](https://whimsical.com/LxtNBwNDTjNXYP3EHM6uqS)! 
<img style="background-color:white!important" src="../../images/software_block_diagram.png" alt="detailedsoftwareblockdiagram">

#### Low level
Here is a detailed architecture diagram of the Cloudy software. You can access and modify the detailed diagram from the [link](https://raw.githubusercontent.com/robolaunch/cloudy/main/docs/DetailedSoftwareDiagram.drawio)! 
<img style="background-color:white!important" src="../../images/DetailedSoftwareDiagram.drawio.png" alt="detailedsoftwareblockdiagram">

## Build Github Repository
We have to initialize the workspace we are going to work on. Let's get started.

- Create a new workspace:

```bash
mkdir cloudy_ws/src -p && cd cloudy_ws/
```
- Clone the repository

```bash
git clone https://github.com/robolaunch/cloudy.git src
```

- Init rosdep if you have not already

```bash
sudo rosdep init
```

- Install dependencies

```bash
sudo rosdep update && rosdep install --from-paths src --ignore-src -y
```

- Source your ROS distribution

```bash
source  /opt/ros/$ROS_DISTRO/setup.bash
```

- Build the repository

```bash
colcon build && source install/setup.bash
```

We have prepared the ROS2 workspace. There are several software packages in Cloudy Software stack. 
For detailed explanation please check [**Software Packages**](/SoftwareDesign/Development%26Production/SoftwarePackages/) page.
