#!/bin/bash

if [ "$RUN_MIGRATIONS" = "true" ]; then
  python manage.py migrate
fi

if [ "$RUN_COLLECTSTATIC" = "true" ]; then
  python manage.py collectstatic --noinput
fi
python manage.py runserver 0.0.0.0:$PORT