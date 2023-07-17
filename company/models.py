from django.db import models
from user.models import *
from account.models import Company
# Create your models here.

class CompanyProfile(models.Model):
    user = models.OneToOneField(Company,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="company_logo/",null=True,blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.company_name
      
    
class AddJob(models.Model):
    user = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=200,null=True)
    job_tittle = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=200,null=True)
    job_type = models.CharField(max_length=100,null=True)
    salary = models.CharField(max_length=100,null=True)
    skills_required = models.CharField(max_length=250,null= True)
    education_required = models.CharField(max_length=150,null=True)
    experience_required = models.CharField(max_length=250,null= True)
    created = models.DateField(auto_now_add=True,null=True)
    updated = models.DateField(auto_now=True,null=True)
    
    def __str__(self):
        return self.job_tittle
    


    
