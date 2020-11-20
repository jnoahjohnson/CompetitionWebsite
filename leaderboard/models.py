from django.db import models

# Create your models here.

class Board (models.Model):
    competition = models.ForeignKey('competitions.Competition', on_delete=models.DO_NOTHING)
    group = models.ForeignKey('connectfriends.Group', on_delete=models.DO_NOTHING)