# Generated by Django 4.1.4 on 2022-12-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0004_alter_all_companies_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_companies',
            name='branch',
            field=models.BooleanField(),
        ),
    ]