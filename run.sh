if [[ $1 = dev* ]];
then
  docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build
else
  docker-compose -f docker-compose.yml -f docker-compose.production.yml up --build
fi
