from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
 

# Create your models here.

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"
        COMPANY = "COMPANY", "Company"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)
    
    
    
class UserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.USER)


class  User(CustomUser):
    base_role = CustomUser.Role.USER
    user = UserManager()

    class Meta:
        proxy = True

    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    

class CompanyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.COMPANY)


    
class Company(CustomUser):
    base_role = CustomUser.Role.COMPANY
    company = CompanyManager()

    class Meta:
        proxy = True