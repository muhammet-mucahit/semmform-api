from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from account.managers import UserManager
from form.models import Form


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    date_joined = models.DateTimeField(_('Katılma Tarihi'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('Yetkili Mi?'), default=False)
    forms = models.ManyToManyField(Form)

    # Profile Part
    first_name = models.CharField(_('İsim'), max_length=100, null=True)
    last_name = models.CharField(_('Soyisim'), max_length=100, null=True)
    dob = models.DateField(null=True)
    phone = models.CharField(_('Telefon'), max_length=16,
                             null=True, )
    address = models.CharField(_('Adres'),
                               max_length=300,
                               null=True,
                               blank=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=5, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
