from django.urls import path
from . views import *

urlpatterns = [
    path('admin_home',admin_home,name='admin_home'),
    path('registered_users',registered_users,name='registered_users'),
   
    
]