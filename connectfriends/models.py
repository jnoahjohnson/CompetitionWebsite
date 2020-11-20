from django.db import models

# Create your models here.
class Group(models.Model):
    Groupname = models.CharField(max_length=30)
    Username = models.ManyToManyField('leaderboard.User')

    def __str__(self):
        return self.GroupName

