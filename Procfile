release: python manage.py makemigrations --noinput
release: python3 manage.py collectstatic --noinput
release: python manage.py migrate --noinput
web: gunicorn api.wsgi 