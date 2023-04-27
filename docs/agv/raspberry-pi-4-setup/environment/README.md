# Setting up Environment

You have two options for setting up the ROS 2 environment and launch Cloudy Mini-AGV packages.

- [***Option 1:*** **Setting up Robotics Cloud**](./agv/raspberry-pi-4-setup/environment/robotics-cloud/) This option is recommended way to setup an environment. With this method, you will first setup a cloud instance and register your Cloudy Mini-AGV using Kubernetes native methods. Variety of ROS 2 environments can be provisioned in Kubernetes and you can offload GPU-heavy and CPU-heavy tasks to the cloud.
- [***Option 2:*** **Setting up Host**](./agv/raspberry-pi-4-setup/environment/host.md) This is the legacy way to setup an environment. With this method, you will install ROS 2 to Ubuntu Server you configured earlier and prepare ROS 2 workspaces.