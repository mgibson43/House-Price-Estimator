from django.contrib import admin
from .models import State, CityState, CityCode

admin.site.register([State, CityState, CityCode])