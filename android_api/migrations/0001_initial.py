# Generated by Django 4.0 on 2022-12-27 18:28

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (Базовые типы)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (Базовые типы)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='ConfirmationTelegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField(verbose_name='Device id')),
                ('is_telegram_activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Подтверждение регистрации в телеграме',
                'verbose_name_plural': 'Подтверждение регистраций в телеграме',
            },
        ),
        migrations.CreateModel(
            name='CurrentUTCTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_utc', models.CharField(max_length=2, verbose_name='Текущее значение UTC')),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField()),
                ('driver_id', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('is_telegram_activated', models.BooleanField(default=False)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('location', models.CharField(blank=True, max_length=625)),
                ('is_stopped', models.BooleanField()),
                ('app_type', models.CharField(choices=[('phone', 'Phone'), ('mirror', 'Mirror')], max_length=25)),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('okodrive_status', models.CharField(blank=True, choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], default='ignore', max_length=25)),
                ('state_number', models.CharField(blank=True, max_length=125, null=True)),
                ('speed', models.FloatField()),
                ('satellites', models.PositiveIntegerField(blank=True, null=True)),
                ('accuracy', models.FloatField()),
                ('bearing', models.FloatField()),
                ('client_timestamp', models.PositiveIntegerField()),
                ('altitude', models.FloatField()),
                ('last_message_timestamp_utc', models.PositiveBigIntegerField(blank=True, null=True)),
                ('last_message_timestamp_txt_utc', models.CharField(blank=True, max_length=625, verbose_name='Last message')),
                ('charging', models.BooleanField()),
                ('battery_percent', models.PositiveIntegerField()),
                ('network_type', models.CharField(blank=True, max_length=12, null=True)),
                ('yandex_link', models.CharField(blank=True, max_length=625)),
                ('acceleration_x', models.FloatField()),
                ('acceleration_y', models.FloatField()),
                ('acceleration_z', models.FloatField()),
                ('error_name', models.CharField(blank=True, choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('none', 'None')], max_length=12, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Телеметрия устройства',
                'verbose_name_plural': 'Телеметрия устройств',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField(verbose_name='Device id')),
                ('driver_id', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('is_telegram_activated', models.BooleanField(default=False)),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('location', models.CharField(blank=True, max_length=625, verbose_name='Location')),
                ('is_stopped', models.BooleanField()),
                ('app_type', models.CharField(choices=[('phone', 'Phone'), ('mirror', 'Mirror')], max_length=25)),
                ('activity_type', models.CharField(max_length=25, verbose_name='Activity Type')),
                ('okodrive_status', models.CharField(blank=True, choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], default='ignore', max_length=25)),
                ('speed', models.FloatField(verbose_name='Speed')),
                ('satellites', models.PositiveIntegerField(blank=True, null=True, verbose_name='Satellites')),
                ('accuracy', models.FloatField(verbose_name='Accuracy')),
                ('client_timestamp', models.PositiveIntegerField()),
                ('bearing', models.FloatField(verbose_name='Bearing')),
                ('altitude', models.FloatField(verbose_name='Altitude')),
                ('last_message_timestamp_utc', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Last message timestamp utc')),
                ('last_message_timestamp_txt_utc', models.CharField(blank=True, max_length=625)),
                ('charging', models.BooleanField(verbose_name='Charging')),
                ('battery_percent', models.PositiveIntegerField(verbose_name='Battery percent')),
                ('network_type', models.CharField(blank=True, max_length=12, null=True, verbose_name='Network Type')),
                ('yandex_link', models.CharField(blank=True, max_length=625, verbose_name='Yandex link')),
                ('acceleration_x', models.FloatField(verbose_name='Acceleration X')),
                ('acceleration_y', models.FloatField(verbose_name='Acceleration Y')),
                ('acceleration_z', models.FloatField(verbose_name='Acceleration Z')),
                ('error_name', models.CharField(blank=True, choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('none', 'None')], max_length=12, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Изменено')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'История устройства',
                'verbose_name_plural': 'История устройств',
                'ordering': ['-device_id', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalDevice',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('device_id', models.IntegerField()),
                ('driver_id', models.CharField(blank=True, db_index=True, max_length=40, null=True)),
                ('is_telegram_activated', models.BooleanField(default=False)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('location', models.CharField(blank=True, max_length=625)),
                ('is_stopped', models.BooleanField()),
                ('app_type', models.CharField(choices=[('phone', 'Phone'), ('mirror', 'Mirror')], max_length=25)),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('okodrive_status', models.CharField(blank=True, choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], default='ignore', max_length=25)),
                ('state_number', models.CharField(blank=True, max_length=125, null=True)),
                ('speed', models.FloatField()),
                ('satellites', models.PositiveIntegerField(blank=True, null=True)),
                ('accuracy', models.FloatField()),
                ('bearing', models.FloatField()),
                ('client_timestamp', models.PositiveIntegerField()),
                ('altitude', models.FloatField()),
                ('last_message_timestamp_utc', models.PositiveBigIntegerField(blank=True, null=True)),
                ('last_message_timestamp_txt_utc', models.CharField(blank=True, max_length=625, verbose_name='Last message')),
                ('charging', models.BooleanField()),
                ('battery_percent', models.PositiveIntegerField()),
                ('network_type', models.CharField(blank=True, max_length=12, null=True)),
                ('yandex_link', models.CharField(blank=True, max_length=625)),
                ('acceleration_x', models.FloatField()),
                ('acceleration_y', models.FloatField()),
                ('acceleration_z', models.FloatField()),
                ('error_name', models.CharField(blank=True, choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('none', 'None')], max_length=12, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Телеметрия устройства',
                'verbose_name_plural': 'historical Телеметрия устройств',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='InVehicleOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (IN_VEHICLE)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (IN_VEHICLE)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='OnBicycleOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (ON_BICYCLE)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (ON_BICYCLE)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='OnFootOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (ON_FOOT)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (ON_FOOT)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='RunningOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (RUNNING)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (RUNNING)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='SpeedIntervalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_interval', models.CharField(max_length=12, verbose_name='Первый интервал')),
                ('second_interval', models.CharField(max_length=12, verbose_name='Второй интервал')),
                ('third_interval', models.CharField(max_length=12, verbose_name='Третий интервал')),
                ('fourth_interval', models.CharField(max_length=12, verbose_name='Четвёртый интервал')),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Настройка промежутков скоростей для определения OkoDrive_status',
                'verbose_name_plural': 'Настройки промежутков скоростей для определения OkoDrive_status',
                'ordering': ['-is_main'],
            },
        ),
        migrations.CreateModel(
            name='StillOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (STILL)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (STILL)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='TiltingOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (TILTING)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (TILTING)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='TimeStampSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_interval', models.PositiveIntegerField(default=10)),
                ('max_interval', models.PositiveIntegerField(default=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Временная метка',
                'verbose_name_plural': 'Временные метки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UnknownOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (UNKNOWN)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (UNKNOWN)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.CreateModel(
            name='WalkingOkoDriveSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('IN_VEHICLE', 'In Vehicle'), ('ON_BICYCLE', 'On Bicycle'), ('ON_FOOT', 'On Foot'), ('WALKING', 'Walking'), ('RUNNING', 'Running'), ('STILL', 'Still'), ('TILTING', 'Tilting'), ('UNKNOWN', 'Unknown'), ('None', 'None')], max_length=25)),
                ('speed_of_first_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для первого интервала')),
                ('speed_of_second_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для второго интервала')),
                ('speed_of_third_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для третьего интервала')),
                ('speed_of_fourth_interval', models.CharField(choices=[('in_car', 'In Car'), ('out_car', 'Out Car'), ('ignore', 'Ignore'), ('error', 'Error')], max_length=12, verbose_name='Статус для четвёртого интервала')),
            ],
            options={
                'verbose_name': 'Настройка для OkoDrive_status по Activity_type (WALKING)',
                'verbose_name_plural': 'Настройки для OkoDrive_status по Activity_type (WALKING)',
                'ordering': ['-activity_type'],
            },
        ),
        migrations.AddConstraint(
            model_name='speedintervalsettings',
            constraint=models.UniqueConstraint(condition=models.Q(('is_main', True)), fields=('is_main',), name='unique_is_main'),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='auth.user'),
        ),
    ]
