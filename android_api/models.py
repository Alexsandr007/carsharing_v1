from django.db import models
from django.db.models import UniqueConstraint, Q
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from android_api.services.generating_interval_values_dict import get_interval_values_dict


class OkoDriveStatuses(models.TextChoices):
    in_car = 'in_car'
    out_car = 'out_car'
    ignore = 'ignore'
    error = 'error'


class ErrorNames(models.TextChoices):
    in_car = 'in_car'
    out_car = 'out_car'
    none = 'none'


class AppTypes(models.TextChoices):
    phone = 'phone'
    mirror = 'mirror'


class ActivityTypes(models.TextChoices):
    IN_VEHICLE = 'IN_VEHICLE'
    ON_BICYCLE = 'ON_BICYCLE'
    ON_FOOT = 'ON_FOOT'
    WALKING = 'WALKING'
    RUNNING = 'RUNNING'
    STILL = 'STILL'
    TILTING = 'TILTING'
    UNKNOWN = 'UNKNOWN'
    NONE = 'None'


class Parametrs(models.Model):
    value = models.FloatField()
    accuracy = models.FloatField()

    class Meta:
        abstract = True


class Bearing(Parametrs):

    class Meta:
        verbose_name = 'Bearing'
        verbose_name_plural = 'Bearings'


class Speed(Parametrs):

    class Meta:
        verbose_name = 'Speed'
        verbose_name_plural = 'Speeds'


class XY(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField()

    class Meta:
        verbose_name = 'Coordinate'
        verbose_name_plural = 'Coordinates'


class AllActivityMetrics(models.Model):
    activity = models.CharField(max_length=25, choices=ActivityTypes.choices)
    confidence = models.IntegerField()

    class Meta:
        verbose_name = 'AllActivityMetric'
        verbose_name_plural = 'AllActivityMetrics'


class Data(models.Model):
    bearing = models.OneToOneField(
        Bearing,
        on_delete=models.CASCADE,
    )
    speed = models.OneToOneField(
        Speed,
        on_delete=models.CASCADE,
    )
    xy = models.OneToOneField(
        XY,
        on_delete=models.CASCADE,
    )
    time = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=25)
    all_activity_metrics = models.ManyToManyField(
        AllActivityMetrics
    )


class Device(models.Model):
    device_id = models.IntegerField()
    data = models.OneToOneField(
        Data,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Телеметрия устройства'
        verbose_name_plural = 'Телеметрия устройств'

    def __str__(self):
        return f'Устройство {self.device_id}'


class TimeStampSetting(models.Model):
    min_interval = models.PositiveIntegerField(default=10)
    max_interval = models.PositiveIntegerField(default=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Временная метка'
        verbose_name_plural = 'Временные метки'
        ordering = ['-created_at']


class BaseOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (Базовые типы)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (Базовые типы)'
        ordering =['-activity_type']


class InVehicleOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (IN_VEHICLE)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (IN_VEHICLE)'
        ordering =['-activity_type']


class OnBicycleOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (ON_BICYCLE)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (ON_BICYCLE)'
        ordering =['-activity_type']


class OnFootOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (ON_FOOT)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (ON_FOOT)'
        ordering =['-activity_type']


class WalkingOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (WALKING)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (WALKING)'
        ordering =['-activity_type']


class RunningOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (RUNNING)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (RUNNING)'
        ordering =['-activity_type']


class TiltingOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (TILTING)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (TILTING)'
        ordering =['-activity_type']


class UnknownOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (UNKNOWN)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (UNKNOWN)'
        ordering =['-activity_type']


class StillOkoDriveSettings(models.Model):
    activity_type = models.CharField(max_length=25, choices=ActivityTypes.choices)
    speed_of_first_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для первого интервала')
    speed_of_second_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для второго интервала')
    speed_of_third_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для третьего интервала')
    speed_of_fourth_interval = models.CharField(
        max_length=12, choices=OkoDriveStatuses.choices, verbose_name='Статус для четвёртого интервала')

    def __str__(self):
        return f'Настройка статусов для {self.activity_type}'

    class Meta:
        verbose_name = 'Настройка для OkoDrive_status по Activity_type (STILL)'
        verbose_name_plural = 'Настройки для OkoDrive_status по Activity_type (STILL)'
        ordering =['-activity_type']


class SpeedIntervalSettings(models.Model):
    first_interval = models.CharField(max_length=12, verbose_name='Первый интервал')
    second_interval = models.CharField(max_length=12, verbose_name='Второй интервал')
    third_interval = models.CharField(max_length=12, verbose_name='Третий интервал')
    fourth_interval = models.CharField(max_length=12, verbose_name='Четвёртый интервал')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'Настройка промежутков скоростей для определения OkoDrive_status'

    class Meta:
        verbose_name = 'Настройка промежутков скоростей для определения OkoDrive_status'
        verbose_name_plural = 'Настройки промежутков скоростей для определения OkoDrive_status'
        constraints = [
            UniqueConstraint(fields=['is_main'], condition=Q(is_main=True),
                             name='unique_is_main')
        ]
        ordering = ['-is_main']


class CurrentUTCTime(models.Model):
    current_utc = models.CharField(max_length=2, verbose_name='Текущее значение UTC')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'UTC {self.current_utc}'



