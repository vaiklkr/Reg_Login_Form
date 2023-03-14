from django.shortcuts import render
from .forms import RegForm, LoginForm
from .models import Reg
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)      #we create RegForm class object with request.POST parameter
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("Registration Successful...!")
        else:
            print(form.errors)
    else:
        form = RegForm()   #we create RegForm class object without any parameter
    return render(request, 'register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form1 = LoginForm(request.POST)  #create object of LoginForm with request.POST as an parameter
        if form1.is_valid():
            user = form1.cleaned_data['user']
            pwd = form1.cleaned_data['pwd']
            dbuser = Reg.objects.filter(user=user,pwd=pwd)
            if not dbuser:
                return HttpResponse('Login Failed...!')
            else:
                return HttpResponse('Login Successful...!')
    else:
        form1 = LoginForm()
        return render(request, 'login.html', {'form1':form1})
