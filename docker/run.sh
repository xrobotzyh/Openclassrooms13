#!/bin/bash

if [ "$RUN_MIGRATIONS" = "true" ]; then
    run python manage.py migrate
fi

python manage.py runserver 0.0.0.0:$PORT