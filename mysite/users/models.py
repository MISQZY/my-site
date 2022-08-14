from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from django.conf import settings

class CustomUser(AbstractUser):
    acess_level = models.IntegerField(
        default=1,
        verbose_name="Уровень Доступа",
        choices=settings.ACESS_LEVELS,
        blank=False,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
        )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.username
