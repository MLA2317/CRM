from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.safestring import mark_safe
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if phone is None:
            raise TypeError('User should have a phone number')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password should not be None')

        user = self.create_user(
            phone=phone,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_teacher = True
        user.is_student = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    GENDER = (
        (0, 'None'),
        (1, 'Male'),
        (2, 'Female'),
    )
    ROLE = (
        (0, 'Staff'),
        (1, 'Teacher'),
        (2, 'Student'),
        (3, 'demo'),
    )

    first_name = models.CharField(max_length=50, verbose_name='First name', null=True)
    last_name = models.CharField(max_length=50, verbose_name='Last name', null=True)
    phone = models.CharField(max_length=16, unique=True, db_index=True, verbose_name='Phone number', null=True)
    birth_year = models.IntegerField(null=True, blank=True, verbose_name="Birth year")
    avatar = models.ImageField(upload_to='accounts/', verbose_name='User avatar', null=True, blank=True)
    role = models.IntegerField(choices=ROLE, default=1)
    gender = models.IntegerField(choices=GENDER, default=0)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_teacher = models.BooleanField(default=False, verbose_name="Teacher")
    is_student = models.BooleanField(default=False, verbose_name="Student")
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    date_login = models.DateTimeField(auto_now=True, verbose_name='Date login')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    objects = AccountManager()

    EMAIL_FIELD = 'phone'
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.phone}'

    def image_tag(self):
        if self.avatar:
            return mark_safe(f'<a href="{self.avatar.url}"><img src="{self.avatar.url}" style="height:40px;"/></a>')
        return 'no_image'

    @property
    def image_url(self):
        if self.avatar:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.avatar.url}'
            return f'{settings.PROD_BASE_URL}{self.avatar.url}'
        else:
            return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
