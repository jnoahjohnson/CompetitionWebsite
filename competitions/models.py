from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    point_value = models.IntegerField()

    def __str__(self):
        return self.title

class Competition(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    rules = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    group = models.ForeignKey('connectfriends.Group', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class UserTask(models.Model):
    task_date = models.DateField()
    task_completed = models.BooleanField()
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    competition = models.ForeignKey(Competition, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.task.title



