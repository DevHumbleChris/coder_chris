web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn coder_chris.wsgi
release: python manage.py migrate
