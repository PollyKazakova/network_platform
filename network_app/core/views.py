from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Post


@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': posts})


@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':

        new_post = Post.objects.create(user=request.user.username, image=request.FILES.get('image_upload'),
                                       caption=request.POST['caption'])
        new_post.save()
    return redirect('/')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_profile.first_name = request.POST['first_name']
        user_profile.last_name = request.POST['last_name']
        user_profile.bio = request.POST['bio']
        user_profile.location = request.POST['location']
        if request.FILES.get('image') is None:
            user_profile.profile_img = user_profile.profile_img
        else:
            user_profile.profile_img = request.FILES.get('image')
        user_profile.save()
        return redirect('settings')

    return render(request, 'settings.html', {'user_profile': user_profile})


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

                # log in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create a Profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Accounting Data Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')



