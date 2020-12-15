# Generated by Django 3.1.3 on 2020-12-15 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_competitor_completed_competitions'),
        ('competitions', '0003_auto_20201215_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedusers',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competition'),
        ),
        migrations.AlterField(
            model_name='completedusers',
            name='competitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorization.competitor'),
        ),
    ]
