from django.shortcuts import render
from django.http import JsonResponse
from .models import State,CityState
from .utils import createHouse, estateEstimation

def index(request):
  return render(request, 'estimator/index.html')

def getStates(request):
  stateValues = list(State.objects.order_by('id').values())
  return JsonResponse({'data':stateValues})

def getCities(request):
  cityValues = list(CityState.objects.values())
  return JsonResponse({'data':cityValues})

def getModels(request, *args, **kwargs):
  selectedState = kwargs.get('state')
  cities = list(CityState.objects.filter(state_id=selectedState).order_by('id').values())
  return JsonResponse({'data':cities})

def estimation(request):
  house = createHouse(request.POST.dict())
  estimation = estateEstimation(house)
  return render(request, 'estimator/estimation.html', {'estimation':estimation})