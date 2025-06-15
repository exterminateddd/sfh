docker stop sfh-flask-c
docker rm sfh-flask-c

docker build -t sfh-flask . --network=host
docker run -p 5000:5000 -d --name sfh-flask-c sfh-flask

docker network connect sfh-nw sfh-flask-c
