### Steps to setup the backend

1. cd backend
2. source .venv/bin/activate
3. pip install django [one-time]
4. django-admin startproject pdf_extractor .
5. python manage.py startapp api
6. Test the development server - python manage.py runserver


### Setup the APIs
1. Install Django Rest Framework - pip install djangorestframework
2. Migrate the DB - python manage.py makemigrations and python manage.py migrate
3. Create a superuser - python manage.py createsuperuser
4. Optional - Create regular users from /admin


### Notes -
1. This project doesn't actually create a RESTful API, but just mimics the workflow in classic django views. Same can be built in the RESTful API(s) using serializers and JsonResponse, but the overall workflow still remains the same.

This is primarily done to _
 - reduce the effort for building the frontend exclusively in React/Next/Vue etc.
 - It gets out of scope for the job role to build the frontend.