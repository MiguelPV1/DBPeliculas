from django.shortcuts import render
from .models import Actor, Pelicula
from django.template.defaulttags import register

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


def index(request):
  movies = Pelicula.objects.all()
  
  movies_years = []
  for movie in movies:
    if movie.anio not in movies_years:
      movies_years.append(movie.anio)

  movies_years.sort()

  context = {'movies_years': movies_years}

  return render(request, "index.html", context)

def pelicula(request, year):
  movies = Pelicula.objects.filter(anio = year)

  context = {'movies': movies, 'year': year}

  return render(request, "pelicula.html", context)

def actores(request):
  actors = Actor.objects.all().order_by('nombre')

  movies_per_actor = {}
  for actor in actors:
    movies_per_actor[actor.nombre] = ", ".join(movie.nombre for movie in actor.peliculas.all())

  context = {'actors': actors, 'movies_per_actor': movies_per_actor}

  return render(request, "actores.html", context)
