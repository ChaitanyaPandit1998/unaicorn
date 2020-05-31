from django.urls import path
from . import views

app_name='firstpage'
urlpatterns = [
  path('home/',views.index,name='index'),
  path('home/result/',views.result,name='result'),
]