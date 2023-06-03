from django.urls import path
from .views import *

urlpatterns = [
    path('company_index/',company_index,name ='company_index'),
    path('company_register/',company_registration,name ='company_register'),
    path('company_login/',company_login,name ='company_login'),
    path('logout_company/',logout_company,name ='logout_company'),
    path('company_profile/',company_profile,name ='company_profile'),
    path('company_list/',company_list,name ='company_list'),
    path('company_details/<int:id>/',company_details,name ='company_details'),
    path('company_addjob/',company_addjob,name ='company_addjob'),
    path('company_joblist/',company_joblist,name ='company_joblist'),
    path('company_jobdetails/<int:id>/',company_jobdetails,name ='company_jobdetails'),
    path('application_submission',appliction_submision,name ='application_submission'),
    path('application_list',appliction_list,name ='application_list'),  
]