#!/bin/sh

#ls -la /home/django/mysite_venv/bin
#source /home/django/mysite_venv/bin/activate

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"
