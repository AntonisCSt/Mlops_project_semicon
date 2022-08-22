
pipenv shell

docker compose up -d

sleep 5

pytest

docker-compose down

echo $?

sleep 4