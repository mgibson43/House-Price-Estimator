from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Model
from .models import State,CityState,CityCode

def index(request):
  states = State.objects.all()
  cities = CityState.objects.all()
  codes = CityCode.objects.all()
  
  return render(request, 'estimator/index.html', {'states' : states, 'cities' : cities, 'codes': codes})

def getStates(request):
  stateValues = list(State.objects.order_by('id').values())
  print(stateValues)
  return JsonResponse({'data':stateValues})

def getCities(request):
  cityValues = list(CityState.objects.values())
  return JsonResponse({'data':cityValues})

def getModels(request, *args, **kwargs):
  selectedState = kwargs.get('state')
  cities = list(CityState.objects.filter(state_id=selectedState).order_by('id').values())
  return JsonResponse({'data':cities})