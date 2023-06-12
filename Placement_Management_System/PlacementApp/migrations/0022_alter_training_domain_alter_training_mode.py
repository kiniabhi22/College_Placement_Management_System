# Generated by Django 4.1.4 on 2022-12-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0021_alter_all_companies_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='domain',
            field=models.CharField(choices=[('online', 'ONLINE'), ('offline', 'OFFLINE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='training',
            name='mode',
            field=models.CharField(choices=[('online', 'ONLINE'), ('offline', 'OFFLINE')], default='offline', max_length=10),
        ),
    ]
