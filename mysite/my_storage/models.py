from django.db import models
from django.urls import reverse

class Storage(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    file = models.FileField(upload_to='files',blank=False, verbose_name='Файл')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse("card_id", kwargs={"card_id": self.pk})


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'карточку'
        verbose_name_plural = 'Библиотека'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        test = reverse("categories_list_for_get", kwargs={"category_id": self.pk})
        return test


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']
