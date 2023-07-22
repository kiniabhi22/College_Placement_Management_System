# Generated by Django 4.1.4 on 2023-06-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0004_alter_all_companies_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_companies',
            name='company_name',
            field=models.CharField(choices=[('SAP', 'SAP'), ('Fivetran', 'FFIVETRAN'), ('JUNIPER NETWORKS', 'JUNIPER NETWORKS'), ('TARGET', 'TARGET'), ('MICROFOCUS', 'MICROFOCUS'), ('QUANTIPHY', 'QUANTIPHY'), ('DELL', 'DELL'), ('HP', 'HP'), ('IVANTI', 'IVANTI'), ('KALEYRA', 'KALEYRA'), ('FINFLUX', 'FINFLUX'), ('Harman', 'Harman'), ('Target', 'Target'), ('Fedility', 'Fedility'), ('Persistent System', 'Persistent System'), ('Infosys', 'Infosys'), ('Wipro', 'Wipro'), ('TCS', 'TCS'), ('Avaya', 'Avaya'), ('TCS', 'TCS'), ('Toshiba', 'Toshiba'), ('Akamai Technologies', 'Akamai Technologies'), ('Intel', 'Intel'), ('Extreme Networks', 'Extreme Networks'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Energy Exemplar', 'Energy Exemplar')], default='SAP', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='USN',
            field=models.CharField(max_length=10),
        ),
    ]
