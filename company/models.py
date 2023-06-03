from django.db import models
from user.models import *
# Create your models here.

class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="company_logo/",null=True,blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.company_name
      
    
class AddJob(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
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
    

class AppllicationSubmition(models.Model):
    
    selection_choices = (
        ('pending','Pending'),
        ('selected','Selected'),
        ('not selected','Not Selected')
    )
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,null= True)
    job = models.ForeignKey(AddJob,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume/',null=True)
    status = models.CharField(max_length=100,default='pending')
    
    def __str__(self):
        return f"{self.username} - {self.job.title}"    
    
    
