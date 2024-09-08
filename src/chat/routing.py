from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/socket-server/',ChatConsumer.as_asgi() ),
]