# scratchpay-john-test
scratchpay-api-docker-microk8s-kubernetes

##

ll
total 588676
drwxrwxr-x  2 john john      4096 May 24 18:12 ./
drwxrwxr-x 13 john john      4096 May 24 18:49 ../
-rw-rw-r--  1 john john 602777600 May 24 18:12 api-scratchpay.tar   # not added in GIT 
-rw-rw-r--  1 john john      1897 May 24 17:56 app.py
-rw-rw-r--  1 john john       119 May 24 15:01 data.csv
-rw-rw-r--  1 john john       312 May 24 17:55 Dockerfile
################################################################
Explaining the files .  
app.py   ==  API application file.  
data.csv ==  data storage in csv  for get and post. 
Dockerfile  == Docker file for creating Docker image. 

api-scratchpay.tar ==  docker image in tar file for adding to  microk8s image list. 
###  Not added in GIT  repo size issue 



https://microk8s.io/docs/getting-started

####  to save Docker image to  .tar file 
docker save mynginx > myimage.tar
#####  to add Docker tar file to microk8s image  list  
microk8s ctr image import myimage.tar



sudo microk8s  kubectl get pods --all-namespaces
NAMESPACE     NAME                                        READY   STATUS    RESTARTS      AGE
kube-system   dashboard-metrics-scraper-7bc864c59-kn4q4   1/1     Running   3 (39m ago)   29d
kube-system   kubernetes-dashboard-dc96f9fc-bxsfk         1/1     Running   5 (39m ago)   29d
kube-system   calico-node-fvnvj                           1/1     Running   1 (39m ago)   24d
kube-system   calico-kube-controllers-54675f9875-2zdm7    1/1     Running   1 (39m ago)   24d
kube-system   metrics-server-6f754f88d-6bps4              1/1     Running   3 (39m ago)   29d
default       scratchpayapi-5ddb86bd7b-k8qqs              1/1     Running   0             2m37s
john@Ubuntu18:~/Vimal/MicroK8s$ sudo microk8s  kubectl get pods --all-namespaces


###scratchpayapi-5ddb86bd7b-k8qqs  

########-----------------------------------------------------------------

