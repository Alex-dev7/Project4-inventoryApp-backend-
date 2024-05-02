# !/usr/bin/env bash

# exit on error
set -o errexit

## Install dependencies
pip install -r requirements.txt
# python3.9 manage.py collectstatic

## Run migrations in case any migrations hadn't been run yet
python manage.py migrate