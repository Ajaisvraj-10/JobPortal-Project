from django.shortcuts import render

# Create your views here.

def unauthorized_page(request):
    return render(request,'unauthorized.html')