# Generated by Django 4.1.4 on 2023-05-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0030_registration_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration_com',
            old_name='student_name',
            new_name='student_usn',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='id',
        ),
        migrations.AlterField(
            model_name='all_companies',
            name='company_name',
            field=models.CharField(choices=[('sap', 'SAP'), ('Fivetran', 'FFIVETRAN'), ('JUNIPER NETWORKS', 'JUNIPER NETWORKS'), ('TARGET', 'TARGET'), ('MICROFOCUS', 'MICROFOCUS'), ('QUANTIPHY', 'QUANTIPHY'), ('DELL', 'DELL'), ('HP', 'HP'), ('IVANTHI', 'IVANTHI'), ('CALAYRA', 'CALAYRA'), ('FINFLUX', 'FINFLUX')], default='SAP', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='current_models',
            name='Current_Education_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='past_models',
            name='KCET_Rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='past_models',
            name='Past_Education_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='Contact_Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='USN',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]