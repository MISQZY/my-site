# Generated by Django 4.0.6 on 2022-08-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('token', models.TextField(verbose_name='Токен')),
            ],
            options={
                'verbose_name': 'бота',
                'verbose_name_plural': 'Боты',
                'ordering': ['-title'],
            },
        ),
    ]
