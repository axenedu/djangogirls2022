# pull official base image
FROM python:slim-bookworm


# install system dependencies
RUN apt-get update && apt-get install -y netcat-traditional

# create the django user
RUN addgroup --system django \
    && adduser --system --group django
USER django

#SET work directory
ENV HOME=/home/django
ENV PROJECT_NAME=project
ENV APP_HOME=$HOME/$PROJECT_NAME
WORKDIR $HOME
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=$HOME/${PROJECT_NAME}_venv

# create virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
#RUN chmod +x ${APP_HOME}/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/home/django/project/entrypoint.sh"]
