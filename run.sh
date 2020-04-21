if [[ $1 = prod* ]];
then
  echo 'production'
  docker-compose -f docker-compose.yml -f docker-compose.production.yml up --build -d
else
  echo 'development'
  docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build
fi
