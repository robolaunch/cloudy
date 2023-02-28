## Single Board Computer Setup 

**Setup With SD Card**
* Download ubuntu 22.04 image for selected SBC
* Write the image to sd card with <a href="https://win32diskimager.org/">win32 disk imager</a> or <a href="https://www.balena.io/etcher">balena etcher</a>.
* Install ROS2 Humble from <a href="https://docs.ros.org/en/humble/index.html">ROS Documentation</a>.
* Clone the cloudy robot repository to SBC from https://github.com/robolaunch/cloudy
* Clone the micro ros setup to SBC from https://github.com/micro-ROS/micro_ros_setup

The Cloudy robot utilizes Micro ROS for connecting to ROS2. In order to use the Cloudy robot with ROS2, it is necessary to setup the Micro ROS Agent package on the SBC computer that will be controlling the robot.

ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0

**Setup With Robolaunch Cloud Kubernetes**
* Download ubuntu 20.04 image for selected SBC

    ***K3S Installation*** 
        apt-get update 
        curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.24.10+k3s1 K3S_KUBECONFIG_MODE="644" INSTALL_K3S_EXEC="  --cluster-cidr=10.200.1.0/24 --service-cidr=10.200.2.0/24    --cluster-domain=robot-arm-01.local --disable-network-policy --disable=traefik --disable=local-storage --kube-apiserver-arg oidc-issuer-url='https://identity.robolaunch.cloud/auth/realms/robolaunch' --kube-apiserver-arg oidc-client-id=gatekeeper --kube-apiserver-arg oidc-username-claim=preferred_username --kube-apiserver-arg oidc-groups-claim=groups" sh - 
* Check to ```kubectl get nodes``` command is turn READY
* Check to ```kubectl get pods -A ``` command status is Running

    ***Helm and OpenEBS Installation***
        wget https://get.helm.sh/helm-v3.8.0-linux-arm64.tar.gz
        tar -zxvf helm*.tar.gz
        cp /root/linux-arm64/helm /usr/local/bin/helm
        export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
        helm repo add openebs https://openebs.github.io/charts 
        helm repo update
        export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
        helm install openebs --namespace openebs openebs/openebs --create-namespace
        kubectl patch storageclass openebs-hostpath -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

?> If you encounter below problem (The connection to the server 127.0.0.1:6443 was refused - did you specify the right host or port?)</br></br>
Solution is Add this block cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1 into end of these two files (/boot/cmdline.txt and /boot/firmware/cmdline.txt). Be careful to just these block at the end of line not new line.



## Microcontroller Setup

The Cloudy robot utilizes the Arduino IDE for programming and uploading to the microcontroller. It is suggested to use version 2.0 or higher of the Arduino IDE for an easier experience. Additionally, the Cloudy robot utilizes several Arduino libraries, which should be added to the Arduino IDE prior to programming. The necessary libraries can be found and downloaded below.

https://github.com/micro-ROS/micro_ros_arduino

https://github.com/gin66/FastAccelStepper

https://github.com/bmellink/IBusBM

https://github.com/adafruit/Adafruit_NeoPixel

## Docker Setup

İf you have own kubernetes or just want to use on docker, cloudy docker is avaible on https://github.com/robolaunch/cloudy.

## Cloud Login

Login to robolaunch.cloud and select the cloudy workspace, you can start to develop and manage robot from everywhere!

 https://www.robolaunch.cloud/login