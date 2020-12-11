from django.db import models

# Create your models here.

class LeaderBoard (models.Model):
    competition = models.ForeignKey('competitions.Competition', on_delete=models.DO_NOTHING)
