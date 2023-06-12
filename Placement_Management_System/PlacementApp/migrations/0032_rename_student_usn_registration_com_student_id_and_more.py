# Generated by Django 4.1.4 on 2023-05-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0031_rename_student_name_registration_com_student_usn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration_com',
            old_name='student_usn',
            new_name='student_id',
        ),
        migrations.AlterField(
            model_name='student_details',
            name='USN',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
