#!/bin/bash

MAIN_HOME=$HOME/aiops
KUBESPRAY_HOME=$MAIN_HOME/kubespray
K8S_INVENTORY=$KUBESPRAY_HOME/inventory/prod/group_vars
KUBEFLOW_HOME=$MAIN_HOME/kubeflow

host_name=inlab



cd $KUBESPRAY_HOME
source $KUBESPRAY_HOME/venv/bin/activate
pwd
echo "ansible-playbook -i inventory/prod/hosts.yml --become --become-user=root reset.yml -v"
ansible-playbook -i inventory/prod/hosts.yml --become --become-user=root reset.yml -v

