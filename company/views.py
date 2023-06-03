from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="company_login")
def company_index(request):
    return render(request,'company/company_index.html')

def company_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        
        if not CustomUser.objects.filter(username=username).exists():
            if password1 == password2:
                CustomUser.objects.create_user(
                    username=username,
                    first_name=company_name,
                    email=email,
                    password=password2
                )
        return redirect('company_profile')
    return render(request, 'company/company_registration.html')


def company_login(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        password = request.POST.get('password')
        user = authenticate(request,company_name=company_name,password=password)
        if user:
            login(request,user)
            return redirect('company_index')
    return render(request,'company/company_login.html')


def logout_company(request):
    logout(request)
    return redirect("company_login")


def company_profile(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        logo = request.FILES.get('logo')
        CompanyProfile.objects.create(
            user=request.user,
            company_name=company_name,
            location=location,
            contact_email=contact_email,
            contact_phone=contact_phone,
            logo=logo
        )
        return redirect('company_list')
    return render(request,'company/company_profile.html')


def company_list(request):
    user = request.user
    profiles = CompanyProfile.objects.filter(user=user)
    context = {"profiles": profiles}
    return render(request,'company/company_list.html',context)


def company_details(request,id):
    details = CompanyProfile.objects.get(id=id)
    context = {'profiles':details}
    return render(request,'company/company_details.html',context)


def company_addjob(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        job_title = request.POST.get('job_title')
        description = request.POST.get('description')
        job_type = request.POST.get('job_type')
        salary = request.POST.get('salary')
        skills_required = request.POST.get('skills_required')
        education_required = request.POST.get('education_required')
        experience_required = request.POST.get('experience_required')

        AddJob.objects.create(
            user = request.user,
            company_name=company_name,
            location=location,
            job_tittle=job_title,
            description=description,
            job_type=job_type,
            salary=salary,
            skills_required=skills_required,
            education_required=education_required,
            experience_required=experience_required
        )
        return redirect('company_joblist')
    return render(request,'company/company_addjob.html')


def company_joblist(request):
    user = request.user
    joblist = AddJob.objects.filter(user=user)
    context = {'joblist':joblist}
    return render(request,'company/company_joblist.html',context)


def company_jobdetails(request,id):
    jobdetails = AddJob.objects.get(id=id)
    context = {'joblist':jobdetails}
    return render(request,'company/company_jobdetails.html',context)


def appliction_submision(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        job = request.POST.get('job')
        resume = request.POST.get('resume')
        status = request.FILES.get('status')
    
        AppllicationSubmition.objects.create(
            user = request.user,
            username=username,
            job=job,
            resume=resume,
            status=status
        )
        return redirect('application_list')
    return render(request,'company/application_submission.html',{'choices':AppllicationSubmition.selection_choices})


def appliction_list(request):
    application = AppllicationSubmition.objects.all()
    context = {'application':application}
    return render(request,'company/application_list.html',context)