# Generated by Django 3.1.3 on 2020-11-20 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=30)),
                ('Avatar', models.ImageField(upload_to='')),
                ('Date_Joined', models.DateField()),
                ('Login_Attempts', models.IntegerField()),
            ],
        ),
    ]