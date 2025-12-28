from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано')
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Слаг')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    body = models.TextField( verbose_name='Содержание')
    image = models.ImageField(upload_to="%Y/%m/%d/", verbose_name='Изображение')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name='Статус'
    )

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )



class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',verbose_name='Заголовок')
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField( verbose_name='Электронная почта')
    body = models.TextField( verbose_name='Содержание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
