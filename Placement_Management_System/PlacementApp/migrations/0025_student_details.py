# Generated by Django 4.1.4 on 2023-03-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0024_reg_com_remove_all_companies_branch1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Details',
            fields=[
                ('student_id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('USN', models.CharField(max_length=10)),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(blank=True, max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Branch', models.CharField(choices=[('CSE', 'cse'), ('ISE', 'ISE'), ('AIML', 'AIML'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MECHANICAL', 'MECH'), ('CIVIL', 'CIVIL'), ('ARCHITECTURE', 'ARCH')], default='CSE', max_length=15)),
                ('EMAIL', models.CharField(max_length=100)),
                ('Contact_Number', models.IntegerField(max_length=10)),
            ],
        ),
    ]