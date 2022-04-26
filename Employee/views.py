from django.shortcuts import render
from .models import *
from django.contrib.auth import login,authenticate

# Create your views here.


def index(request):
    return render(request,'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user=user, empcode=ec)
            error="no"
        except:
            error="yes"
    return render(request,'registration.html',locals())


def emp_login(request):
    error = ""
    if request.method == "POST":
        em = request.POST['emailid']
        pwd = request.POST['password']
        user = authenticate(username=em, password=pwd)
        if user:
            error = "no"
            login(request, user)
        else:
            error = "yes"
    return render(request, 'emp_login.html', locals())

def emp_home(request):
    return render(request,'emp_home.html')