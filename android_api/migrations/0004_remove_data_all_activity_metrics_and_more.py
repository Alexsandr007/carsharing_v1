# Generated by Django 4.1.6 on 2023-02-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android_api', '0003_alter_device_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='all_activity_metrics',
        ),
        migrations.AddField(
            model_name='data',
            name='all_activity_metrics',
            field=models.ManyToManyField(to='android_api.allactivitymetrics'),
        ),
    ]
