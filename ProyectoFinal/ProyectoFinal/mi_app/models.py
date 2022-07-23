from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class Profesional(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class Desempleado(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()