# Celery

## Description 
Trying celery's get started.
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps

## Development
This project was developed on Linux Ubuntu 21.04. See the Dockerfile apt-get install command to get the list of packages you will need to have installed for the requirements to be installed successfully.

Then, we recommend installing pyenv and pyenv-virtualenv, install python 3.8.0 on it and then create a pyenv virtualenv with this python version.

## Development Environment
### Database

#### Installing requirements

```bash
  pip install -r requirements.txt
```

#### Up the rabbitmq container (broker)

```bash
  docker run -d -p 5672:5672 rabbitmq
```

#### Run celery's worker server

```bash
  celery -A tasks worker --loglevel=INFO
```

#### You can use flower to see the same informations but out of terminal

```bash
  celery flower -A tasks
```