git pull
docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d --no-deps --build flask frontend
