from django.db import models

# Create your models here.


class CompetitionCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CompletedUsers(models.Model):
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE)
    competitor = models.ForeignKey(
        'authorization.Competitor', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Competition(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    points = models.IntegerField()
    creator = models.ForeignKey('authorization.Competitor',
                                on_delete=models.DO_NOTHING)
    completed_users = models.ManyToManyField(
        'authorization.Competitor', through='CompletedUsers', related_name="CompletedUsers")
    competition_category = models.ForeignKey(
        'CompetitionCategory', on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.name
