from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)

class Competition(models.Model):
    name = models.CharField(max_length=20)
    tasks = models.ManyToManyField(Task)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.name

