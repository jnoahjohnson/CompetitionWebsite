# Generated by Django 3.1.3 on 2020-12-14 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competition_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.competitioncategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='authorization.competitor'),
            preserve_default=False,
        ),
    ]
