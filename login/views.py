from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib.auth.models import Group

from .models import Customer

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if username == 'reception' and password =='1234':
            print(username)
            return redirect('book_list',)
        elif username == 'medecin' and password =='1234':
            print(username)
            return redirect('medecin_list',)
        elif username == 'specialiste' and password =='1234':
            print(username)
            return redirect('specialiste_list',)
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login/login.html')

