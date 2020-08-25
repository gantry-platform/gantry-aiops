# kubernetes 설치 (master and node1 or noede2 ... nodeN)
## kubernetes 기본 환경 설정 (kubespray_master와 kubespray_node1 동일하게 구성)

### Python 설치
Ansible이 작업을 수행하는 모든 서버는 python이 설치되어져 있어야 합니다. Ubuntu 18.04에서는 기본적으로 Python3이 설치되어져 있으므로 symbolic link를 만들어 줍니다.    
$ sudo ln -s /usr/bin/python3 /usr/bin/python    

### Swap 비활성화    
$ sudo swapoff -a    
$ sudo sed -i '/ swap /d' /etc/fstab    

$ sudo apt update    
$ sudo apt install openssh-server     
$ sudo apt install net-tools      

### sudo command without password 설정
$ sudo visudo 
   %sudo   ALL=(ALL:ALL) NOPASSWD:ALL     

### 호스트 이름 변경 
$ sudo vi /etc/hostname [옵션]      
    kubespray_master : master 변경      
    kubespray_node1 : node1 변경       
### 마스트와 노드 아이피 확인 
$ ifconfig      
    IP 확인       
### 로그아웃 또는 리부팅 
$ sudo reboot now 

## 제어 서버 환경 설정
### key 기반 인증을 사용할 수 있도록 SSH 구성    
```
$ ssh-keygen –t rsa 
$ ssh-copssh-keygen –ty-id inslab@[kubespray_master IP address] 
$ ssh-copy-id inslab@[kubespray_node1 IP address]

$ mkdir ~/kubeflow
$ cd ~/kubeflow
$ python3 -m venv venv-k8s
$ source venv-k8s/bin/activate

$ git clone  https://github.com/kubernetes-incubator/kubespray.git
$ cd kubespray 
$ git checkout v2.12.6    #because tag:v2.12.6 = kubernetes 1.16.9 version
    k8s check version : $ vi README.md 
$ cp –rfp inventory/sample inventory/kubeflow
$ declare -a IPS=([kubespray_master_IP_address] [kubespray_node1_IP_address]) 
$ CONFIG_FILE=inventory/kubeflow/hosts.yml python3 contrib/inventory_builder/inventory.py ${IPS[@]}$ vi inventory/kubeflow/hosts.yml     # 마스트 1, 노드1 로 편집 
$ vi inventory/kubeflow/group_vars/k8s-cluster/k8s-cluster.yml
    cluster_name: kubeflow.gantry

$ vi inventory/kubeflow/all/all.yaml
    ansible_user: inslab
    ansible_ssh_private_key_file: [Private키 경로] 
```


# kubeflow 설치 
