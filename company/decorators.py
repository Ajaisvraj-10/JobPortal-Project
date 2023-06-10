from django.shortcuts import redirect,render


def company_login_required(function):
    def wrappeer(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('company_login')
        else:
            if request.user.role != 'COMPANY':
                return render(request, "unauthorized.html")
        return function(request,*args,**kwargs)
    return wrappeer