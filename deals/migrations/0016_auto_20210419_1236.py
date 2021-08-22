# Generated by Django 2.2.6 on 2021-04-19 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0015_merge_20210419_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Что нужно сделать?', max_length=50, verbose_name='Задание')),
                ('text', models.TextField(help_text='Подробное описание здания', max_length=500, verbose_name='Описание')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('expected_date', models.DateTimeField(help_text='Когда следует сделать', verbose_name='Запланировано')),
                ('image', models.ImageField(blank=True, help_text='Можно добавить изображение', null=True, upload_to='deals/', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('group', models.ForeignKey(blank=True, help_text='Можно выбрать группу', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='deals.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='SubDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Наименование', max_length=50, verbose_name='Наименование')),
                ('quantity', models.FloatField(help_text='Какое количество требуется', max_length=10, verbose_name='Количество')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('done', models.BooleanField(default=False, help_text='Это задание уже выполнено?', verbose_name='Прогресс')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_deals', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_deals', to='deals.Deal', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Подзадание',
                'verbose_name_plural': 'Подзадания',
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='follow',
            name='author',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]