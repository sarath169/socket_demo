from django.urls import path

from .consumers import WSConsumer
ws_urlpatterns = [
    path('ws_users/', WSConsumer.as_asgi())
]