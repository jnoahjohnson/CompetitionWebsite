# Generated by Django 3.1.3 on 2020-12-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20201214_2214'),
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='completed_competitions',
            field=models.ManyToManyField(related_name='CompletedUsers', through='competitions.CompletedUsers', to='competitions.Competition'),
        ),
    ]