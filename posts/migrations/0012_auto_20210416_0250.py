# Generated by Django 2.2.6 on 2021-04-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20210414_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]
