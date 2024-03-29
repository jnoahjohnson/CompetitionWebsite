# Generated by Django 3.1.3 on 2020-12-14 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=40)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.competition')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authorization.competitor')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='completed_users',
            field=models.ManyToManyField(related_name='CompletedUsers', through='competitions.CompletedUsers', to='authorization.Competitor'),
        ),
    ]
