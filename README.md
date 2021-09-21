# Django-custom-email-authenticate
 Register/login with email. and verify account with email

with this application you can register account with email, login with email, logout. Also you can verify your account with email. user need to verify their email for access user/admin page. Different home page for users and admin.

# reqirments:
1. python venv
2. django
3. pillow

# run project:
open terminal and run those commands:

active virtual envirment * .\Scripts\activate * cd email_verify

migrate project * python manage.py makemigrations * python manage.py migrate

run project * python manage.py runserver

# configure email settings:
project settings.py:

Email Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'Yourmail@your.com'

EMAIL_HOST_PASSWORD = 'Your Password'


# if you need superuser/admin
create superuser:
* python manage.py createsuperuser
* enter your email
* enter your password
