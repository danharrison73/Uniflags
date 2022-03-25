# Written by Dan and Max

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import loader

from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Flag


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            newUser = User.objects.create_user(username, email, password1)

            newUser.save()

            messages.success(request, "Account successfully created.")
            return redirect('signin')

    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "home.html", {'username': username})
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.info(request, "You have succesfully logged out.")
    return redirect("signin")

def question(request):
    current_user = request.user
    user = User.objects.filter(username=current_user)
    new_flag = Flag(lat=0, lng=0, owner=current_user)
    new_flag.save()
    return render(request, 'question.html')


@login_required(login_url='signin')
def leaderboard(request):
    flags = Flag.objects.all()
    users = User.objects.all()

    number_of_flags = flags.count()

    data = []

    # goes through all the flags and works out how many flags each user owns by checking their owners.
    for flag in flags:
        owner = flag.get_owner().username
        owner_in_data = False
        for i in data:
            if i['username'] == owner:
                owner_in_data = True
                i['flag_count'] += 1
        if not owner_in_data:
            data.append({'username':owner, 'flag_count':1, 'flag_pct':0})

    for i in data:
        i['flag_pct'] = round(i['flag_count'] * 100 / number_of_flags)

    data = sorted(data, key=lambda d: d['flag_count'], reverse=True)
    data = data[:5]

    return render(request, 'leaderboard.html', {'data': data})


@login_required(login_url='signin')
def scan(request):
    return render(request, 'scan.html')
