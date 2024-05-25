from django.contrib.auth.models import UserManager


class AccountManager(UserManager):

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = username or email
        return super(AccountManager, self).create_superuser(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = username or email
        return super(AccountManager, self).create_superuser(username, email, password, **extra_fields)
