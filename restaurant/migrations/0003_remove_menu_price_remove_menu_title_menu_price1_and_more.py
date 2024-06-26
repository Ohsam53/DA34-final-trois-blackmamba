# Generated by Django 4.0.3 on 2024-05-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_break_time_restaurant_close_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title',
        ),
        migrations.AddField(
            model_name='menu',
            name='price1',
            field=models.CharField(default='', max_length=20, verbose_name='메인메뉴1 가격'),
        ),
        migrations.AddField(
            model_name='menu',
            name='price2',
            field=models.CharField(default='', max_length=20, verbose_name='메인메뉴2 가격'),
        ),
        migrations.AddField(
            model_name='menu',
            name='title1',
            field=models.CharField(default='', max_length=50, verbose_name='메인메뉴1 이름'),
        ),
        migrations.AddField(
            model_name='menu',
            name='title2',
            field=models.CharField(default='', max_length=50, verbose_name='메인메뉴2 이름'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='break_time',
            field=models.CharField(default=False, max_length=20, verbose_name='브레이크 타임'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='close_day',
            field=models.CharField(default=False, max_length=10, verbose_name='휴일'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='introduction',
            field=models.CharField(default=False, max_length=200, verbose_name='가게 소개'),
        ),
    ]
