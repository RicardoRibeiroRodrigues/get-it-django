#!/usr/bin/env bash

# Install libaries
cd /home/ubuntu/
python3 -m venv env
source env/bin/activate
source .ENV_VARS
cd get-it-django
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input

# Restart gunicon
cd /home/ubuntu/
sudo ./start_gunicorn.sh

# Restart services
sudo service supervisor restart
sudo service nginx restart