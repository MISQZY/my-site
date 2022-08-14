from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomUser(AbstractUser):
    acess_level = models.IntegerField(
        default=1,
        verbose_name="Уровень Доступа",
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
        )

    def __str__(self):
        return self.username
