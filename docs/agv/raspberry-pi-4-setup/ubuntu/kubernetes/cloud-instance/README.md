# Setting Up Cloud Instance

This is the table of contents for this document.

- [Quick Start](#quick-start)
  - [Running the Script](#running-the-script)
  - [Getting Connection Hub Key](#get-connection-hub-key)
- [Components](#components)

## Quick Start

This document assumes you have **a desktop environment** or **virtual machine** (with `amd64` architecture) on any cloud provider and has Ubuntu 20.04 or 22.04 on it.

### Running the Script

Run the following commands to set up cloud instance:

```bash
# inside physical instance
sudo -i # login as root
export ORGANIZATION=sample-org
export TEAM=sample-team
export REGION=sample-region
export CLOUD_INSTANCE=cloud-instance
export CLOUD_INSTANCE_ALIAS=my-first-instance
export DESIRED_CLUSTER_CIDR=10.100.1.0/24
export DESIRED_SERVICE_CIDR=10.100.2.0/24
export RUN_SCRIPT=run.sh # replace `run.sh` with `run_desktop.sh` if you are in a desktop environment
wget https://raw.githubusercontent.com/robolaunch/cosmodrome/main/instance-setup/cloud-instance/$RUN_SCRIPT
chmod +x $RUN_SCRIPT
./$RUN_SCRIPT
```

The output will be similar to this:
```
Installing tools...
Setting up NVIDIA container runtime...
Setting up k3s cluster...
Checking cluster health...
Labeling node...
Updating Helm repositories...
Installing openebs...
Installing NVIDIA device plugin...
Installing cert-manager...
Installing robolaunch Operator Suite...
Deploying Connection Hub...


Get connection hub key by running the command below:

kubectl get connectionhub connection-hub -o jsonpath={.status.key} | yq -P

You can use this key to establish a connection with cloud instance my-first-instance/cloud-instance.
```

It's done. Now you can get the connection hub key in the next section.

### Getting Connection Hub Key

```bash
kubectl get connectionhub connection-hub -o jsonpath={.status.key} | yq -P
```

You should save this key since it will be used to register physical instances.