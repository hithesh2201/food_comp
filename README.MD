# commands need to run in a vm to start the flask app
sudo su \
yum-config-manager -y --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
yum install docker-ce -y \
systemctl start docker \
git clone https://github.com/hithesh2201/food_comp.git \
cd food_comp \
docker build -t app . \
docker run -p 80:5000 app 