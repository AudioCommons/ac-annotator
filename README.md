# music-annotator

Music annotator component.

**Note:** What's hosted here is work in progress, no functional component is provided yet.


# Development

The Audio Commons music annotator is a web service written in Python 3 using the Django framework. We use the PostgreSQL database backend with the JSON fields (PostgreSQL >= 9.2).

The easiest way to set up a local development version is to use Docker container definitions provided in this repository. Below you'll find instructions for setting up the development environment using Docker. You can also set up the development environment manually by installing all dependencies (including PostgreSQL and Redis). This works like a standard Django application but you'll have to manually connect all components. We do not provide instructions for manuall installation, but it should not be too complicated.


## Setting up dev environment

Before starting make sure you have [Docker](https://www.docker.com/products/overview)
(with `docker-compose`) installed.

- Clone repository and cd into it
```
git clone git@github.com:AudioCommons/ac-mediator.git
cd ac_mediator
```

- Build and run Docker containers for required services
```
docker-compose up
```

Now you should be able to access your server at `https://localhost:8000`


# License
Apache License 2.0

