#!/bin/bash


MAIN_HOME=$HOME/aiops
KUBESPRAY_HOME=$MAIN_HOME/kubespray
K8S_INVENTORY=$KUBESPRAY_HOME/inventory/prod/group_vars
KUBEFLOW_HOME=$MAIN_HOME/kubeflow
CURRENT_FOLD=${PWD}
now_fold=$CURRENT_FOLD
echo $now_fold

host_name=inslab

echo "######################################" 
echo "##  main       home : " $MAIN_HOME
echo "##  kubernetes home : " $KUBESPRAY_HOME
echo "##  kubeflow   home : " $KUBEFLOW_HOME
echo "######################################" 

# for test
#rm -rf $MAIN_HOME
echo "rm -rf /home/inslab/$MAIN_HOME"

function make_fold() 
{
    ## Create install base fold and source clone
    cd
    if [ ! -d $MAIN_HOME ]; then
      mkdir -p $MAIN_HOME
      cp ./hosts.yml $MAIN_HOME/.

      cd $MAIN_HOME
      git clone https://github.com/kubernetes-sigs/kubespray.git
      
    fi
    if [ ! -d $KUBEFLOW_HOME ]; then
      mkdir -p $KUBEFLOW_HOME
    fi
    
    if [ ! -f $MAIN_HOME/hosts.yml ]; then
      cp $now_fold/hosts.yml $MAIN_HOME/.
      echo "cp $now_fold/hosts.yml $MAIN_HOME/."
    fi
}


function k8s_install()
{ 
    master="172.20.11.223"
    node1="172.20.11.184"

    # kubernetes version checkout v 1.16.9
    cd $KUBESPRAY_HOME
    git checkout v2.12.6 

    python3 -m venv $KUBESPRAY_HOME/venv
    source $KUBESPRAY_HOME/venv/bin/activate
    pip install -r $KUBESPRAY_HOME/requirements.txt 
    
    cp -rfp $KUBESPRAY_HOME/inventory/sample $KUBESPRAY_HOME/inventory/prod 
    
    # master=172.02.11.182  node1=172.20.11.127
    declare -a IPS=($master $node1)
    CONFIG_FILE=inventory/prod/hosts.yml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
    
    cp -rf $MAIN_HOME/hosts.yml $KUBESPRAY_HOME/inventory/prod/.
    
}

function substitute_word()
{
    # cluster_name: cluster.local : inventory/prod/group_vars/k8s-cluster/k8s-cluster.yml
    sed -i'.bak' $'s/cluster_name: cluster.local/cluster_name: kubeflow.gantry/g' $K8S_INVENTORY/k8s-cluster/k8s-cluster.yml
    echo "ansible_user: $host_name" >> $K8S_INVENTORY/all/all.yml
    echo "ansible_ssh_private_key_file: $HOME/.ssh/id_rsa" >> $K8S_INVENTORY/all/all.yml 
     
}

function main()
{
    echo "MAIN RUN"
    make_fold
    #if [ ! -d $KUBESPRAY_HOME ]; then 
      k8s_install
    #fi
    substitute_word
}
main

