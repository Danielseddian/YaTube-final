from django.contrib.auth import get_user_model
from django.db import models

from .settings import NOT_DONE

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Группа',
        max_length=200
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=200,
        unique=True
    )
    description = models.TextField('Описание', help_text='Описание группы')

    def __str__(self):
        return self.title


class Deal(models.Model):
    title = models.CharField(
        verbose_name='Задание',
        help_text='Что нужно сделать?',
        max_length=50
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Подробное описание здания',
        max_length=500
    )
    creation_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True,
    )
    expected_date = models.DateTimeField(
        verbose_name='Запланировано',
        help_text='Когда следует сделать',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='deals',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Можно выбрать группу',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='deals/',
        blank=True,
        null=True,
        help_text='Можно добавить изображение',
    )
    status = models.CharField(
        verbose_name='Прогресс',
        default= NOT_DONE,
        help_text='Это задание уже выполнено?',
        max_length=20
    )

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ('-creation_date',)

    def __str__(self):
        return f'Задание: {self.text} Описание: {self.title} ' \
               f'Создано: {self.creation_date} ' \
               f'Запланировано: {self.expected_date}'


class SubDeal(models.Model):
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name='sub_deals',
        verbose_name='Задание'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sub_deals',
        verbose_name='Автор'
    )
    title = models.CharField(
        verbose_name='Наименование',
        help_text='Наименование',
        max_length=50
    )
    quantity = models.FloatField(
        verbose_name='Количество',
        help_text='Какое количество требуется',
        default=0,
        blank=True,
        null=True,
        max_length=10
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    status = models.CharField(
        verbose_name='Прогресс',
        default=NOT_DONE,
        help_text='Это задание уже выполнено?',
        max_length=20
    )

    class Meta:
        verbose_name = 'Подзадание'
        verbose_name_plural = 'Подзадания'
        ordering = ('-created',)

    def __str__(self):
        if self.done is False:
            done = 'нет'
        else:
            done = 'да'
        return f'Что: {self.title} Количество: {self.quantity} ' \
               f'Создано: {self.creation_date} Сделано: {done}'


'''class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        verbose_name = 'Подписан'
        ordering = ('author',)

    def __str__(self):
        return f'Пользователь: {self.user.username} ' \
               f'Подписан на: {self.author.username}'''
