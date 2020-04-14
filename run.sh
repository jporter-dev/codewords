if [[ $1 = dev* ]];
then
echo 'development'
  docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build
else
echo 'production'
  docker-compose -f docker-compose.yml -f docker-compose.production.yml up --build -d
fi
