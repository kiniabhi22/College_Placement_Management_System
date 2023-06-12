from django.shortcuts import render,redirect
#to be added
from django.http import HttpResponse
from .models import All_Companies,Training,Reg_Com,Reg_Com,studentProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q



# Create your views here. object.remove
def company_reg(request):
        registeredCompanies = Reg_Com.objects.all()
        current_date = timezone.now().date()
        companies = All_Companies.objects.exclude(Q(company_name__in=Reg_Com.objects.all().values_list('company_name', flat=True)) | Q(lastdate__lt=current_date))
        return render(request, 'company_reg.html', {'companies': companies,'regcompanies':registeredCompanies})
    
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
                    company_name=selected_company.company_name,
                    desc=selected_company.desc,
                    branch=selected_company.branch,
                    catagory=selected_company.catagory,
                    salary=selected_company.salary,
                    stipend=selected_company.stipend,
                    role=selected_company.role,
                    aggregate=selected_company.aggregate,
                    joblocation=selected_company.joblocation,
                    dateofdrive=selected_company.dateofdrive
                )
            obj.save()
            registeredCompanies=Reg_Com.objects.all()
            return render(request,'reg_com.html',{'companies':registeredCompanies})
        
        else:
            registeredCompanies = Reg_Com.objects.all()
            return render(request,'reg_com.html',{'companies':registeredCompanies})


def all_companies(request):
    obj=All_Companies.objects.all()  #all_com.objects.get(usn=user.usn)
    return render(request,'all_com.html',{'companies':obj})

def studProfile(request):
    details=studentProfile.objects.all()
    return render(request,'profile.html',{'detail':details})

def dashboard(request):
    return render(request,'dashboard.html') 

def extra(request):
    return HttpResponse("hii bro")

# def Students(request):
#     //details=Student_Details.objects.all()
#     return render(request,'students.html',{'deets':details})

def training(request):
    train=Training.objects.all()
    return render(request,'training.html',{'training':train})

# def reg_com(request):
#     reg=Reg_Com.objects.all()
#     return render(request,'reg_com.html',{'reg_com':reg})

# def current_views(request):
#     curr=Current_Models.objects.all()
#     return render(request,'curr_edu.html',{'currentt':curr})

# def past_views(request):
#     past=Past_Models.objects.all()
#     return render(request,'past_edu.html',{'pastt':past})

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
        USN=request.POST.get('usn')
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
     

# def register_student(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Get the student and company objects
#             student_id = form.cleaned_data['student_id']
#             company_id = form.cleaned_data['company_id']
#             student = Student.objects.get(id=student_id)
#             company = Company.objects.get(id=company_id)

#             # Check if the student has already registered for the company
#             if Registration.objects.filter(student=student, company=company).exists():
#                 return render(request, 'registration_error.html')

#             # Create a new registration object
#             registration = Registration.objects.create(student=student, company=company)

#             # Redirect the user to the confirmation page
#             return redirect('registration_success')
#     else:
#         form = RegistrationForm()

#     return render(request, 'register_student.html', {'form': form})




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# @csrf_exempt
# def login(request):
#     if(request.method=='POST'):
#         user_name=request.POST.get('username')
#         pass_word=request.POST.get('password')
#         user=authenticate(username=user_name,password=pass_word)
#         if(user is not None):
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,"Invalid Credentials")
#             return render(request,'login.html')
#     else:
#         return render(request, "login.html")
    

# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# @csrf_exempt
# def register(request):
#     if request.method == 'POST':
#         first_name=request.POST.get('firstname')
#         last_name=request.POST.get('lastname')
#         user_name=request.POST.get('username')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         password1=request.POST.get('password1')
#         if password==password1:
#             user=User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
#             user.save()
#             print("User created")
#             return redirect("/login")
#         else:
#             messages.info(request, "Password doesn't match")
#             return redirect("register")
#     else:
#         return render(request, "register.html")