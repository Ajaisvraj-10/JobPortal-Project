from django.db import models
from account.models import CustomUser,User,Company
from company.models import AddJob
# Create your models here.

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cont_email = models.EmailField()
    cont_phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class AddEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name_of_college = models.CharField(max_length=100,null= True)
    passout_year = models.CharField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null= True)
    
    
    
class AddSkills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    

    
class AddExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    start_date = models.CharField(max_length=100,null=True)
    end_date = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.company_name} - {self.position}"
    
    
    
class AddProject(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    job = models.ForeignKey(AddJob, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/',null=True, blank=True)

    def __str__(self):
        return f"Application for {self.job.job_title} by {self.name}"
    



class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    skills_required = models.TextField()
    education_required = models.CharField(max_length=100)
    experience_required = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
