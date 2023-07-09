from django.shortcuts import render
from user.models import UserProfile
from company.models import CompanyProfile
from .decorators import admin_login_required


# Create your views here.

@admin_login_required
def admin_home(request):
    return render(request, 'admin/admin_home.html')



def registered_users(request):
    users = UserProfile.objects.all()
    companies = CompanyProfile.objects.all()
    context = {
        'users': users,
        'companies': companies
    }
    return render(request, 'admin/registered_users.html', context)
