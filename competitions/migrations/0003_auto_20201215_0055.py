# Generated by Django 3.1.3 on 2020-12-15 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20201214_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='competition_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.competitioncategory'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]