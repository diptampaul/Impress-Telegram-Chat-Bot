from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(), name='home'),
    path('telegram_webhook/', views.telegram_webhook, name='telegram_webhook'),
]