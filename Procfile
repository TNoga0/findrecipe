release: python3 manage.py migrate
web: python3 manage.py collectstatic --noinput
web: gunicorn fridge_reciper.wsgi