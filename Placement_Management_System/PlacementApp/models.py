from django.db import models
# from django import forms
# from django.contrib.auth.models import User

# Create your models here.

# BRANCH_CHOICES = (
#     ('cse','CSE'),
#     ('ise', 'ISE'),
#     ('aiml','AIML'),
#     ('ece','ECE'),
#     ('eee','EEE'),
#     ('mech','MECHANICAL'),
#     ('civil','CIVIL')
# )

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
  
    # Current_Education_Details=models.ForeignKey(max_length=100,blank=False)
    # Past_Education_Details=models.ForeignKey(max_length=100,blank=False)
    # Other_Details=models.ForeignKey(max_length=100,blank=False)

CATAGORY=(
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
    company_name=models.CharField(max_length=100,choices=COMPANY,default='SAP', unique=True, blank=False)
    desc=models.TextField()
    branch=models.CharField(max_length=100)
    catagory=models.CharField(max_length=50,choices=CATAGORY,default='IT')
    salary=models.IntegerField()
    stipend=models.IntegerField(default="30000")
    role=models.CharField(max_length=100)
    aggregate=models.FloatField(default=0.0)
    joblocation=models.CharField(max_length=100, default="Bangalore")
    dateofdrive=models.DateField()
    lastdate=models.DateField()

    def __str__(self):
        return self.company_name   #doubt: asdfghjklkgjtybc fbfbfrgsh
    
class Reg_Com(models.Model):
    ID=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=100,choices=COMPANY, unique=True, blank=False)
    desc=models.TextField()
    branch=models.CharField(max_length=100)
    catagory=models.CharField(max_length=50,choices=CATAGORY,default='IT')
    salary=models.IntegerField()
    stipend=models.IntegerField(default="30000")
    role=models.CharField(max_length=100)
    aggregate=models.FloatField(default=0.0)
    joblocation=models.CharField(max_length=100, default="Bangalore")
    dateofdrive=models.DateField(default=2022-11-11)

    def __str__(self):
        return self.company_name

    
class Training(models.Model):
    course_name=models.CharField(max_length=50)
    sponsor=models.CharField(max_length=50)
    domain=models.CharField(max_length=50,choices=CATAGORY)
    eligible_branch=models.CharField(max_length=50)
    mode=models.CharField(max_length=10,choices=MODE,default='offline')
    location=models.CharField(max_length=50, blank=True)
    duration=models.IntegerField()
    fee=models.IntegerField()

# class Reg_Com(models.Model):
#      reg_company_name=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_desc=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_branch=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_category=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_salary=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_stipend=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_role=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_aggregate=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_job_location=models.ForeignKey(All_Companies,on_delete=models.CASCADE)
#      reg_dateofdrive=models.ForeignKey(All_Companies,on_delete=models.CASCADE)

# class Registration_com(models.Model):
#     student_usn = models.ForeignKey(Student_Details, on_delete=models.CASCADE)
#     company_name = models.ForeignKey(All_Companies, on_delete=models.CASCADE)
#     date_drive = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student_usn} registered for {self.company_name} on {self.date_drive}"
