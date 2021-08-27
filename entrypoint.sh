#!/bin/sh
python manage.py migrate --no-input

python manage.py loaddata user_fixtures.json

python manage.py loaddata product_fixtures.json

python manage.py loaddata map_history_fixtures.json

python manage.py runserver 0.0.0.0:8000
