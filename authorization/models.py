from django.db import models

# Create your models here.


class Competitor(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    completed_competitions = models.ManyToManyField(
        'competitions.Competition', related_name='CompletedUsers', through='competitions.CompletedUsers')

    def __str__(self):
        return self.user.first_name
