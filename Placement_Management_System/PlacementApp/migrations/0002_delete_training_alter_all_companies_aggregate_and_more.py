# Generated by Django 4.1.4 on 2023-06-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.AlterField(
            model_name='all_companies',
            name='aggregate',
            field=models.FloatField(default=7.0),
        ),
        migrations.AlterField(
            model_name='all_companies',
            name='salary',
            field=models.IntegerField(default='30000'),
        ),
    ]
