# Generated by Django 4.1.6 on 2023-02-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android_api', '0010_devicehistory_yandex_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicehistory',
            name='time',
            field=models.CharField(blank=True, max_length=625, verbose_name='Last message'),
        ),
        migrations.AlterField(
            model_name='historicaldevicehistory',
            name='time',
            field=models.CharField(blank=True, max_length=625, verbose_name='Last message'),
        ),
    ]