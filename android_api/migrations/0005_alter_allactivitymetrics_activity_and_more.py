# Generated by Django 4.1.6 on 2023-02-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android_api', '0004_remove_data_all_activity_metrics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allactivitymetrics',
            name='activity',
            field=models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='allactivitymetrics',
            name='confidence',
            field=models.IntegerField(null=True),
        ),
    ]