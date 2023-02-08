### Welcome

This repository shows you how to handle static files.
This is not for production use.

In order to use the repo perform the following steps.

``` bash
git clone https://github.com/r3ap3rpy/django-imaginerium.git
virtualenv djangoinv
djangoinv\Scripts\activate.bat
pip install django
cd django-imaginerium
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```