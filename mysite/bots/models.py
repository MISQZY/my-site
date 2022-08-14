from django.db import models

class Bots(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    tg_name = models.CharField(max_length=150, verbose_name='Название в Телеграмм')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'бота'
        verbose_name_plural = 'Боты'
        ordering = ['-title']
