# Setting up Ubuntu Server

## 1. Ubuntu Server Installation to SD Card (using Raspberry PI Imager)

Get `.deb` file of Raspberry PI Imager from [releases](https://github.com/raspberrypi/rpi-imager/releases). Install it to your computer.

```bash
# choose the latest version, v1.7.4 is used for this example
wget https://github.com/raspberrypi/rpi-imager/releases/download/v1.7.4/rpi-imager_1.7.4_amd64.deb
sudo apt install rpi-imager_1.7.4_amd64.deb
```

Insert your SD card to your computer. Open the Raspberry PI Imager. Choose **Ubuntu 20.04/22.04 Server** as operating system and your SD card. Click the "Write" button and wait until it's finished.

<img style="width:50%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/trademark/main/repository-media/cloudy/images/rpimager.jpg"/>

After writing finishes successfully, remove your SD card from your computer and insert it to your Raspberry Pi 4. For further operations, connect your Raspberry Pi 4 to a screen. 

Set your Linux user's password after you logged in as default user. (default username/password is `ubuntu`/`ubuntu`) Then switch to `root` for further processes using:

```bash
sudo -i # and type your password
```

## 2. Configure WiFi Connection

First, you need to setup WiFi configuration manually. Backup your current network configuration before editing anything:

```bash
cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init-original.yaml
```

Now you can edit the configuration. You can use `nano` or `vi` as the terminal editor.

```bash
nano /etc/netplan/50-cloud-init.yaml
```

Add your WiFi configuration in the following format:

```bash
    ethernets:
    # ...
    # add this section
    wifis:
        wlan0:
            optional: true
            access-points:
                "<YOUR-NETWORK>":
                    password: "<YOUR-NETWORK-PASSWORD>"
            dhcp4: true
```

Apply the changes and reboot:

```bash
netplan apply
reboot
```

## 3. Setting up SSH Server

To connect Raspberry Pi 4 remotely with SSH, you need to setup SSH server. First, install OpenSSH server:

```bash
apt-get install -y openssh-server
```

Enable SSH server:

```bash
systemctl enable ssh
```

Start SSH server:

```bash
systemctl start ssh
```

## 4. Configuring Boot CMD Line

?> If no `cmdline.txt` is provided under the directory `/boot/firmware`, check your boot CMD Line configuration path. It may be `/boot/cmdline.txt`. 

Open `/boot/firmware/cmdline.txt` with a terminal editor:

```bash
nano /boot/firmware/cmdline.txt
```

Add the following part at the end of the file (after a space, not after a new line):

```bash
cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1
```

Reboot your Raspberry Pi 4:

```bash
reboot
```

Your Ubuntu on Raspberry Pi 4 is configured successfully. Next step is to set up environment for launching the ROS 2 packages. Proceed with [Setting Up Environment](./agv/raspberry-pi-4-setup/environment/).