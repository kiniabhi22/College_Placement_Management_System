# Generated by Django 4.1.4 on 2023-05-09 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0037_delete_registration_com'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_Com',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_drive', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlacementApp.all_companies')),
                ('student_usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlacementApp.student_details')),
            ],
        ),
    ]