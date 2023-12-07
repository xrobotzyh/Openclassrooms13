#!/bin/bash

#if [ "$RUN_MIGRATIONS" = "true" ]; then
#  render run python manage.py migrate
#fi
python manage.py dumpdata > data.json
python manage.py loaddata data.json
python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT