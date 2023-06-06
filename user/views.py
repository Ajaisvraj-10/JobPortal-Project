from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from account .models import *
from .models import *

# Create your views here.

def user_index(request):
    return render(request,"user/user_index.html")



def user_login(request):
    if request.user.is_authenticated:
        return redirect("user_index")
    user = request.user
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect("user_index")
        messages.error(request, "Invalid username or password")
    return render(request,"user/user_login.html")


def logout_user(request):
    logout(request)
    return redirect('user_login')


def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        email = request.POST.get('email')
        
        user = User.objects.filter(username=username)
        if not user:
            if password1 == password2:
                User.objects.create_user(
                    username=username,
                    first_name=name,
                    email=email,
                    password=password2,
                    is_active = True
                )
                messages.success(request, "Account created successfully")
                return redirect('adduser_profile')
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exists")
    return render(request, 'user/user_registration.html')
    

def adduser_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        cont_email = request.POST.get('cont_email')
        cont_phone = request.POST.get('cont_phone')
        profile_image = request.FILES.get('profile_image')
        gender = request.POST.get('gender')
        
        UserProfile.objects.create(
            user=request.user,
            name=name,
            location=location,
            cont_email=cont_email,
            cont_phone=cont_phone,
            profile_image=profile_image,
            gender=gender
        )
        return redirect('user_profileview')
    return render(request,'user/adduser_profile.html',{'choices':UserProfile.GENDER_CHOICES})


 
def user_profileview(request):
    user = request.user
    profileview = UserProfile.objects.filter(user=user)
    context = {'profileview':profileview}
    return render(request,'user/user_profileview.html',context)


def user_profile_details(request,id):
    profile_details = UserProfile.objects.get(id=id)
    context = {'profileview':profile_details}
    return render(request,'user/user_profile_details.html',context)


def add_education(request):
    if request.method == 'POST':
        name_of_college = request.POST.get('name_of_college')
        passout_year = request.POST.get('passout_year')
        subject = request.POST.get('subject')

        

        Education.objects.create( 
            user_profile = request.user,
            name_of_college=name_of_college,
            passout_year=passout_year,
            subject=subject
        )

        return redirect('profile')
    return render(request,'add_education.html')


