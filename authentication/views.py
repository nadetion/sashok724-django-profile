from django.contrib.auth import forms as auth_forms, login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse as JSON
from . import models, forms
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1 != password2):
            return HttpResponse("Пароли не совпадают")

        form = auth_forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return create_response_object(False, "Успешно")
        else:
            return create_response_object(True, form.errors.as_json())
    elif request.method == 'GET':
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return create_response_object(False, 'Успешно')
        else:
            return create_response_object(True, 'Неправильный логин или пароль')
    elif request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'profile.html')
        else:
            return redirect('/auth/profile/')

def acc_logout(request):
    logout(request)
    return redirect('/')


def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'profile.html')
        else:
             redirect('/auth/signin/')


def mc_login(request):
    login = request.GET['login']
    password = request.GET['password']
    user = authenticate(username=login, password=password)
    if user is not None:
        return HttpResponse('OK:' + user.username)
    else:
        return HttpResponse('Login or password is invalid')


def upload_skin(request):
    if request.method == 'POST':
        form = forms.SkinUpload(request.POST, request.FILES)
        if form.is_valid():
            profile = models.Profile.objects.filter(user=request.user)
            if len(profile) == 0:
                models.Profile.objects.create(user=request.user, skin=request.FILES['skin'])
            else:
                profile.update(skin=request.FILES['skin'])
            file_save(request.FILES['skin'],'/mc/skins/' + request.user.username + '.png')
            return create_response_object(False, "Скин успешно загружен")
        else:
            return create_response_object(True, form.errors.as_json())


def upload_cloak(request):
    if request.method == 'POST':
        form = forms.CloakUpload(request.POST, request.FILES)
        if form.is_valid():
            profile = models.Profile.objects.filter(user=request.user)
            if len(profile) == 0:
                models.Profile.objects.create(user=request.user, cloak=request.FILES['cloak'])
            else:
                profile.update(cloak=request.FILES['cloak'])
            file_save(request.FILES['cloak'],'/mc/cloaks/' + request.user.username + '.png')
            return create_response_object(False, "Плащ успешно загружен")
        else:
            return create_response_object(True, form.errors.as_json())


def create_response_object(error, data):
    if error:
        return JSON({'error': True, 'data': data})
    else:
        return JSON({'error': False, 'data': data})


def file_save(f, dir):
    with open(settings.STATICFILES_DIRS[0] + dir, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)
