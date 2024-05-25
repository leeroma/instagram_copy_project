from django.db import models
from accounts.models import Account


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='profile')
    follower = models.ManyToManyField(Account, related_name='followers', blank=True, verbose_name='Подписчик')

    def __str__(self):
        return self.user.username


class Publication(models.Model):
    image = models.ImageField('Изображение', upload_to='post_images', blank=False, null=False)
    description = models.TextField('Описание', max_length=3000, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='publications', verbose_name='Профиль')
    likes = models.ManyToManyField(Account, related_name='likes', blank=True, verbose_name='Нравится')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Publication {self.id}, by {self.profile.user.username}'

    @property
    def get_all_likes(self):
        return self.likes.count()


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT, related_name='comments',
                                    verbose_name='Публикация')
    user = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='comments', verbose_name='Пользователь')
    text = models.TextField('Комментарий', blank=False, null=False)

    def __str__(self):
        return self.text
