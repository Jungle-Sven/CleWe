# CleWe
database:

docker-compose up -d

docker container app:

docker build -t my_app .

docker run --rm --network clewe_my_network -p 8080:80 my_app

flask running - http://127.0.0.1:8080/