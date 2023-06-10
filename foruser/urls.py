from django.urls import path
from .views import *




urlpatterns = [
    path('unauthorized_page/',unauthorized_page,name='unauthorized_page'),
    
]