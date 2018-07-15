#/bin/bash

cd ~/.virtualenvs/
cd my-orchestrating-docker-v3-project/
docker-machine stop dev
docker-machine start dev
eval "$(docker-machine env dev)"
docker-compose build --no-cache --force-rm
docker volume rm $(docker volume ls -qf dangling=true)
docker-compose down --timeout 0
docker-compose up

#docker system prune
