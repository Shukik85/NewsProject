from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    surname = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.EmailField(max_length=150, verbose_name='почта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    info = models.CharField(max_length=250, verbose_name='о себе')
    photo = models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name='фото')
    is_admin = models.BooleanField(default=False, verbose_name='администратор')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='профессия')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['-created_at']


class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='профессия')

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
