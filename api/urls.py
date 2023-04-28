from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [    
    path('', index, name="index"),
    path('pelicula/<int:year>', pelicula, name="pelicula"),
    path('actores/', actores, name="actores"),
]