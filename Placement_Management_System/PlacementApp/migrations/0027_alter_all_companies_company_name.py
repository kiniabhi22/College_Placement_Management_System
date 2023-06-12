# Generated by Django 4.1.4 on 2023-05-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0026_current_models_past_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_companies',
            name='company_name',
            field=models.CharField(choices=[('sap', 'SAP'), ('Fivetran', 'FFIVETRAN'), ('JUNIPER NETWORKS', 'JUNIPER NETWORKS'), ('TARGET', 'TARGET'), ('MICROFOCUS', 'MICROFOCUS'), ('QUANTIPHY', 'QUANTIPHY'), ('DELL', 'DELL'), ('HP', 'HP'), ('IVANTHI', 'IVANTHI'), ('CALAYRA', 'CALAYRA'), ('FINFLUX', 'FINFLUX')], default='SAP', max_length=100),
        ),
    ]
