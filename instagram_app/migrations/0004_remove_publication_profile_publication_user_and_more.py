# Generated by Django 5.0.6 on 2024-06-02 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_app', '0003_alter_publication_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='profile',
        ),
        migrations.AddField(
            model_name='publication',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='publications', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
