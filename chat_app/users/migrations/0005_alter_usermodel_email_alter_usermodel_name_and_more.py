# Generated by Django 5.0.3 on 2024-03-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usermodel_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone',
            field=models.IntegerField(default=0, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='surname',
            field=models.CharField(default='', max_length=255, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default='', max_length=255, verbose_name='Фамилия'),
        ),
    ]
