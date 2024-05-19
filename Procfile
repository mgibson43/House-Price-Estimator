web: gunicorn PriceEstimator.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py makemigrations estimator
python manage.py migrate estimator
python import_data.py