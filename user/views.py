from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from account .models import *
from .models import *
from.decorators import user_login_required
from company.models import AddJob


# Create your views here.
@user_login_required
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
                )
                messages.success(request, "Account created successfully")
                return redirect('user_login')
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exists")
    return render(request, 'user/user_registration.html')
    
    
    
@user_login_required
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


@user_login_required
def user_profileview(request):
    user = request.user
    profileview = UserProfile.objects.filter(user=user)
    context = {'profileview':profileview}
    return render(request,'user/user_profileview.html',context)



@user_login_required
def user_profile_details(request,id):
    profile_details = UserProfile.objects.get(id=id)
    add_education = AddEducation.objects.filter(user=profile_details.user)
    add_skill = AddSkills.objects.filter(user=profile_details.user)
    add_experience = AddExperience.objects.filter(user=profile_details.user)
    add_projects = AddProject.objects.filter(user=profile_details.user)
    context = {
        'profileview':profile_details,
        'education_list': add_education,
        'skill_list': add_skill,
        'experience_list': add_experience,
        'project_list': add_projects,
    }
    return render(request,'user/user_profile_details.html',context)


@user_login_required
def add_education(request):
    if request.method == 'POST':
        name_of_college = request.POST.get('name_of_college')
        passout_year = request.POST.get('passout_year')
        subject = request.POST.get('subject') 
        user = request.user
        AddEducation.objects.create( 
            user=user,                        
            name_of_college=name_of_college,
            passout_year=passout_year,
            subject=subject,
        )
        user_profile_id = user.userprofile.id
        return redirect('user_profile_details', id=user_profile_id)
    return render(request, 'user/add_education.html')


@user_login_required
def add_skill(request):
    if request.method == 'POST':
        skill_name = request.POST.get('skill_name')
        description = request.POST.get('description')
        user=request.user
        AddSkills.objects.create(
            user=user,
            skill_name = skill_name,
            description = description,
            
        )
        user_profile_id = user.userprofile.id
        return redirect('user_profile_details',id=user_profile_id)
    return render(request,'user/add_skill.html')


@user_login_required
def add_experience(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user = request.user
        AddExperience.objects.create(
            user=user,
            company_name = company_name,
            position = position,
            start_date = start_date,
            end_date = end_date,
            
        )
        user_profile_id = user.userprofile.id
        return redirect('user_profile_details',id=user_profile_id)
    return render(request,'user/add_experience.html')


def add_projects(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        AddProject.objects.create(
            user=user,
            title = title,
            description = description,
        )
        user_profile_id = user.userprofile.id
        return redirect('user_profile_details',id=user_profile_id)
    return render(request,'user/add_project.html')


def apply_job(request, job_id):
    job = AddJob.objects.get(id=job_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        
        JobApplication.objects.create(
            job=job,
            name=name,
            email=email,
            resume=resume,
        )
        return redirect('job_listing')
    return render(request, 'user/apply_job.html', {'job': job})



def job_listing(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    return render(request, 'user/job_listing.html', {'job': job})