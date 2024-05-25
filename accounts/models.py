from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import AccountManager


class Account(AbstractUser):
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    avatar = models.ImageField('Аватар', upload_to='avatars', blank=False, null=False)
    bio = models.TextField('Информация о пользователе', max_length=3000, blank=True, null=True)
    phone_number = models.IntegerField('Номер телефона', blank=True, null=True)
    sex = models.CharField('Пол', choices=SEX_CHOICES, max_length=6, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'avatar', 'password']

    objects = AccountManager()

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username
