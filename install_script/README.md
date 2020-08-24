Python 설치
Ansible이 작업을 수행하는 모든 서버는 python이 설치되어져 있어야 합니다. Ubuntu 18.04에서는 기본적으로 Python3이 설치되어져 있으므로 symbolic link를 만들어 줍니다.    

$ sudo ln -s /usr/bin/python3 /usr/bin/python    

Swap 비활성화    
$ sudo swapoff -a    
$ sudo sed -i '/ swap /d' /etc/fstab    

key 기반 인증을 사용할 수 있도록 SSH 구성    
Ansible을 실행하려는 서버에서 다음 명령어를 실행하여 RSA key pair를 생성합니다.    
$ ssh-keygen -t rsa    
public key를 모든 노드에 복사합니다.    
$ ssh-copy-id inslab@<node-ip-address>   
 
