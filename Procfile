web: gunicorn PriceEstimator.wsgi --log-file -
python manage.py collectstatic --noinput
python manage.py makemigrations estimator
python manage.py migrate estimator
python import_data.py