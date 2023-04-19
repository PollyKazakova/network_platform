from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.info(request, 'Passwords are not equal! Try, please, again.')
            return redirect('signup')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Such email already exists!")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Such username already exists!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email,
                                                password=password)
                user.save()

                # create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')