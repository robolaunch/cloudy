# Simulation
![logo](https://raw.githubusercontent.com/robolaunch/trademark/main/repository-media/cloudy/images/cloudy_rviz.png)

## Guide

**Vehicle Types**
- cloudy_v2 (default)
- cloudy_v1
- arcelik

The launch files for simulation are collected under `sim_launch` folder. All config files are under `config` folder and the ones starting with `sim_` are used for simulation.

First source the workspace
```bash
source install/setup.bash
```
## All Launch

In order to launch both SLAM and navigation run:
```bash
ros2 launch robolaunch_cloudy_navigation sim_launch_all.launch.py
```

If you want to launch saperately, first open the simulation. The default vehicle is `cloudy_v2` but if you wish to use another robot, set the `vehicle` parameter to one of the vehicles listed above. Default map is warehouse but if you wish to open on playground world use `world:=playground`.

## Gazebo Launch

```bash
ros2 launch robolaunch_cloudy_simulator gazebo.launch.py
```
## Slam Launch

Then launch slam:
```bash
ros2 launch robolaunch_cloudy_navigation sim_slam.launch.py
```
## Navigation Launch

Finally, launch navigation. If you would like to open rviz set rviz parameter true by adding `rviz:=true` at the end of the command:
```bash
ros2 launch robolaunch_cloudy_navigation sim_nav.launch.py
```

## Config

All config files are under config folder. There are five types of config files which are ekstended kalman filter, slam, navigation, laser filter, and mask filter.</br>
https://github.com/robolaunch/cloudy/blob/main/robolaunch_cloudy_navigation/config/

- sim_slam.yaml         : parameters for navislamgation in simulation.
- sim_navigation.yaml: parameters for navigation in simulation.

