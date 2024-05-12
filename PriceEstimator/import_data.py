import django
from pathlib import Path
from django.conf import settings

settings.configure(
  SECRET_KEY = 'django-insecure-whmkd_j%nd0w9qjbzhe)l7lich^ip$1q+i$_@rz(3d2i9tky_)',

  DEBUG=True,

  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'estimator',
    'pandas',
  ],

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
  },
)

django.setup()

from estimator.models import State, CityCodes, CityState
import pandas as pd

State.objects.all().delete()
CityState.objects.all().delete()
CityCodes.objects.all().delete()

file_path = '../Data/city-state-data.csv'
df = pd.read_csv(file_path)

def import_data(df):
  curr_state = None
  curr_city = None
  for index, row in df.iterrows():
    print(index)
    State.objects.get_or_create(
        state=row['state'],
      )

    print(State.objects.get(state=row['state']))
    curr_state=State.objects.get(state=row['state'])

    CityState.objects.get_or_create(
        city=row['city'],
        state=curr_state,
      )
    curr_city=CityState.objects.get(city=row['city'])

    CityCodes.objects.get_or_create(
        code=row['city code'],
        city=curr_city
    )

import_data(df)