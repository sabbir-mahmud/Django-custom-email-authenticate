# imports
from django.shortcuts import redirect

# user authentication check


def authenUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin-home-page')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def userpage(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.admin == True:
            return view_func(request, *args, **kwargs)

        else:
            return redirect('user-home-page')

    return wrapper_func
