# music-annotator

Music annotator component.

**Note:** What's hosted here is work in progress, no functional component is provided yet.
The music annotator is available directly from `http://localhost:8000`.
You will be able to choose a sound, and then be directed to a page to annotate it.

# annotator

Annotation tool which enable users to generate labels from the AudioSet Ontology to Freesound clips.
You cann access it at for instance from: `http://localhost:8000/generate_annotations/36/`, where the last integer is a Freesound sound id.
Another more extented version can be found at this repository branch: `https://github.com/MTG/freesound-datasets/tree/annotation-tools-FRUCT2018`.


# Development

The Audio Commons Annotator is a web service written in Python 3 using the Django framework. 

The easiest way to set up a local development version is to use Docker container definitions provided in this repository. Below you'll find instructions for setting up the development environment using Docker. We do not provide instructions for manuall installation, but it should not be too complicated.


## Setting up dev environment

Before starting make sure you have [Docker](https://www.docker.com/products/overview)
(with `docker-compose`) installed.

- Clone repository and cd into it
```
git clone git@github.com:AudioCommons/ac-annotator.git
cd ac_annotator
```

- Build and run Docker containers for required services
```
docker-compose up
```

Now you should be able to access your server at `http://localhost:8000`


# License
Apache License 2.0

