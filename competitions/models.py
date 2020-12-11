from django.db import models

# Create your models here.
class CompletedUsers(models.Model):
    user_name = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.user_name

class Competition(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    points = models.IntegerField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    completed = models.ManyToManyField(CompletedUsers)

    def __str__(self):
        return self.name




