#copied from urls of project
from django.urls import path,include #added include
from .import views


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('All_Companies/',views.all_companies,name='All_Companies'),
    path('Training/',views.training,name='training'),
    # path('Login/',views.login,name='login'),
    # path('Register/',views.register,name='register'),
    # path('logout/',views.logout,name='logout'),
    path('Reg_Com/',views.reg_com,name='reg_com'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('Register_reg/',views.company_reg, name='company_reg'),
    # path('deRegister/',views.deRegister, name='deRegister'),
    path('profile/',views.studProfile, name='profile'),
    

]