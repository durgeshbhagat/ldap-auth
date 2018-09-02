from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render

def user_login(request):
    if request.method == 'GET':
        return render(request,'ldap_auth/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("login successful")
            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse("Invalid Login Credentials")


