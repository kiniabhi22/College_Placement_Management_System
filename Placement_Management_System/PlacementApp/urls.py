#copied from urls of project
from django.urls import path,include #added include
from .import views
# from django.urls import reverse


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('All_Companies/',views.all_companies,name='All_Companies'),
    path('Reg_Com/',views.reg_com,name='reg_com'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('Register_reg/',views.company_reg, name='company_reg'),
    path('profile/',views.studProfile, name='profile'),
    path('getJob/',views.job_search, name='getJob'),
    path('upload/', views.uploadResume, name='uploadResume'),
    path('view/<int:resume_id>/', views.viewResume, name='viewResume'),
    path('studentDetails', views.studentDetails,name='studentDetails'),
    
]