git pull
if [[ $* ]];
then
  docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d --no-deps --build $*
else
  docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d --no-deps --build flask frontend
fi
