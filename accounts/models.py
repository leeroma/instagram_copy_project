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
    follower = models.ManyToManyField(to='accounts.Account', related_name='followers', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'avatar', 'password']

    objects = AccountManager()

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    @property
    def get_all_publications(self):
        return self.publications.count()

    @property
    def get_all_followers(self):
        return self.follower.all().count()

    @property
    def get_all_followings(self):
        return Account.objects.filter(follower__id=self.id).count()

    def __str__(self):
        return self.username
