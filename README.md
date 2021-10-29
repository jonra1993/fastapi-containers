# fastapi-containers

## Clone

Please run the following commands.

```
git clone https://github.com/jonra1993/fastapi-containers.git
cd fastapi-containers
```

## Docker Compose

This repo is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 80. It uses FastAPI Python async backend and Nginx as reverse proxy.

```sh
docker-compose up
```

Open a browser and go to http://localhost/docs, you should see a screen of Swagger documentation.

![Fast API - docker](https://res.cloudinary.com/dnv0qwkrk/image/upload/v1625416683/wordpress_JRTEC/doc_yvpzob.png)

To stop containers run:

```sh
docker-compose down
```


# Docker should increse the RAM from 2 to 4

# Windows Command line
docker run --network=fastapi-containers_default --rm -e SONAR_HOST_URL="http://sonarqube-container-fast:9000" -e SONAR_LOGIN="71d9eb1ba1eaa52691ed530a90a8a33a7e32f15d" -v "%cd%:/usr/src" sonarsource/sonar-scanner-cli

# Windows Command line
docker run --network=fastapi-containers_default --rm -e SONAR_HOST_URL="http://sonarqube-container-fast:9000" -e SONAR_LOGIN="71d9eb1ba1eaa52691ed530a90a8a33a7e32f15d" -v "${PWD}:/usr/src" sonarsource/sonar-scanner-cli

# Mac and Linux
docker run --network=fastapi-containers_default --rm -e SONAR_HOST_URL="http://sonarqube-container-fast:9000" -e SONAR_LOGIN="71d9eb1ba1eaa52691ed530a90a8a33a7e32f15d" -v "$(pwd):/usr/src" sonarsource/sonar-scanner-cli

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Created by <a href="https://www.jonathanvargas.ml" target="_blank">Jonathan Vargas</a>


