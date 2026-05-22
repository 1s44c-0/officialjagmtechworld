#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
pip install cloudinary 
pip install django-cloudinary-storage 
pip install Pillow
