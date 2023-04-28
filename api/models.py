from django.db import models

class Actor(models.Model):
  nombre           = models.CharField(max_length=30)
  fecha_nacimiento = models.DateField()
  
  def __unicode__(self):
    return self.nombre

class Pelicula(models.Model):
  nombre    = models.CharField(max_length=60)
  anio      = models.IntegerField()
  actores   = models.ManyToManyField(Actor, related_name='peliculas')
  
  def __unicode__(self):
    return self.nombre
