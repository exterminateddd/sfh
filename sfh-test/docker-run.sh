docker stop sfh-c
docker rm sfh-c

. fix-env.sh

docker build -t sfh .
docker run -p 8080:80 -d --name sfh-c sfh

docker network connect sfh-nw sfh-c
