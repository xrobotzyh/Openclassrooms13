#!/bin/bash

if [ "$RUN_MIGRATIONS" = "true" ]; then
    python manage.py migrate
fi

python manage.py runserver 0.0.0.0:$PORT