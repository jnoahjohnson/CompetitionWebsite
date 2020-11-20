from django.db import models

# Create your models here.
class Leaderboard(models.Model) :
    competition = models.ForeignKey('competitions.competition', on_delete=models.DO_NOTHING)
    group = models.ForeignKey('connectfriends.group', on_delete=models.DO_NOTHING)

    def __str__(self):
        return (self.competition.name)  