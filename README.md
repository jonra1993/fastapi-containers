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


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Created by <a href="https://www.jonathanvargas.ml" target="_blank">Jonathan Vargas</a>


