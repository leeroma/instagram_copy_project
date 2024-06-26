# Generated by Django 5.0.6 on 2024-06-02 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='follower',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
