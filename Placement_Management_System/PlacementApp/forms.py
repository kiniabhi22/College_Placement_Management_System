from django import forms
from django.forms import ModelForm
from .models import Registration_com

class company_reg(ModelForm):
    class Meta:
        model= Registration_com
        fields=('student_usn','company_name')  #('student_usn','company_name','date_drive')#if we are not selecting all the fields fron the model and few out of it, then we write code as followed "fields=('field1','field2','field3',...)"
        