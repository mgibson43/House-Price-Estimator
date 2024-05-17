from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('state-json/', views.getStates, name='state-json'),
  path('city-json/', views.getCities, name='city-json'),
  path('models-json/<str:state>/', views.getModels, name='models-json'),
  path('estimation', views.estimation, name='estimation'),
]