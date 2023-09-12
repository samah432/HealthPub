#!/bin/bash

rm db.sqlite3
rm -rf ./healthpubapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations healthpubapi
python3 manage.py migrate healthpubapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata customers
python3 manage.py loaddata employees
python3 manage.py loaddata appointments
python3 manage.py loaddata symptom_type