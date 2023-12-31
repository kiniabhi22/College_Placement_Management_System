# Generated by Django 4.1.4 on 2023-06-30 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Companies',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(choices=[('-', 'notplaced'), ('SAP', 'SAP'), ('Fivetran', 'FFIVETRAN'), ('JUNIPER NETWORKS', 'JUNIPER NETWORKS'), ('TARGET', 'TARGET'), ('MICROFOCUS', 'MICROFOCUS'), ('QUANTIPHY', 'QUANTIPHY'), ('DELL', 'DELL'), ('HP', 'HP'), ('IVANTI', 'IVANTI'), ('KALEYRA', 'KALEYRA'), ('FINFLUX', 'FINFLUX'), ('Harman', 'Harman'), ('Target', 'Target'), ('Fedility', 'Fedility'), ('Persistent System', 'Persistent System'), ('Infosys', 'Infosys'), ('Wipro', 'Wipro'), ('TCS', 'TCS'), ('Avaya', 'Avaya'), ('TCS', 'TCS'), ('Toshiba', 'Toshiba'), ('Akamai Technologies', 'Akamai Technologies'), ('Intel', 'Intel'), ('Extreme Networks', 'Extreme Networks'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Energy Exemplar', 'Energy Exemplar')], default='SAP', max_length=100, unique=True)),
                ('desc', models.TextField()),
                ('branch', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('IT', 'IT'), ('CORE', 'CORE')], default='IT', max_length=50)),
                ('salary', models.IntegerField()),
                ('stipend', models.IntegerField(default='30000')),
                ('role', models.CharField(max_length=100)),
                ('aggregate', models.FloatField(default=0.0)),
                ('joblocation', models.CharField(default='Bangalore', max_length=100)),
                ('dateofdrive', models.DateField()),
                ('lastdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='resumes/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('USN', models.CharField(max_length=10, unique=True)),
                ('company_name', models.CharField(choices=[('-', 'notplaced'), ('SAP', 'SAP'), ('Fivetran', 'FFIVETRAN'), ('JUNIPER NETWORKS', 'JUNIPER NETWORKS'), ('TARGET', 'TARGET'), ('MICROFOCUS', 'MICROFOCUS'), ('QUANTIPHY', 'QUANTIPHY'), ('DELL', 'DELL'), ('HP', 'HP'), ('IVANTI', 'IVANTI'), ('KALEYRA', 'KALEYRA'), ('FINFLUX', 'FINFLUX'), ('Harman', 'Harman'), ('Target', 'Target'), ('Fedility', 'Fedility'), ('Persistent System', 'Persistent System'), ('Infosys', 'Infosys'), ('Wipro', 'Wipro'), ('TCS', 'TCS'), ('Avaya', 'Avaya'), ('TCS', 'TCS'), ('Toshiba', 'Toshiba'), ('Akamai Technologies', 'Akamai Technologies'), ('Intel', 'Intel'), ('Extreme Networks', 'Extreme Networks'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Energy Exemplar', 'Energy Exemplar')], max_length=100, unique=True)),
                ('category', models.CharField(choices=[('IT', 'IT'), ('CORE', 'CORE')], default='IT', max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('joblocation', models.CharField(default='Bangalore', max_length=100)),
                ('placed', models.CharField(choices=[('Yet To Be Placed', 'NOT PLACED'), ('Placed', 'PLACED')], default=1, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='studentProfile',
            fields=[
                ('USN', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(blank=True, max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Branch', models.CharField(choices=[('CSE', 'cse'), ('ISE', 'ISE'), ('AIML', 'AIML'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MECHANICAL', 'MECH'), ('CIVIL', 'CIVIL'), ('ARCHITECTURE', 'ARCH')], default='CSE', max_length=15)),
                ('EMAIL', models.CharField(max_length=100)),
                ('Contact_Number', models.IntegerField()),
                ('Tenth_Scheme', models.CharField(choices=[('State', 'State'), ('CBSC', 'CBSC'), ('ICSC', 'ICSC')], default='State', max_length=30)),
                ('Twelth_Scheme', models.CharField(choices=[('State', 'State'), ('CBSC', 'CBSC'), ('ICSC', 'ICSC')], default='State', max_length=30)),
                ('Tenth_Grade', models.FloatField(max_length=6)),
                ('Twelth_Grade', models.FloatField(max_length=6)),
                ('KCET_Rank', models.IntegerField()),
                ('First_Sem_GPA', models.FloatField(max_length=10)),
                ('Second_Sem_GPA', models.FloatField(max_length=10)),
                ('Third_Sem_GPA', models.FloatField(max_length=10)),
                ('Fourth_Sem_GPA', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('sponsor', models.CharField(max_length=50)),
                ('domain', models.CharField(choices=[('IT', 'IT'), ('CORE', 'CORE')], max_length=50)),
                ('eligible_branch', models.CharField(max_length=50)),
                ('mode', models.CharField(choices=[('ONLINE', 'ONLINE'), ('ONLINE', 'OFFLINE')], default='offline', max_length=10)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('duration', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reg_Com',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(choices=[('-', 'notplaced'), ('SAP', 'SAP'), ('Fivetran', 'FFIVETRAN'), ('JUNIPER NETWORKS', 'JUNIPER NETWORKS'), ('TARGET', 'TARGET'), ('MICROFOCUS', 'MICROFOCUS'), ('QUANTIPHY', 'QUANTIPHY'), ('DELL', 'DELL'), ('HP', 'HP'), ('IVANTI', 'IVANTI'), ('KALEYRA', 'KALEYRA'), ('FINFLUX', 'FINFLUX'), ('Harman', 'Harman'), ('Target', 'Target'), ('Fedility', 'Fedility'), ('Persistent System', 'Persistent System'), ('Infosys', 'Infosys'), ('Wipro', 'Wipro'), ('TCS', 'TCS'), ('Avaya', 'Avaya'), ('TCS', 'TCS'), ('Toshiba', 'Toshiba'), ('Akamai Technologies', 'Akamai Technologies'), ('Intel', 'Intel'), ('Extreme Networks', 'Extreme Networks'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Intel', 'Intel'), ('Energy Exemplar', 'Energy Exemplar')], max_length=100, unique=True)),
                ('desc', models.TextField()),
                ('branch', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('IT', 'IT'), ('CORE', 'CORE')], default='IT', max_length=50)),
                ('salary', models.IntegerField()),
                ('stipend', models.IntegerField(default='30000')),
                ('role', models.CharField(max_length=100)),
                ('aggregate', models.FloatField(default=0.0)),
                ('joblocation', models.CharField(default='Bangalore', max_length=100)),
                ('dateofdrive', models.DateField(default=2000)),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
