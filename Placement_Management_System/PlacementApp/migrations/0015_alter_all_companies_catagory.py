# Generated by Django 4.1.4 on 2022-12-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0014_alter_training_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_companies',
            name='catagory',
            field=models.CharField(choices=[('it', 'IT'), ('core', 'CORE')], default='IT', max_length=50),
        ),
    ]