# Generated by Django 4.0.6 on 2022-07-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_storage', '0002_alter_category_options_alter_storage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
    ]
