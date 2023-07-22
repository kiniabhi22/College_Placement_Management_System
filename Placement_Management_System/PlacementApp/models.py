from django.db import models
from django.contrib.auth.models import User

#In below tuple, the what we mention in FIRST inverted comma will be shown on DISPLAY, SECOND will be shown on ADMIN PANEL

BRANCH=(
    ('CSE','cse'),
    ('ISE','ISE'),
    ('AIML','AIML'),
    ('ECE','ECE'),
    ('EEE','EEE'),
    ('MECHANICAL','MECH'),
    ('CIVIL','CIVIL'),
    ('ARCHITECTURE','ARCH')
)

SCHEME=(
    ('State','State'),
    ('CBSC','CBSC'),
    ('ICSC','ICSC')
)

class studentProfile(models.Model):
    USN=models.CharField(max_length=10, primary_key=True,unique=True)
    First_Name=models.CharField(max_length=100,blank=False)
    Middle_Name=models.CharField(max_length=100,blank=True)
    Last_Name=models.CharField(max_length=100,blank=False)
    Branch=models.CharField(max_length=15, choices=BRANCH, default='CSE',blank=False)
    EMAIL=models.CharField(max_length=100,blank=False)
    Contact_Number=models.IntegerField(blank=False)
    Tenth_Scheme=models.CharField(max_length=30,choices=SCHEME, default='State')
    Twelth_Scheme=models.CharField(max_length=30,choices=SCHEME, default='State')
    Tenth_Grade=models.FloatField(max_length=6,blank=False)
    Twelth_Grade=models.FloatField(max_length=6,blank=False)
    KCET_Rank=models.IntegerField(blank=False)  
    First_Sem_GPA=models.FloatField(max_length=10,blank=False)
    Second_Sem_GPA=models.FloatField(max_length=10,blank=False)
    Third_Sem_GPA=models.FloatField(max_length=10,blank=False)
    Fourth_Sem_GPA=models.FloatField(max_length=10,blank=False)

CATEGORY=(
    ('IT','IT'),
    ('CORE','CORE')
)

MODE=(
    ('ONLINE','ONLINE'),
    ('ONLINE','OFFLINE')
) 

COMPANY = (
    ('SAP','SAP'),
    ('Fivetran', 'FFIVETRAN'),
    ('JUNIPER NETWORKS','JUNIPER NETWORKS'),
    ('TARGET','TARGET'),
    ('MICROFOCUS','MICROFOCUS'),
    ('QUANTIPHY','QUANTIPHY'),
    ('DELL','DELL'),
    ('HP','HP'),
    ('IVANTI','IVANTI'),
    ('KALEYRA','KALEYRA'),
    ('FINFLUX','FINFLUX'),
    ('Harman','Harman'),
    ('Target','Target'),
    ('Fedility','Fedility'),
    ('Persistent System','Persistent System'),
    ('Infosys','Infosys'),
    ('Wipro','Wipro'),
    ('TCS','TCS'),
    ('Avaya','Avaya'),
    ('TCS','TCS'),
    ('Toshiba','Toshiba'),
    ('Akamai Technologies','Akamai Technologies'),
    ('Intel','Intel'),
    ('Extreme Networks','Extreme Networks'),
    ('Intel','Intel'),
    ('Intel','Intel'),
    ('Intel','Intel'),
    ('Energy Exemplar','Energy Exemplar')


)

class All_Companies(models.Model):
    ID=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=100,choices=COMPANY,default='SAP', blank=False)
    desc=models.TextField()
    branch=models.CharField(max_length=100)
    category=models.CharField(max_length=50,choices=CATEGORY,default='IT')
    salary=models.IntegerField(default="30000")
    stipend=models.IntegerField(default="30000")
    role=models.CharField(max_length=100)
    aggregate=models.FloatField(default=7.0)
    joblocation=models.CharField(max_length=100, default="Bangalore")
    dateofdrive=models.DateField()
    lastdate=models.DateField()

    def __str__(self):
        return self.company_name   #doubt: asdfghjklkgjtybc fbfbfrgsh
    
class Reg_Com(models.Model):
    ID=models.AutoField(primary_key=True)
    usn = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100,choices=COMPANY, unique=True, blank=False)
    desc=models.TextField()
    branch=models.CharField(max_length=100)
    category=models.CharField(max_length=50,choices=CATEGORY,default='IT')
    salary=models.IntegerField()
    stipend=models.IntegerField(default="30000")
    role=models.CharField(max_length=100)
    aggregate=models.FloatField(default=0.0)
    joblocation=models.CharField(max_length=100, default="Bangalore")
    dateofdrive=models.DateField(default=2022-11-11)

    def __str__(self):
        return self.company_name
    
PLACED=( 
    ('Yet To Be Placed','NOT PLACED'),
    ('Placed','PLACED')
)    
class StudentDetails(models.Model):
    ID=models.AutoField(primary_key=True)
    USN = models.CharField(max_length=10)
    company_name=models.CharField(max_length=100,choices=COMPANY, blank=False)
    category=models.CharField(max_length=50,choices=CATEGORY,default='IT')
    role=models.CharField(max_length=100)
    joblocation=models.CharField(max_length=100, default="Bangalore")

    def __str__(self):
        return self.USN

class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name