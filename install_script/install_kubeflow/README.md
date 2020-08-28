# Kubeflow 설치
## step 1
cat 00_set_k8s_env
명령어를 하나 하나 수동으로 복사 붙여넣기 한다. 

## step 2
$ source 01_setenv_kubeflow


## step 3
$ source 02_deploy_kubeflow

## step 4
kfctl apply -V -f ${CONFIG_FILE}


