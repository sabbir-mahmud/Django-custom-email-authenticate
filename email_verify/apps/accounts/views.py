# imports
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditProfile
from .models import Profile
from .decorators import authenUser, userpage

# Created your views here.
# Home view
# admin home view


@login_required(login_url='login')
@userpage
def adminhome(request):
    return render(request, 'users/admin.html')

# users home view


@login_required(login_url='login')
def userhome(request):
    return render(request, 'users/admin.html')

# Home view ends
# edit user info


def user_edit(request):
    user = request.user.profile
    if request.method == 'POST':
        fm = EditProfile(request.POST, request.FILES, instance=user)
        if fm.is_valid():
            fm.save()
            return redirect('admin-home-page')
    fm = EditProfile(instance=user)
    context = {'form': fm}
    return render(request, 'users/editprofile.html', context)
# login view


@authenUser
def loggin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            error = 'Email or Password is wrong'
            context = {'error': error}
            return render(request, 'auth/login.html', context)

        if user is not None:
            if user.profile.verify == True:
                login(request, user)
                return redirect('admin-home-page')
            else:
                return HttpResponse('You need to verify your email')
    return render(request, 'auth/login.html')

# login view ends
# log out view


def loggedout(request):
    logout(request)
    return redirect('login')

# log out view ends
# user registration view


@authenUser
def Reg(request):
    if request.method == 'POST':

        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')

    fm = RegisterForm()
    context = {'form': fm}
    return render(request, 'auth/reg.html', context)

# user registration view ends
# user email verify view


def verifier(request, token):
    user = Profile.objects.filter(token=token).first()
    user.token = ''
    user.verify = True
    user.save()
    return redirect('login')

# verify view ends
