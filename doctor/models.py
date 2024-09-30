from django.db import models

class Direction(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    directions = models.ManyToManyField(Direction)
    description = models.TextField()
    birth_date = models.DateField()
    experience = models.PositiveIntegerField()
    sort_order = models.IntegerField()

    def __str__(self):
        return self.name
