from django.db import models
from account.models import CustomUser
# Create your models here.


    
    
class UserProfile(models.Model):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cont_email = models.EmailField()
    cont_phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    name_of_college = models.CharField(max_length=100,null= True)
    passout_year = models.CharField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null= True)
    
    
    
class Skills(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    
    
class Experience(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    start_date = models.CharField(max_length=100,null=True)
    end_date = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.company_name} - {self.position}"
    
    
    
class Project(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    