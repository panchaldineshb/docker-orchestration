mkvirtualenv -p /usr/bin/python3 my-orchestrating-docker-v4-project

http://containertutorials.com/docker-compose/flask-mongo-compose.html

docker-machine start dev

```
$ docker --version
Docker version 1.9.1, build a34a1d5
$ docker-machine --version
docker-machine version 0.14.0, build 89b8332
$ docker-compose --version
docker-compose version 1.22.0-rc1, build e7de1bc3
$ virtualenv --version
16.0.0
```

```
cd ~/.virtualenvs/
rmvirtualenv my-orchestrating-docker-v4-project
mkvirtualenv -p /usr/bin/python3 my-orchestrating-docker-v4-project
cd my-orchestrating-docker-v4-project/
workon my-orchestrating-docker-v4-project

```

```
cd ~/.virtualenvs/my-orchestrating-docker-v4-project/
touch app.py
touch docker-compose.yml
touch Dockerfile
touch requirements.txt
mkdir templates
touch templates/todo.html


docker-machine start dev
docker-machine ls
eval "$(docker-machine env dev)"
ls
docker-compose build
docker-compose up
docker-compose build
docker-machine start dev
eval "$(docker-machine env dev)"
docker-compose build
docker-compose up
docker-machine start dev
docker-compose build
docker-compose up
docker-machine start dev
docker-compose up
docker
docker-compose build --rm
docker-compose build --rm --force-rm
docker-compose build --force-rm
docker-compose up
```

```
cd .virtualenvs/
cd my-orchestrating-docker-v4-project/
workon my-orchestrating-docker-v4-project/
docker-machine start dev
eval "$(docker-machine env dev)"
docker-compose build --force-rm
docker volume rm $(docker volume ls -qf dangling=true)
docker-compose down --timeout 0
docker-compose up -d
```

```
docker-compose build --force-rm; docker-compose down; docker-compose up -d
```

```
https://realpython.com/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/
http://containertutorials.com/docker-compose/flask-mongo-compose.html


https://medium.com/dev-bits/deploying-cloud-services-applications-properly-with-docker-docker-compose-a4d9973a1953
https://medium.com/@devfire/how-to-become-a-devops-engineer-in-six-months-or-less-366097df7737


[Mail - dpanchal@USGA.org](https://outlook.office365.com/owa/?realm=USGA.org&exsvurl=1&ll-cc=2057&modurl=0&path=/mail/inbox "Mail - dpanchal@USGA.org")
[How to Dockerize your End-to-End acceptance tests – freeCodeCamp](https://medium.freecodecamp.org/how-to-dockerize-your-end-to-end-acceptance-tests-dbb593acb8e0 "How to Dockerize your End-to-End acceptance tests – freeCodeCamp")
[Smooth Local Development with Docker-Compose, Seeding, Stubs, and Faker](https://blog.philipphauer.de/local-development-docker-compose-seeding-stubs/ "Smooth Local Development with Docker-Compose, Seeding, Stubs, and Faker")
[GitHub - docker/compose: Define and run multi-container applications with Docker](https://github.com/docker/compose "GitHub - docker/compose: Define and run multi-container applications with Docker")
[Interpolate environment variables in docker-compose.yml · Issue #1377 · docker/compose · GitHub](https://github.com/docker/compose/issues/1377 "Interpolate environment variables in docker-compose.yml · Issue #1377 · docker/compose · GitHub")
[Docker Compose | Containerizing A MEAN Stack Application | Edureka](https://www.edureka.co/blog/docker-compose-containerizing-mean-stack-application/ "Docker Compose | Containerizing A MEAN Stack Application | Edureka")
[mongodb - How do I seed a mongo database using docker-compose? - Stack Overflow](https://stackoverflow.com/questions/31210973/how-do-i-seed-a-mongo-database-using-docker-compose "mongodb - How do I seed a mongo database using docker-compose? - Stack Overflow")
[Preferred way to run docker-compose in interactive mode - Docker for Windows - Docker Forums](https://forums.docker.com/t/preferred-way-to-run-docker-compose-in-interactive-mode/8450 "Preferred way to run docker-compose in interactive mode - Docker for Windows - Docker Forums")
[Using Docker Compose for Python Development - via @codeship | via @codeship](https://blog.codeship.com/using-docker-compose-for-python-development/ "Using Docker Compose for Python Development - via @codeship | via @codeship")
[Getting Started guide does not successfully get me started w/ docker-compose 1.7.0 / docker client+server 1.11.0, darwin/amd64 · Issue #3368 · docker/compose · GitHub](https://github.com/docker/compose/issues/3368 "Getting Started guide does not successfully get me started w/ docker-compose 1.7.0 / docker client+server 1.11.0, darwin/amd64 · Issue #3368 · docker/compose · GitHub")
[Flask on Docker](http://192.168.99.100:5000/ "Flask on Docker")
[HTTPie 0.9.8 (latest) documentation](https://httpie.org/doc#examples "HTTPie 0.9.8 (latest) documentation")
[docker up rm at DuckDuckGo](https://duckduckgo.com/?q=docker+up+rm&t=lm&atb=v124-6&ia=web "docker up rm at DuckDuckGo")
[GitHub - chadoe/docker-cleanup-volumes: Shellscript to delete orphaned docker volumes](https://github.com/chadoe/docker-cleanup-volumes "GitHub - chadoe/docker-cleanup-volumes: Shellscript to delete orphaned docker volumes")
[Theming Bootstrap · Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/theming/ "Theming Bootstrap · Bootstrap")

```
