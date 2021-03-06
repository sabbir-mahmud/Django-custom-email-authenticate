# imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

# Create your models here.

# user manager


class UserManager(BaseUserManager):
    # create user
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Enter a valid email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create staff user
    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password)
        user.staff = True
        user.save(using=self._db)
        return user

    # create super user / admin
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# user model


class User(AbstractBaseUser):
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    email = models.EmailField(max_length=245, unique=True)
    first_name = models.CharField(max_length=245)
    last_name = models.CharField(max_length=245)
    gender = models.CharField(max_length=245, choices=genders, default='Male')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    # username replaced with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin == True:
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.admin == True:
            return True
        else:
            return False


# profile model
class Profile(models.Model):
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=245)
    email = models.EmailField(max_length=245, unique=True)
    gender = models.CharField(max_length=245, choices=genders, default='Male')
    token = models.CharField(max_length=245, null=True, blank=True)
    verify = models.BooleanField(default=False)
    pro_img = models.ImageField(
        upload_to='auth/profile_img/', default='auth/profile_img/user.svg')

    def __str__(self):
        return self.name
