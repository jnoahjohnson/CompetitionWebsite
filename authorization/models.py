from django.db import models

# Create your models here.
class Competitor(models.Model):
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=30)
    Avatar = models.ImageField()
    Date_Joined = models.DateField()
    Login_Attempts = models.IntegerField()

    def __str__(self):
        return self.Username