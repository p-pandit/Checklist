from django.shortcuts import render,HttpResponseRedirect
from .models import s21
from tablib import Dataset
from datetime import datetime,timedelta,date
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
import pytz

IST = pytz.timezone('Asia/Kolkata')
today = date.today()


def stn(request):
    if request.user.is_authenticated:

        data=s21.objects.filter(date=today).first()
        stn = s21.objects.filter(date=today)[1:]
    else:
        return HttpResponseRedirect('login')

    return render(request,'stn.html',{'data':data,'stn':stn,'date':today,'user':request.user})


def loginform(request):
    fm = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                paswd = fm.cleaned_data['password']

                user = authenticate(username=uname, password=paswd)
                if user is not None:
                    login(request, user)
                    print("inside login")
                    print(user)
                    return HttpResponseRedirect('stn')
        else:
            return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('stn')


def logoutt(request):
    logout(request)
    return HttpResponseRedirect('login')