web: gunicorn movie_universe.wsgi:application --log-file - --log-level debug
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate