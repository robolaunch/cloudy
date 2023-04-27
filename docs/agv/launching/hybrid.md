# Hybrid Deployment of Cloudy Mini-AGV

?> Make sure that you connected your physical instance (Raspberry Pi 4) to the cloud instance. 

To check the connection, you can run the command below in your cloud instance.

```bash
kubectl get physicalinstances
```

Check the `PHASE` column. It's good to go if you see an output similar to this:

```
NAME              GATEWAY            HOSTNAME           CLUSTER ID        SUBNETS                           MULTICAST   FEDERATION   PHASE
robot-cloudy-01   ip-172-31-180-59   ip-172-31-28-234   robot-cloudy-01   ["10.20.2.0/24","10.20.1.0/24"]   Connected   Connected    Connected
```

In this part, we will deploy Cloudy Mini-AGV to the Kubernetes and launch ROS 2 packages over Kubernetes API. **Notice that you will be deploying all resources to the cloud instance on this document**.

## 1. Deploying Fleet

The very first step is to deploy Fleet resource. Fleet will provision a discovery server to enable ROS 2 nodes in cloud instance and physical instance discover each other. Here is the manifest of the fleet:

```yaml
# fleet.yaml
apiVersion: types.kubefed.io/v1beta1
kind: FederatedFleet
metadata:
  name: my-fleet
spec:
  template:
    metadata:
      name: my-fleet  
    spec:
      discoveryServerTemplate:
        type: Server
        cluster: cloud-instance
        reference:
          name: my-fleet-discovery
          namespace: my-fleet
        hostname: my-fleet
        subdomain: discovery
      hybrid: true
      instances: 
      - cloudy-mini-agv
      - cloud-instance
  placement:
    clusters:
    - name: cloudy-mini-agv
    - name: cloud-instance
  overrides:
  - clusterName: cloud-instance
    clusterOverrides:
    - path: "/spec/discoveryServerTemplate/type"
      value: Server
    - path: "/spec/discoveryServerTemplate/reference"
      value: {}
    - path: "/spec/discoveryServerTemplate/cluster"
      value: ""
    - path: "/metadata/labels"
      op: "add"
      value:
        robolaunch.io/cloud-instance: cloud-instance
        robolaunch.io/cloud-instance-alias: my-first-instance
        robolaunch.io/organization: sample-org
        robolaunch.io/region: sample-region
        robolaunch.io/team: sample-team
  - clusterName: cloudy-mini-agv
    clusterOverrides:
    - path: "/spec/discoveryServerTemplate/type"
      value: Client
    - path: "/metadata/labels"
      op: "add"
      value:
        robolaunch.io/cloud-instance: cloud-instance
        robolaunch.io/cloud-instance-alias: my-first-instance
        robolaunch.io/organization: sample-org
        robolaunch.io/region: sample-region
        robolaunch.io/team: sample-team
        robolaunch.io/physical-instance: cloudy-mini-agv
```

Create Fleet:

```bash
kubectl apply -f fleet.yaml
```

### Checking Fleet Health

In both instances, check the Fleet phase by running:

```bash
# check this command's output in both instances
kubectl get fleet my-fleet -o jsonpath="{.status.phase}"
```

When both instances return Fleet phase as `Ready`, you can proceed with the next section [Deploying Robot](#2-deploying-robot) to provision a ROS 2 environment for Cloudy Mini-AGV.

## 2. Deploying Robot

The second step is to deploy Robot resource. Robot's mission is to create a persistent ROS 2 environment by checking the requirements. For example, environment for Cloud Mini-AGV should have ROS 2 Humble distribution on it. It's workspaces should contain three repositories: [robolaunch Cloudy](https://github.com/robolaunch/cloudy), [RPLidar](https://github.com/babakhani/rplidar_ros2), and [Micro-ROS](https://github.com/micro-ROS/micro_ros_setup). These kinds of configurational parameters about robot's environment should be passed to Kubernetes through Robot's manifest:

```yaml
# robot.yaml
apiVersion: types.kubefed.io/v1beta1
kind: FederatedRobot
metadata:
  name: cloudy
  namespace: my-fleet
spec:
  template:
    metadata:
      name: cloudy
      namespace: my-fleet
    spec:
      distributions: 
      - humble
      rmwImplementation: "rmw_fastrtps_cpp"
      storage:
        amount: 30000
        storageClassConfig:
          name: openebs-hostpath
          accessMode: ReadWriteOnce
      discoveryServerTemplate:
        type: Client
        reference:
          name: my-fleet-discovery
          namespace: my-fleet
        cluster: cloud-instance
        hostname: "xxx"
        subdomain: "yyy"
      rosBridgeTemplate:
        ros2:
          enabled: true
          distro: foxy
      robotDevSuiteTemplate:
        vdiEnabled: false
        ideEnabled: false
        robotVDITemplate:
          serviceType: NodePort
          ingress: false
          privileged: false
          webrtcPortRange: "31000-31004"
          nat1to1: ""
          resources:
            gpuCore: 1
        robotIDETemplate:
          display: true
          serviceType: NodePort
          ingress: false
          privileged: false
          resources:
            gpuCore: 1
      workspaceManagerTemplate:
        workspacesPath: /root/workspaces
        workspaces:
        - name: cloudy-ws
          distro: humble
          repositories:
            cloudy:
              url: "https://github.com/robolaunch/cloudy"
              branch: main
        - name: physical-ws
          distro: humble
          repositories:
            rplidar:
              url: "https://github.com/babakhani/rplidar_ros2"
              branch: ros2
            microros:
              url: "https://github.com/micro-ROS/micro_ros_setup"
              branch: humble
  placement:
    clusters:
    - name: cloudy-mini-agv
    - name: cloud-instance
  overrides:
  - clusterName: cloud-instance
    clusterOverrides:
    - path: "/metadata/labels"
      op: "add"
      value:
        robolaunch.io/cloud-instance: cloud-instance
        robolaunch.io/cloud-instance-alias: my-first-instance
        robolaunch.io/organization: sample-org
        robolaunch.io/region: sample-region
        robolaunch.io/team: sample-team
    - path: "/spec/robotDevSuiteTemplate/vdiEnabled"
      value: true
  - clusterName: cloudy-mini-agv
    clusterOverrides:
    - path: "/metadata/labels"
      op: "add"
      value:
        robolaunch.io/cloud-instance: cloud-instance
        robolaunch.io/cloud-instance-alias: my-first-instance
        robolaunch.io/organization: sample-org
        robolaunch.io/region: sample-region
        robolaunch.io/team: sample-team
        robolaunch.io/physical-instance: cloudy-mini-agv
    - path: "/spec/rosBridgeTemplate/ros2/enabled"
      value: false
    - path: "/spec/robotDevSuiteTemplate/vdiEnabled"
      value: false
    - path: "/spec/robotDevSuiteTemplate/robotVDITemplate/privileged"
      value: true
    - path: "/spec/robotDevSuiteTemplate/robotIDETemplate/privileged"
      value: true
    - path: "/spec/robotDevSuiteTemplate/robotIDETemplate/resources"
      value: {}
    - path: "/spec/robotDevSuiteTemplate/robotIDETemplate/display"
      value: false
```

Create Robot:

```bash
kubectl apply -f robot.yaml
```

### Checking Robot Health

In both instances, check the Robot phase by running when waiting for Robot to prepare the environment for Cloudy Mini-AGV:

```bash
# check this command's output in both instances
kubectl get robot cloudy -n my-fleet
```

```
# sample output
NAMESPACE   NAME     DISTRIBUTIONS   PHASE
my-fleet    cloudy   ["humble"]      EnvironmentReady
```

When both instances return Robot's phase `EnvironmentReady`, you can proceed with the next section [Deploying BuildManager](#3-deploying-buildmanager) to build Cloudy Mini-AGV's ROS 2 packages.

## 3. Deploying BuildManager

Third step is to build Cloudy Mini-AGV's workspaces. To do that over Kubernetes API, we should deploy a BuildManager. BuildManager will specify required commands for building workspaces. BuildManager steps can differ by instance type. For example, in the manifest you see below, BuildManager will build workspace `cloudy-ws` in the cloud instance while it builds `physical-ws` in the physical instance:

```yaml
# buildmanager.yaml
apiVersion: types.kubefed.io/v1beta1
kind: FederatedBuildManager
metadata:
  name: build-cloudy
  namespace: my-fleet
spec:
  template:
    metadata:
      labels:
        robolaunch.io/target-robot: cloudy
      name: build-cloudy
      namespace: my-fleet
    spec:
      steps:
      - name: rosdep-cloudy
        workspace: cloudy-ws
        command: |
          cd $WORKSPACES_PATH/cloudy-ws && \
          source /opt/ros/humble/setup.bash && \
          apt-get update && \
          rosdep update && \
          rosdep install --from-path src --ignore-src -y -r
        selector:
          robolaunch.io/cloud-instance: cloud-instance
      - name: compress-pkgs
        workspace: cloudy-ws
        command: |
          apt-get update && \
          apt-get install -y ros-humble-image-transport-plugins
        selector:
          robolaunch.io/cloud-instance: cloud-instance
      - name: build-cloudy
        workspace: cloudy-ws
        command: |
          cd $WORKSPACES_PATH/cloudy-ws && \
          source /opt/ros/humble/setup.bash && \
          colcon build
        selector:
          robolaunch.io/cloud-instance: cloud-instance
      - name: build-2-cloudy
        workspace: cloudy-ws
        command: |
          cd $WORKSPACES_PATH/cloudy-ws && \
          source /opt/ros/humble/setup.bash && \
          colcon build
        selector:
          robolaunch.io/cloud-instance: cloud-instance
      - name: rosdep-physical
        workspace: physical-ws
        command: |
          cd $WORKSPACES_PATH/physical-ws && \
          source /opt/ros/humble/setup.bash && \
          apt-get update && rosdep update && \
          rosdep install --from-path src --ignore-src -y -r
        selector:
          robolaunch.io/physical-instance: cloudy-mini-agv
      - name: camera-pkgs
        workspace: physical-ws
        command: |
          apt-get update && \
          apt-get install -y ros-humble-image-transport-plugins
        selector:
          robolaunch.io/physical-instance: cloudy-mini-agv
      - name: build-physical
        workspace: physical-ws
        command: |
          cd $WORKSPACES_PATH/physical-ws && \
          source /opt/ros/humble/setup.bash && \
          colcon build
        selector:
          robolaunch.io/physical-instance: cloudy-mini-agv
      - name: micro-ros-physical
        workspace: physical-ws
        command: |
          cd $WORKSPACES_PATH/physical-ws && \
          rosdep update && \
          source install/setup.bash && \
          source install/local_setup.bash && \
          ros2 run micro_ros_setup create_agent_ws.sh && \
          ros2 run micro_ros_setup build_agent.sh
        selector:
          robolaunch.io/physical-instance: cloudy-mini-agv
  placement:
    clusters:
    - name: cloudy-mini-agv
    - name: cloud-instance
```

Create BuildManager:

```bash
kubectl apply -f buildmanager.yaml
```

### Checking BuildManager Steps

BuildManager creates Kubernetes jobs to execute building operations of Cloudy Mini-AGV. You can follow the BuildManager phase by running:

```bash
# check this command's output in both instances
kubectl get buildmanager build-cloudy my-fleet -o jsonpath="{.status.phase}"
```

Also you can monitor the jobs to build Cloudy Mini-AGV:

```bash
# check this command's output in both instances
kubectl get jobs -n my-fleet
```

```
# sample output
NAME                   COMPLETIONS   DURATION   AGE
cloudy-loader          1/1           114s       26h
cloudy-ws-cloner       1/1           16s        26h
build-rosdep-cloudy    1/1           10m        26h
build-compress-pkgs    1/1           18s        26h
build-build-cloudy     1/1           55s        26h
build-build-2-cloudy   1/1           9s         26h
```

Optionally you can follow the logs of the steps by picking a pod created by these jobs with the command below:

```bash
kubectl logs -f pod/build-rosdep-cloudy-59d7w -n my-fleet
```

When both instances return BuildManager's phase as `Ready`, you can proceed with the next section [Deploying LaunchManager](#4-deploying-launchmanager) to launch ROS 2 nodes.

## 4. Deploying LaunchManager

LaunchManager starts ROS 2 nodes by creating a launch pod. The launch descriptions in LaunchManager manifest are converted to `ros2 launch` or `ros2 run` commands by Robot Operator. Each launch container uses same discovery server configurations described in Robot's manifest to discovery each other's nodes and topics.

Manifest for LaunchManager will be added.