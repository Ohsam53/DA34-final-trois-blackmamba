# Generated by Django 4.0.3 on 2024-05-29 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_restaurant_close_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='parking_area',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='주차장소추천'),
        ),
    ]
