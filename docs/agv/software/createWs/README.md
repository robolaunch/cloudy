# Create Workspace
## Github Repository
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
