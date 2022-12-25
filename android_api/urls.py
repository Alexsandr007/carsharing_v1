from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from android_api.views import TimeStampSettingView, DeviceViewSet, RegisterDriverView, CheckTelegramAuthView, TelegramConfirmationView

router = routers.SimpleRouter()
router.register('telemetry', DeviceViewSet, basename='telemetry')

urlpatterns = [
    path('get_settings/', TimeStampSettingView.as_view(), name='get_settings'),
    # Регистрация пользователя
    path('reg_driver/', RegisterDriverView.as_view(), name='reg_driver'),
    # Проверка регистрации
    path('reg_check/<int:device_id>/', CheckTelegramAuthView.as_view(), name='reg_check'),
    # Подтверждение телеграмма
    path('reg_confirmation/', TelegramConfirmationView.as_view(), name='reg_confirmation')
]


urlpatterns += router.urls