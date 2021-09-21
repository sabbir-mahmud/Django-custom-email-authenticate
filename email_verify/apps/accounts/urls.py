# imports
from django.urls import path, include
from . import views
from django.contrib.auth import views as reset_password

# urls
urlpatterns = [
    # admin/user home page view
    path('', views.adminhome, name='admin-home-page'),
    path('users/', views.userhome, name='user-home-page'),
    # user info edit
    path('edit_info/', views.user_edit, name='user_edit'),
    # logIn/logOut/register/verifier view
    path('login/', views.loggin, name='login'),
    path('logout/', views.loggedout, name='log_out'),
    path('register/', views.Reg, name='reg'),
    path('accounts/<slug:token>', views.verifier, name='verifier'),
    # change password
    path('change_password/', reset_password.PasswordChangeView.as_view(template_name='auth/changepass.html'),
         name='password_change'),
    path('change_password_done/', reset_password.PasswordChangeDoneView.as_view(
        template_name='auth/changepassdone.html'), name='password_change_done'),
    # password reset urls
    # reset password email submit page
    path('reset_password/', reset_password.PasswordResetView.as_view(template_name='auth/forgetpass.html'),
         name='reset_password'),

    # reset password email sent page
    path('reset_token_sent/', reset_password.PasswordResetDoneView.as_view(template_name='auth/emailsent.html'),
         name='password_reset_done'),

    # reset password clicked on mail token page
    path('reset/<uidb64>/<token>/', reset_password.PasswordResetConfirmView.as_view(template_name='auth/setnewpass.html'),
         name='password_reset_confirm'),

    # reset password done page
    path('password_reset_complete/', reset_password.PasswordResetCompleteView.as_view(template_name='auth/forgetpassdone.html'),
         name='password_reset_complete'),
]
