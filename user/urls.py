from django.urls import path
from .views import *

urlpatterns = [
    path('',user_index,name='user_index'),
    path('user_login/', user_login, name='user_login'),
    path('user_register/', user_registration, name='user_register'),
    path('logout_user/', logout_user, name='logout_user'),
    path('adduser_profile/', adduser_profile, name='adduser_profile'),
    path('user_profileview/', user_profileview, name='user_profileview'),
    path('user_profile_details/<int:id>/', user_profile_details, name='user_profile_details'),
    path('add_education', add_education, name='add_education'),
    path('add_skill', add_skill, name='add_skill'),
    path('add_experience', add_experience, name='add_experience'),
    path('add_projects', add_projects, name='add_projects'),
    path('apply_job/<int:job_id>/', apply_job, name='apply_job'),
    path('job_listing', job_listing, name='job_listing'),
]