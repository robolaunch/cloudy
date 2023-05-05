# Registering Cloudy Mini-AGV

This is the table of contents for this document.

- [Quick Start](#quick-start)
  - [Running the Script](#running-the-script)
  - [Registering to Cloud Instance](#registering-to-cloud-instance)
  - [Checking the Connection Status](#checking-the-connection-status)
- [Components](#components)

## Quick Start

This document assumes you have a single board computer (eg. Raspberry PI 4) virtual machine (with `arm64` architecture) provisioned on any cloud provider and has Ubuntu 20.04 or 22.04 on it. Also you should complete the steps about [setting up cloud instance](./mini-agv/raspberry-pi-4-setup/environment/robotics-cloud/cloud-instance.md) before starting.

### Running the Script
Run the following commands to register physical instance:

```bash
# inside physical instance
sudo -i # login as root
export CONNECTION_HUB_KEY="<REDACTED>" # enter the key obtained previous section
export SKIP_PLATFORM=true
export ORGANIZATION=sample-org
export TEAM=sample-team
export REGION=sample-region
export CLOUD_INSTANCE=cloud-instance
export CLOUD_INSTANCE_ALIAS=my-first-instance
export PHYSICAL_INSTANCE=cloudy-mini-agv
export DESIRED_CLUSTER_CIDR=10.20.1.0/24 # should be unique per physical instance
export DESIRED_SERVICE_CIDR=10.20.2.0/24 # should be unique per physical instance
export NETWORK=External # should be `Local` if cloud instance uses desktop configuration
wget https://raw.githubusercontent.com/robolaunch/cosmodrome/main/instance-setup/physical-instance/run.sh
chmod +x run.sh
./run.sh
```

The output will be similar to this:
```
Installing tools...
Setting up k3s cluster...
Checking cluster health...
Labeling node...
Updating Helm repositories...
Installing openebs...
Installing cert-manager...
Installing robolaunch Operator Suite...
Joining connection hub instance-1/robot-cloud-06...
Checking connection status...


cat <<EOF | kubectl apply -f -
apiVersion: connection-hub.roboscale.io/v1alpha1
kind: PhysicalInstance
metadata:
  name: cloudy-mini-agv
spec:
  server: https://10.20.1.1:6443
  credentials:
    certificateAuthority: <REDACTED>
    clientCertificate: <REDACTED>
    clientKey: <REDACTED>
EOF

Physical instance is connected to the cloud instance my-first-instance/cloud-instance.
In order to complete registration of physical instance you should run the command above in cloud instance my-first-instance/cloud-instance.
```

It's done. Now you can register the physical instance to cloud instance in the next section.

### Registering to Cloud Instance

Register the Cloudy AGV to the cloud instance by running:

```bash
# inside cloud instance
cat <<EOF | kubectl apply -f -
apiVersion: connection-hub.roboscale.io/v1alpha1
kind: PhysicalInstance
metadata:
  name: cloudy-mini-agv
spec:
  server: https://10.20.1.1:6443
  credentials:
    certificateAuthority: <REDACTED>
    clientCertificate: <REDACTED>
    clientKey: <REDACTED>
EOF
```

### Checking the Connection Status

Check the connection status by running:
```bash
# inside cloud instance
watch kubectl get physicalinstances
```

If the values for the columns `MULTICAST`, `FEDERATION` and `PHASE` are all `Connected`, you have successfully register a physical instance to a cloud instance.
```
NAME              GATEWAY             HOSTNAME           CLUSTER ID        SUBNETS                           MULTICAST   FEDERATION   PHASE
cloudy-mini-agv        ip-172-31-182-159   ip-172-31-28-234   cloudy-mini-agv        ["10.20.2.0/24","10.20.1.0/24"]   Connected   Connected    Connected
```