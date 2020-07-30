Create Jupyter Custom Notebook 

## 참고자료 
custome image 생성 : 
https://www.kubeflow.org/docs/notebooks/custom-notebook/ 

notebook base image
https://github.com/jupyter/docker-stacks/tree/master/base-notebook

kubeflow tensorflow image
https://github.com/kubeflow/kubeflow/blob/master/components/tensorflow-notebook-image/Dockerfile


[example]
$ docker build -t apps . 
$ docker tag apps:latest gtno1chun/note-custom-image:1.0.0
$ docker push gtno1chun/note-custom-image:1.0.0 

## custom image download URL 
$ docker pull gtno1chun/note-custom-image:1.0.0
