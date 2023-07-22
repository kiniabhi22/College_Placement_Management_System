from django.shortcuts import render,redirect
#to be added
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

def job_search(request):
    print("im inside")
    query = requests.get('http://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=689f1d48&app_key=fe3754cf6140d0d631fffbd04b1c707d&results_per_page=20&what=javascript%20developer&content-type=application/json').json()
    print(query)
    return render(request, 'getJob.html', {'job_results': query})

# def job_search(request):
#     print("I'm inside")
#     api_url = 'http://api.adzuna.com/v1/api/jobs/gb/search/1'
#     api_params = {
#         'app_id': 'a9637649',
#         'app_key': '3d5f86d6e2e80e0df942c1561a86de36',
#         'results_per_page': 30,
#         'what': 'javascript developer',
#         'where': 'uk',
#     }
#     query = requests.get(api_url, params=api_params)
#     return render(request, 'getJob.html', {'job_results': query})


def dashboard(request):
    details=StudentDetails.objects.all()
    return render(request,'dashboard.html',{'deets':details})

def company_reg(request):
        registeredCompanies = Reg_Com.objects.all()
        current_date = timezone.now().date()
        companies = All_Companies.objects.exclude(Q(company_name__in=Reg_Com.objects.all().values_list('company_name', flat=True)) | Q(lastdate__lt=current_date))
        return render(request, 'company_reg.html', {'companies': companies,'regcompanies':registeredCompanies})

@login_required
def reg_com(request):
        if request.method=='POST':
            if 'deRegister' in request.POST:
                id = request.POST.get('deRegister')
                selected_company = Reg_Com.objects.get(ID=id)
                print(request.method)
                selected_company.delete() 
                registeredCompanies = Reg_Com.objects.all()
                return render(request, 'reg_com.html', {'companies': registeredCompanies})
            id = request.POST.get('register')
            selected_company = All_Companies.objects.get(ID=id)
            obj=Reg_Com.objects.create(
                    usn=request.user,
                    company_name=selected_company.company_name,
                    desc=selected_company.desc,
                    branch=selected_company.branch,
                    category=selected_company.category,
                    salary=selected_company.salary,
                    stipend=selected_company.stipend,
                    role=selected_company.role,
                    aggregate=selected_company.aggregate,
                    joblocation=selected_company.joblocation,
                    dateofdrive=selected_company.dateofdrive
                )
            obj.save()
            registeredCompanies=Reg_Com.objects.all()
            search_query = request.GET.get('search')
            if search_query:
                registeredCompanies = registeredCompanies.filter(usn__icontains=search_query)
            return render(request,'reg_com.html',{'companies':registeredCompanies})
        
        else:
            registeredCompanies = Reg_Com.objects.all()
            return render(request,'reg_com.html',{'companies':registeredCompanies})
        
@login_required
def all_companies(request):
    obj=All_Companies.objects.all()  #all_com.objects.get(usn=user.usn)
    return render(request,'all_com.html',{'companies':obj})

@login_required
def studProfile(request):
    details=studentProfile.objects.all()
    return render(request,'profile.html',{'detail':details})

@login_required
def uploadResume(request):
    if request.method == 'POST':
        name = request.POST['name']
        file = request.FILES['resume_file']
        resume = Resume(name=name, file=file)
        resume.save()
        return redirect('viewResume', resume_id=resume.id)
    return render(request, 'uploadResume.html')

@login_required
def viewResume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'viewResume.html', {'resume': resume})

def studentDetails(request):
    details=StudentDetails.objects.all()
    return render(request,'students.html',{'deets':details})

@csrf_exempt
def signin(request):
     if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        User=authenticate(request,username=username,password=password)
        if(User is not None):
            auth.login(request,User)
            messages.info(request,("You have successfully logged in..."))
            return redirect('/')
        else:
            messages.info(request,("There is some error in Username oe Password. Please try again..."))
            return redirect('signin')
     else:
      return render(request,'signin.html')

def signout(request):
     auth.logout(request)
     messages.info(request,("You are now logged out of the portal..."))
     return redirect('/')

@csrf_exempt
def signup(request):
     if request.method == 'POST':
        user_name=request.POST.get('username')
        contact_no=request.POST.get('contact')
        email=request.POST.get('email')
        year=request.POST.get('year')
        branch=request.POST.get('branch')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
       
        if password==password1:
            user=User.objects.create_user(username=user_name,password=password,email=email  )
            user.save()
            print("User created")     
            return redirect("/signin")
        else:
            messages.info(request, "Password doesn't match")
            return redirect("signup")
     else:
        return render(request, "signup.html")