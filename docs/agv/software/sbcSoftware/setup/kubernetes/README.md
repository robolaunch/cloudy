## **Setup With Robolaunch Cloud Kubernetes**
<img style="width:50%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/kubernetes.png"/>

* Download ubuntu 20.04 image for selected SBC, follow 3 steps to <a></a>

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

