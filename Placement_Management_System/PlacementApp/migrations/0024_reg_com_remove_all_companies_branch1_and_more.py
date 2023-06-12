# Generated by Django 4.1.4 on 2023-01-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementApp', '0023_alter_all_companies_catagory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg_Com',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('branch', models.CharField(max_length=5)),
                ('catagory', models.CharField(choices=[('IT', 'IT'), ('CORE', 'CORE')], default='IT', max_length=50)),
                ('salary', models.IntegerField()),
                ('stipend', models.IntegerField(default='30000')),
                ('role', models.CharField(max_length=100)),
                ('aggregate', models.FloatField(default=0.0)),
                ('joblocation', models.CharField(default='Bangalore', max_length=100)),
                ('dateofdrive', models.DateField(default=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch1',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch2',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch3',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch4',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch5',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch6',
        ),
        migrations.RemoveField(
            model_name='all_companies',
            name='branch7',
        ),
        migrations.AddField(
            model_name='all_companies',
            name='branch',
            field=models.CharField(default='CSE', max_length=5),
        ),
    ]
