from django.apps import AppConfig


class MyStorageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_storage'
    verbose_name = 'Хранилище'
