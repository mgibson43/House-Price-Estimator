import django
from pathlib import Path
from django.conf import settings

# Initialize django settings
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

from estimator.models import State, CityCode, CityState
import pandas as pd

# Clear objects from the database 
State.objects.all().delete()
CityState.objects.all().delete()
CityCode.objects.all().delete()

# Read in csv file
file_path = 'Data/city-state-data.csv'
df = pd.read_csv(file_path)

# Feed data row by row in to the models
def import_data(df):
  curr_state = None
  curr_city = None

  # Iterate through rows 
  for index, row in df.iterrows():
    
    # Feed current state into the state model
    State.objects.get_or_create(
        id=row['state'],
      )
    curr_state=State.objects.get(id=row['state'])

    # Feed the current city and state into the city state model
    CityState.objects.get_or_create(
        id=row['city'],
        state=curr_state,
      )
    curr_city=CityState.objects.get(id=row['city'])

    # Feed the current city and city code into the city code model
    CityCode.objects.get_or_create(
        id=row['city code'],
        city=curr_city
    )

import_data(df)