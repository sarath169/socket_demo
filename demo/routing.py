from django.urls import path

from .consumers import UpdtaeUserList

ws_urlpatterns = [
    path('ws_users/', UpdtaeUserList.as_asgi())
]