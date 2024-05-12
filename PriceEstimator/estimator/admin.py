from django.contrib import admin
from .models import State, CityState, CityCodes

admin.site.register([State, CityState, CityCodes])