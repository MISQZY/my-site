# Generated by Django 4.0.6 on 2022-08-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_remove_bots_token_bots_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bots',
            name='tg_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Название в Телеграмм'),
        ),
    ]
