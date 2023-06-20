# myproject/routing.py

from django.urls import re_path
from main.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/socker-server/', ChatConsumer.as_asgi()),
]
